#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Open Interface Engineering (OpenIE) Contributors
#
# NOTE ON EMITTED DATA LICENSE:
# While this tool's source code is licensed under Apache-2.0, all corpus
# disclosures, canonical OpenIE Artifact records, WAI1 envelopes, receipts,
# and Commons Scholar ingest bundles emitted from the Free Wearable Corpus
# carry the corpus's CC0-1.0 Universal Public Domain Dedication ("CC0-1.0").
"""emit_wai_commons.py — Canonical OpenIE WAI1 envelope & Commons Scholar emitter/verifier
for the Free Wearable Corpus (`wearable_prior_art`).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

try:
    import blake3 as _native_blake3  # type: ignore[import-not-found]
except ImportError:
    _native_blake3 = None

try:
    import compression.zstd as _stdlib_zstd
except ImportError:
    _stdlib_zstd = None

try:
    import zstandard as _ext_zstd  # type: ignore[import-not-found]
except ImportError:
    _ext_zstd = None

WAI1_MAGIC = b"WAI1"
MANIFEST_MAX_LEN = 1 << 27
MANIFEST_MAX_DEPTH = 127
MANIFEST_MAX_VALUES = 1 << 22
TEXT_DECODED_MAX_LEN = 1 << 27
TEXT_WINDOW_MAX_LEN = 1 << 27
ZSTD_MAGIC_LE = 0xFD2FB528
ZSTD_SKIPPABLE_MASK = 0xFFFFFFF0
ZSTD_SKIPPABLE_MAGIC = 0x184D2A50

JWP_OBJECT_DOMAIN = b"moq-jwp:object\x01"
JWP_LEAF_DOMAIN = b"moq-jwp:merkle-leaf\x01"
JWP_GROUP_SIGN_DOMAIN = b"moq-jwp:group-sign\x01"
JWP_RECEIPT_LINK_DOMAIN = b"moq-jwp:receipt-link\x01"

OPENIE_ARTIFACT_SIGN_DOMAIN = b"openie:artifact:v1"
OPENIE_RELEASE_SIGN_DOMAIN = b"openie:wai-release-receipt:v1"
CORPUS_SLUG = "free-wearable-corpus"
CORPUS_TITLE = "Free Wearable Corpus"
ARTIFACT_PREFIX = "wearable_prior_art"
MEDIA_NS = "free_wearable"
DETERMINISTIC_SIGNER_DOMAIN = (
    b"openie:free-wearable-corpus:ed25519-release-signer:v1\x00"
    b"repo=github.com/openie-dev/free-wearable-corpus\x00license=CC0-1.0"
)
DEFAULT_SIGNER_ID = "openie:free-wearable-corpus:release-signer-v1"
DEFAULT_COMMONS_URL = "https://scholar.askdavidc.ai"
CORPUS_REPO_URL = "https://github.com/openie-dev/free-wearable-corpus"

REQUIRED_CORPUS_FIELDS = (
    "id",
    "canonical_name",
    "corpus",
    "first_disclosure_date",
    "form_factor",
    "schema_version",
)
VALID_CORPUS_KINDS = {"private", "open", "fictional", "academic", "regulatory", "standards"}
AXIS_LIST_FIELDS = ("sensors", "algorithms", "form_factor_tags")

_B3_IV = (
    0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
    0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
)
_B3_CHUNK_START = 1
_B3_CHUNK_END = 2
_B3_PARENT = 4
_B3_ROOT = 8


def _b3_compress8(
    cv: tuple[int, ...], m: tuple[int, ...], counter: int, blen: int, flags: int
) -> tuple[int, int, int, int, int, int, int, int]:
    M = 0xFFFFFFFF
    s0, s1, s2, s3, s4, s5, s6, s7 = cv
    s8, s9, s10, s11 = 0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A
    s12, s13, s14, s15 = counter & M, (counter >> 32) & M, blen, flags
    m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15 = m
    for r in range(7):
        s0 = (s0 + s4 + m0) & M; x = s12 ^ s0; s12 = ((x >> 16) | (x << 16)) & M
        s8 = (s8 + s12) & M; x = s4 ^ s8; s4 = ((x >> 12) | (x << 20)) & M
        s0 = (s0 + s4 + m1) & M; x = s12 ^ s0; s12 = ((x >> 8) | (x << 24)) & M
        s8 = (s8 + s12) & M; x = s4 ^ s8; s4 = ((x >> 7) | (x << 25)) & M

        s1 = (s1 + s5 + m2) & M; x = s13 ^ s1; s13 = ((x >> 16) | (x << 16)) & M
        s9 = (s9 + s13) & M; x = s5 ^ s9; s5 = ((x >> 12) | (x << 20)) & M
        s1 = (s1 + s5 + m3) & M; x = s13 ^ s1; s13 = ((x >> 8) | (x << 24)) & M
        s9 = (s9 + s13) & M; x = s5 ^ s9; s5 = ((x >> 7) | (x << 25)) & M

        s2 = (s2 + s6 + m4) & M; x = s14 ^ s2; s14 = ((x >> 16) | (x << 16)) & M
        s10 = (s10 + s14) & M; x = s6 ^ s10; s6 = ((x >> 12) | (x << 20)) & M
        s2 = (s2 + s6 + m5) & M; x = s14 ^ s2; s14 = ((x >> 8) | (x << 24)) & M
        s10 = (s10 + s14) & M; x = s6 ^ s10; s6 = ((x >> 7) | (x << 25)) & M

        s3 = (s3 + s7 + m6) & M; x = s15 ^ s3; s15 = ((x >> 16) | (x << 16)) & M
        s11 = (s11 + s15) & M; x = s7 ^ s11; s7 = ((x >> 12) | (x << 20)) & M
        s3 = (s3 + s7 + m7) & M; x = s15 ^ s3; s15 = ((x >> 8) | (x << 24)) & M
        s11 = (s11 + s15) & M; x = s7 ^ s11; s7 = ((x >> 7) | (x << 25)) & M

        s0 = (s0 + s5 + m8) & M; x = s15 ^ s0; s15 = ((x >> 16) | (x << 16)) & M
        s10 = (s10 + s15) & M; x = s5 ^ s10; s5 = ((x >> 12) | (x << 20)) & M
        s0 = (s0 + s5 + m9) & M; x = s15 ^ s0; s15 = ((x >> 8) | (x << 24)) & M
        s10 = (s10 + s15) & M; x = s5 ^ s10; s5 = ((x >> 7) | (x << 25)) & M

        s1 = (s1 + s6 + m10) & M; x = s12 ^ s1; s12 = ((x >> 16) | (x << 16)) & M
        s11 = (s11 + s12) & M; x = s6 ^ s11; s6 = ((x >> 12) | (x << 20)) & M
        s1 = (s1 + s6 + m11) & M; x = s12 ^ s1; s12 = ((x >> 8) | (x << 24)) & M
        s11 = (s11 + s12) & M; x = s6 ^ s11; s6 = ((x >> 7) | (x << 25)) & M

        s2 = (s2 + s7 + m12) & M; x = s13 ^ s2; s13 = ((x >> 16) | (x << 16)) & M
        s8 = (s8 + s13) & M; x = s7 ^ s8; s7 = ((x >> 12) | (x << 20)) & M
        s2 = (s2 + s7 + m13) & M; x = s13 ^ s2; s13 = ((x >> 8) | (x << 24)) & M
        s8 = (s8 + s13) & M; x = s7 ^ s8; s7 = ((x >> 7) | (x << 25)) & M

        s3 = (s3 + s4 + m14) & M; x = s14 ^ s3; s14 = ((x >> 16) | (x << 16)) & M
        s9 = (s9 + s14) & M; x = s4 ^ s9; s4 = ((x >> 12) | (x << 20)) & M
        s3 = (s3 + s4 + m15) & M; x = s14 ^ s3; s14 = ((x >> 8) | (x << 24)) & M
        s9 = (s9 + s14) & M; x = s4 ^ s9; s4 = ((x >> 7) | (x << 25)) & M

        if r < 6:
            m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15 = (
                m2, m6, m3, m10, m7, m0, m4, m13, m1, m11, m12, m5, m9, m14, m15, m8,
            )
    return (s0 ^ s8, s1 ^ s9, s2 ^ s10, s3 ^ s11, s4 ^ s12, s5 ^ s13, s6 ^ s14, s7 ^ s15)


def _b3_words(block: bytes) -> tuple[int, ...]:
    if len(block) < 64:
        block = block + b"\x00" * (64 - len(block))
    return struct.unpack("<16I", block)


def _b3_chunk_output(chunk: bytes, counter: int) -> tuple[tuple[int, ...], tuple[int, ...], int, int, int]:
    if not chunk:
        return (_B3_IV, (0,) * 16, counter, 0, _B3_CHUNK_START | _B3_CHUNK_END)
    n_len = len(chunk)
    cv: tuple[int, ...] = _B3_IV
    off = 0
    first = True
    while n_len - off > 64:
        cv = _b3_compress8(cv, struct.unpack_from("<16I", chunk, off), counter, 64, _B3_CHUNK_START if first else 0)
        first = False
        off += 64
    last = chunk[off:]
    return (cv, _b3_words(last), counter, len(last), _B3_CHUNK_END | (_B3_CHUNK_START if first else 0))


def _blake3_pure(data: bytes) -> bytes:
    mv = memoryview(data)
    total_len = len(mv)
    stack: list[tuple[int, ...]] = []
    n_chunks = (total_len - 1) // 1024 + 1 if total_len > 0 else 1
    for idx in range(n_chunks - 1):
        ch = bytes(mv[idx * 1024 : (idx + 1) * 1024])
        cv_in, w, c, bl, f = _b3_chunk_output(ch, idx)
        cv = _b3_compress8(cv_in, w, c, bl, f)
        total = idx + 1
        while (total & 1) == 0:
            cv = _b3_compress8(_B3_IV, stack.pop() + cv, 0, 64, _B3_PARENT)
            total >>= 1
        stack.append(cv)
    last_chunk = bytes(mv[(n_chunks - 1) * 1024 :]) if total_len > 0 else b""
    out = _b3_chunk_output(last_chunk, n_chunks - 1)
    while stack:
        cv_in, w, c, bl, f = out
        right_cv = _b3_compress8(cv_in, w, c, bl, f)
        out = (_B3_IV, stack.pop() + right_cv, 0, 64, _B3_PARENT)
    cv_in, w, c, bl, f = out
    return struct.pack("<8I", *_b3_compress8(cv_in, w, c, bl, f | _B3_ROOT))


def blake3_bytes(data: bytes) -> bytes:
    if _native_blake3 is not None:
        return _native_blake3.blake3(data).digest()
    return _blake3_pure(data)


def blake3_hex(data: bytes) -> str:
    return blake3_bytes(data).hex()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def self_test_blake3() -> None:
    assert _blake3_pure(b"").hex() == "af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262"
    assert _blake3_pure(b"abc").hex() == "6437b3ac38465133ffb63b75273a8db548c558465d79db03fd359c6cd5bd9d85"
    vec2500 = bytes(i % 251 for i in range(2500))
    assert _blake3_pure(vec2500).hex() == "95e809954ebdd862debeb347d5715c09e73d150cd0704d4bbd834993a730e2ff"


def parse_zstd_frame_limits(payload: bytes) -> tuple[int, int | None]:
    if len(payload) < 5:
        raise ValueError("zstd_malformed: payload shorter than RFC 8878 frame header")
    (magic,) = struct.unpack_from("<I", payload, 0)
    if (magic & ZSTD_SKIPPABLE_MASK) == ZSTD_SKIPPABLE_MAGIC:
        raise ValueError("zstd_malformed: skippable frame at start of WAI zstd payload")
    if magic != ZSTD_MAGIC_LE:
        raise ValueError(f"zstd_malformed: bad magic 0x{magic:08x}")
    fhd = payload[4]
    fcs_flag = (fhd >> 6) & 0x03
    single_segment = (fhd >> 5) & 0x01
    if (fhd >> 3) & 0x01:
        raise ValueError("zstd_malformed: reserved bit set in Frame_Header_Descriptor")
    pos = 5
    window_size: int | None = None
    if not single_segment:
        if pos >= len(payload):
            raise ValueError("zstd_malformed: truncated Window_Descriptor")
        wd = payload[pos]
        pos += 1
        window_base = 1 << (10 + (wd >> 3))
        window_size = window_base + (window_base >> 3) * (wd & 0x07)
        if window_size > TEXT_WINDOW_MAX_LEN:
            raise ValueError(f"text_window_too_large: {window_size} > {TEXT_WINDOW_MAX_LEN}")
    pos += (0, 1, 2, 4)[fhd & 0x03]
    fcs_bytes = (1 if single_segment else 0, 2, 4, 8)[fcs_flag]
    declared_size: int | None = None
    if fcs_bytes > 0:
        if pos + fcs_bytes > len(payload):
            raise ValueError("zstd_malformed: truncated Frame_Content_Size")
        if fcs_bytes == 1:
            declared_size = payload[pos]
        elif fcs_bytes == 2:
            declared_size = struct.unpack_from("<H", payload, pos)[0] + 256
        elif fcs_bytes == 4:
            declared_size = struct.unpack_from("<I", payload, pos)[0]
        else:
            declared_size = struct.unpack_from("<Q", payload, pos)[0]
        if declared_size > TEXT_DECODED_MAX_LEN:
            raise ValueError(f"text_decoded_too_long: {declared_size} > {TEXT_DECODED_MAX_LEN}")
        if single_segment and declared_size > TEXT_WINDOW_MAX_LEN:
            raise ValueError(f"text_window_too_large: {declared_size} > {TEXT_WINDOW_MAX_LEN}")
    return (window_size or declared_size or 0, declared_size)


def zstd_compress_deterministic(data: bytes, level: int = 19) -> bytes:
    if len(data) > TEXT_DECODED_MAX_LEN:
        raise ValueError(f"text_decoded_too_long: {len(data)} > {TEXT_DECODED_MAX_LEN}")
    if _stdlib_zstd is not None:
        out = _stdlib_zstd.compress(data, level=level)
    elif _ext_zstd is not None:
        cctx = _ext_zstd.ZstdCompressor(level=level, write_content_size=True, write_checksum=True)
        out = cctx.compress(data)
    else:
        zstd_bin = shutil.which("zstd")
        if not zstd_bin:
            raise RuntimeError("No Zstandard encoder available")
        out = subprocess.run([zstd_bin, f"-{level}", "-q", "--check", "-c"], input=data, capture_output=True, check=True).stdout
    parse_zstd_frame_limits(out)
    return out


def zstd_decompress_checked(payload: bytes) -> bytes:
    parse_zstd_frame_limits(payload)
    if _stdlib_zstd is not None:
        out = _stdlib_zstd.decompress(payload)
    elif _ext_zstd is not None:
        dctx = _ext_zstd.ZstdDecompressor(max_window_size=TEXT_WINDOW_MAX_LEN)
        out = dctx.decompress(payload, max_output_size=TEXT_DECODED_MAX_LEN + 1)
    else:
        zstd_bin = shutil.which("zstd")
        if not zstd_bin:
            raise RuntimeError("No Zstandard decoder available")
        out = subprocess.run([zstd_bin, "-d", "-q", "-c"], input=payload, capture_output=True, check=True).stdout
    if len(out) > TEXT_DECODED_MAX_LEN:
        raise ValueError(f"text_decoded_too_long: {len(out)} > {TEXT_DECODED_MAX_LEN}")
    return out


def _count_json_values_and_depth(val: Any, depth: int = 1) -> tuple[int, int]:
    if isinstance(val, dict):
        total, max_d = 1, depth
        for child in val.values():
            c_cnt, c_d = _count_json_values_and_depth(child, depth + 1)
            total += c_cnt
            max_d = max(max_d, c_d)
        return total, max_d
    if isinstance(val, list):
        total, max_d = 1, depth
        for child in val:
            c_cnt, c_d = _count_json_values_and_depth(child, depth + 1)
            total += c_cnt
            max_d = max(max_d, c_d)
        return total, max_d
    return 1, depth


def _strict_manifest_parse(manifest_bytes: bytes) -> dict[str, Any]:
    if len(manifest_bytes) > MANIFEST_MAX_LEN:
        raise ValueError(f"manifest_too_large: {len(manifest_bytes)} > {MANIFEST_MAX_LEN}")
    raw_text = manifest_bytes.decode("utf-8")

    def no_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        seen: dict[str, Any] = {}
        for k, v in pairs:
            if k in seen:
                raise ValueError(f"manifest_duplicate_member: {k!r}")
            seen[k] = v
        return seen

    def check_int_token(token: str) -> int:
        if token == "-0":
            raise ValueError("manifest_bad_integer: '-0' forbidden")
        return int(token)

    manifest = json.loads(raw_text, object_pairs_hook=no_duplicate_pairs, parse_int=check_int_token)
    if not isinstance(manifest, dict):
        raise ValueError("manifest_malformed: root must be object")
    val_count, max_depth = _count_json_values_and_depth(manifest, depth=1)
    if max_depth > MANIFEST_MAX_DEPTH:
        raise ValueError(f"manifest_too_deep: {max_depth} > {MANIFEST_MAX_DEPTH}")
    if val_count > MANIFEST_MAX_VALUES:
        raise ValueError(f"manifest_too_many_values: {val_count} > {MANIFEST_MAX_VALUES}")
    wai_ver = manifest.get("wai")
    if not isinstance(wai_ver, str) or "." not in wai_ver or wai_ver.split(".")[0] != "1":
        raise ValueError(f"manifest_unsupported_version: {wai_ver!r}")
    for req_str in ("media", "intent"):
        if not isinstance(manifest.get(req_str), str) or not manifest[req_str]:
            raise ValueError(f"manifest_malformed: missing {req_str}")
    mr = manifest.get("model_requirement")
    if not isinstance(mr, dict) or not isinstance(mr.get("capability"), str) or not mr["capability"]:
        raise ValueError("manifest_malformed: missing model_requirement.capability")
    cond = manifest.get("conditioning")
    if not isinstance(cond, dict) or not isinstance(cond.get("kind"), str) or not cond["kind"]:
        raise ValueError("manifest_malformed: missing conditioning.kind")
    return manifest


def build_wai1_envelope(manifest_obj: dict[str, Any], payload_bytes: bytes) -> bytes:
    manifest_bytes = json.dumps(manifest_obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    _strict_manifest_parse(manifest_bytes)
    if len(payload_bytes) > 0xFFFFFFFF:
        raise ValueError("payload_too_large")
    return WAI1_MAGIC + struct.pack("<I", len(manifest_bytes)) + manifest_bytes + struct.pack("<I", len(payload_bytes)) + payload_bytes


def parse_wai1_envelope(wai_bytes: bytes) -> tuple[dict[str, Any], bytes, bytes]:
    if len(wai_bytes) < 12 or wai_bytes[:4] != WAI1_MAGIC:
        raise ValueError("wai1_bad_magic_or_truncated")
    (man_len,) = struct.unpack_from("<I", wai_bytes, 4)
    if man_len > MANIFEST_MAX_LEN or 8 + man_len + 4 > len(wai_bytes):
        raise ValueError("wai1_manifest_bounds")
    manifest_raw = wai_bytes[8 : 8 + man_len]
    manifest = _strict_manifest_parse(manifest_raw)
    (payload_len,) = struct.unpack_from("<I", wai_bytes, 8 + man_len)
    payload_start = 12 + man_len
    if payload_start + payload_len != len(wai_bytes):
        raise ValueError("wai1_payload_len_mismatch")
    return manifest, manifest_raw, wai_bytes[payload_start:]


def load_or_derive_ed25519_signer(signing_key_arg: str | None = None) -> tuple[Ed25519PrivateKey, bytes, str, str]:
    raw_spec = signing_key_arg or os.environ.get("OPENIE_WAI_SIGNING_KEY", "").strip()
    signer_id = os.environ.get("OPENIE_WAI_SIGNER_ID", DEFAULT_SIGNER_ID).strip() or DEFAULT_SIGNER_ID
    if raw_spec:
        if re.fullmatch(r"[0-9a-fA-F]{64}", raw_spec):
            sk = Ed25519PrivateKey.from_private_bytes(bytes.fromhex(raw_spec))
            mode = "configured-seed"
        else:
            loaded = serialization.load_pem_private_key(Path(raw_spec).read_bytes(), password=None)
            if not isinstance(loaded, Ed25519PrivateKey):
                raise ValueError("Not an Ed25519 private key")
            sk = loaded
            mode = "configured-pem"
    else:
        sk = Ed25519PrivateKey.from_private_bytes(blake3_bytes(DETERMINISTIC_SIGNER_DOMAIN))
        mode = "deterministic-corpus-v1"
    pk_bytes = sk.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    return sk, pk_bytes, signer_id, mode


def jwp_group_signing_payload(
    *,
    track_alias: int,
    group_id: int,
    root_hash_hex: str,
    leaf_count: int,
    joules_total: int,
    group_start: str,
    group_end: str,
    signer_pubkey_hex: str,
    signer_id: str,
) -> bytes:
    gs_b = group_start.encode("utf-8")
    ge_b = group_end.encode("utf-8")
    sid_b = signer_id.encode("utf-8")
    return (
        JWP_GROUP_SIGN_DOMAIN
        + track_alias.to_bytes(8, "big")
        + group_id.to_bytes(8, "big")
        + bytes.fromhex(root_hash_hex)
        + leaf_count.to_bytes(8, "big")
        + joules_total.to_bytes(8, "big")
        + len(gs_b).to_bytes(4, "big")
        + gs_b
        + len(ge_b).to_bytes(4, "big")
        + ge_b
        + bytes.fromhex(signer_pubkey_hex)
        + len(sid_b).to_bytes(4, "big")
        + sid_b
    )


def artifact_signing_payload(canonical_id: str, content_sha256: str, release_tarball_blake3: str) -> bytes:
    return (
        OPENIE_ARTIFACT_SIGN_DOMAIN
        + b"\x00"
        + canonical_id.encode("utf-8")
        + b"\x00"
        + content_sha256.encode("utf-8")
        + b"\x00"
        + release_tarball_blake3.encode("utf-8")
    )


def release_receipt_signing_payload(
    *,
    version: str,
    envelope_blake3: str,
    envelope_sha256: str,
    tarball_blake3: str,
    tarball_sha256: str,
    artifacts_blake3: str,
    artifacts_sha256: str,
    commons_blake3: str,
    commons_sha256: str,
) -> bytes:
    fields = (
        version,
        envelope_blake3,
        envelope_sha256,
        tarball_blake3,
        tarball_sha256,
        artifacts_blake3,
        artifacts_sha256,
        commons_blake3,
        commons_sha256,
    )
    return OPENIE_RELEASE_SIGN_DOMAIN + b"\x00" + "\x00".join(fields).encode("utf-8")


def derive_release_timestamp(version: str, override: str | None = None) -> str:
    if override:
        return override
    for q, md in ((".Q1", "01-01"), (".Q2", "04-01"), (".Q3", "07-01"), (".Q4", "10-01")):
        if version.endswith(q):
            return f"{version[:-3]}-{md}T00:00:00Z"
    if re.fullmatch(r"v?[0-9]{4}\.[0-9]{2}\.[0-9]{2}", version):
        return f"{version.lstrip('v').replace('.', '-')}T00:00:00Z"
    return "2026-01-01T00:00:00Z"


def entry_all_tags(entry: dict[str, Any]) -> list[str]:
    tags: list[str] = []
    if entry.get("form_factor"):
        tags.append(str(entry["form_factor"]))
    for field in AXIS_LIST_FIELDS:
        for t in entry.get(field) or []:
            tags.append(str(t))
    return sorted(set(tags))


def load_and_validate_strict(corpus_path: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    errors: list[str] = []
    for lineno, raw_line in enumerate(corpus_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        entry = json.loads(line)
        entries.append(entry)
        for field in REQUIRED_CORPUS_FIELDS:
            if field not in entry or entry[field] in (None, ""):
                errors.append(f"line {lineno} ({entry.get('id', '?')}): missing `{field}`")
        if entry.get("corpus") not in VALID_CORPUS_KINDS:
            errors.append(f"line {lineno} ({entry.get('id', '?')}): invalid corpus")
        if entry.get("schema_version") != 1:
            errors.append(f"line {lineno} ({entry.get('id', '?')}): schema_version != 1")
        tier = entry.get("tier", 1)
        if tier not in (1, 2):
            errors.append(f"line {lineno} ({entry.get('id', '?')}): invalid tier {tier!r}")
        eid = entry.get("id")
        if eid:
            if eid in seen_ids:
                errors.append(f"line {lineno}: duplicate id `{eid}`")
            seen_ids.add(eid)
        if not entry.get("draft"):
            for qf in ("disclosure_citation", "first_disclosure_date"):
                if entry.get(qf) in (None, ""):
                    errors.append(f"{eid}: missing `{qf}`")
            srcs = entry.get("sources")
            if not isinstance(srcs, list) or not srcs:
                errors.append(f"{eid}: `sources` must be non-empty list")
            if tier == 1:
                if not (entry.get("prior_art_notes") or "").strip():
                    errors.append(f"{eid}: Tier 1 missing `prior_art_notes`")
                if not entry_all_tags(entry):
                    errors.append(f"{eid}: Tier 1 missing axis tags")
    if errors:
        raise ValueError("Strict corpus validation failed:\n  " + "\n  ".join(errors[:20]))
    return entries


def build_acyclic_lineage_dag(
    entries: list[dict[str, Any]], lineage_doc: dict[str, Any] | None = None
) -> tuple[dict[str, list[str]], dict[str, list[str]], int, int]:
    by_id = {e["id"]: e for e in entries}
    date_of = {eid: str(e.get("first_disclosure_date") or "") for eid, e in by_id.items()}
    parents_raw: dict[str, set[str]] = {eid: set() for eid in by_id}
    children_raw: dict[str, set[str]] = {eid: set() for eid in by_id}

    if lineage_doc and isinstance(lineage_doc.get("nodes"), list):
        for node in lineage_doc["nodes"]:
            nid = node.get("id")
            if nid not in by_id:
                continue
            for anc in node.get("ancestors") or []:
                if anc in by_id and anc != nid:
                    parents_raw[nid].add(anc)
                    children_raw[anc].add(nid)
            for des in node.get("descendants") or []:
                if des in by_id and des != nid:
                    children_raw[nid].add(des)
                    parents_raw[des].add(nid)
    else:
        for e in entries:
            eid = e["id"]
            for anc in e.get("lineage_ancestors") or []:
                if anc in by_id and anc != eid:
                    parents_raw[eid].add(anc)
                    children_raw[anc].add(eid)
            for des in e.get("lineage_descendants") or []:
                if des in by_id and des != eid:
                    children_raw[eid].add(des)
                    parents_raw[des].add(eid)

    def detect_cycles(ch_map: dict[str, set[str]]) -> list[list[str]]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {eid: WHITE for eid in by_id}
        found: list[list[str]] = []
        for start in sorted(by_id.keys(), key=lambda i: (date_of[i], i)):
            if color[start] != WHITE:
                continue
            stack = [(start, iter(sorted(ch_map[start])))]
            path = [start]
            color[start] = GRAY
            while stack:
                node, it = stack[-1]
                try:
                    nxt = next(it)
                except StopIteration:
                    color[node] = BLACK
                    stack.pop()
                    path.pop()
                    continue
                if color[nxt] == GRAY and nxt in path:
                    found.append(path[path.index(nxt) :] + [nxt])
                elif color[nxt] == WHITE:
                    color[nxt] = GRAY
                    stack.append((nxt, iter(sorted(ch_map[nxt]))))
                    path.append(nxt)
        return found

    raw_cycles = detect_cycles(children_raw)
    for cyc in raw_cycles:
        edges = [(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)]
        back_edges = [(u, v) for (u, v) in edges if (date_of[u], u) > (date_of[v], v)]
        u, v = max(back_edges or edges, key=lambda uv: (date_of[uv[0]], uv[0]))
        children_raw[u].discard(v)
        parents_raw[v].discard(u)

    final_cycles = detect_cycles(children_raw)
    if final_cycles:
        raise ValueError(f"DAG 0-cycle gate failed: {final_cycles}")
    return (
        {eid: sorted(parents_raw[eid]) for eid in by_id},
        {eid: sorted(children_raw[eid]) for eid in by_id},
        len(raw_cycles),
        0,
    )


def make_energy_cost_record(reported_j: float | None, acquisition_class: str = "unmetered") -> dict[str, Any]:
    if reported_j is not None:
        if reported_j < 0:
            raise ValueError("reported_energy_j must be non-negative")
        return {
            "status": "reported_j",
            "reported_j": reported_j,
            "joules_micro": int(round(reported_j * 1_000_000)),
            "acquisition_class": acquisition_class if acquisition_class != "unmetered" else "Estimator",
            "note": "Explicitly reported energy measurement provided at build time.",
        }
    return {
        "status": "unmetered",
        "reported_j": None,
        "joules_micro": 0,
        "acquisition_class": "unmetered",
        "note": "Unmetered build host (joules_micro=0 is the WAI unmetered marker, never a claim of zero physical energy).",
    }


def build_canonical_artifacts(
    *,
    entries: list[dict[str, Any]],
    version: str,
    release_timestamp: str,
    tarball_name: str,
    tarball_bytes_len: int,
    tarball_blake3: str,
    tarball_sha256: str,
    parents_of: dict[str, list[str]],
    children_of: dict[str, list[str]],
    raw_cycles_resolved: int,
    signer_sk: Ed25519PrivateKey,
    signer_pubkey_hex: str,
    signer_id: str,
    energy_record: dict[str, Any],
) -> tuple[list[dict[str, Any]], bytes]:
    wai_filename = f"corpus-{version}.wai"
    entry_canon_b3: dict[str, str] = {}
    entry_canon_sha: dict[str, str] = {}
    entry_canon_id: dict[str, str] = {}

    for e in entries:
        eid = e["id"]
        cbytes = json.dumps(e, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        b3 = blake3_hex(cbytes)
        entry_canon_b3[eid] = b3
        entry_canon_sha[eid] = sha256_hex(cbytes)
        entry_canon_id[eid] = f"blake3:{ARTIFACT_PREFIX}:{b3}"

    timestamp_pointers = {
        "rfc3161_request": "request.tsq",
        "rfc3161_freetsa": "freetsa.tsr",
        "rfc3161_digicert": "digicert.tsr",
        "rfc3161_wai_receipt_request": "wai_receipt.tsq",
        "rfc3161_wai_receipt_freetsa": "wai_receipt.freetsa.tsr",
        "rfc3161_wai_receipt_digicert": "wai_receipt.digicert.tsr",
        "opentimestamps_tarball": f"{tarball_name}.ots",
        "opentimestamps_wai_receipt": "WAI_RECEIPT.json.ots",
        "wai_receipt": "WAI_RECEIPT.json",
    }
    interchange_envelope = {
        "format": "WAI1",
        "wai": "1.0",
        "media_type": "application/vnd.wai",
        "envelope_file": wai_filename,
        "capability": "wai.text.zstd",
        "fallback": None,
        "receipt_file": "WAI_RECEIPT.json",
    }

    records: list[dict[str, Any]] = []
    per_corpus_counts = {k: 0 for k in sorted(VALID_CORPUS_KINDS)}
    axis_tag_set: set[str] = set()
    commons_grade_count = 0
    draft_count = 0

    for idx, e in enumerate(entries):
        eid = e["id"]
        corpus_kind = str(e.get("corpus", ""))
        if corpus_kind in per_corpus_counts:
            per_corpus_counts[corpus_kind] += 1
        is_draft = bool(e.get("draft"))
        if is_draft:
            draft_count += 1
        else:
            commons_grade_count += 1

        tags = entry_all_tags(e)
        axis_tag_set.update(tags)
        cid = entry_canon_id[eid]
        c_b3 = entry_canon_b3[eid]
        c_sha = entry_canon_sha[eid]
        sig_hex = signer_sk.sign(artifact_signing_payload(cid, c_sha, tarball_blake3)).hex()
        parent_ids = parents_of.get(eid, [])
        child_ids = children_of.get(eid, [])

        modality_variants = [
            {"modality": "text/jsonl", "locator": f"corpus.jsonl#id={eid}"},
            {"modality": "text/jsonl", "locator": f"{corpus_kind}.jsonl#id={eid}"},
            {"modality": "text/markdown", "locator": f"CORPUS_INDEX.md#{eid}"},
            {"modality": "application/vnd.wai", "locator": f"{wai_filename}#entry={idx}"},
            {"modality": "application/scholar.idea+json", "locator": f"commons_ingest_bundle.json#{MEDIA_NS}:{eid}"},
        ] + [{"modality": "text/markdown", "locator": f"cross_cuts/{t}.md#{eid}"} for t in tags]

        records.append({
            "schema": "openie.artifact.canonical/v1",
            "artifact_kind": f"{ARTIFACT_PREFIX}_entry",
            "canonical_id": cid,
            "entry_id": eid,
            "entry_index": idx,
            "version": version,
            "released_at": release_timestamp,
            "title": e.get("canonical_name", eid),
            "corpus": corpus_kind,
            "first_disclosure_date": e.get("first_disclosure_date"),
            "disclosure_citation": e.get("disclosure_citation"),
            "license": "CC0-1.0",
            "difficulty_rung": {
                "rung": "R6",
                "label": "Compiled Descriptor",
                "ecology_rung": "R8",
                "ecology_label": "Ecology",
                "rationale": "Three-axis (form x sensor x algorithm) compiled 35 U.S.C. 102/103 wearable & biosensor prior-art descriptor in the R8 Free Wearable Commons",
            },
            "energy_cost_j": energy_record,
            "verification_status": {
                "passed": True,
                "gate": "validate.py --strict + chronological_dag_0_cycle",
                "schema_valid": True,
                "strict_quality_bar": True,
                "commons_grade": not is_draft,
                "draft": is_draft,
                "dag_cycles": 0,
                "raw_declared_cycles_resolved": raw_cycles_resolved,
                "dag_gate_passed": True,
                "human_in_gate": False,
            },
            "provenance_chain": {
                "content_blake3": c_b3,
                "content_sha256": c_sha,
                "release_tarball": tarball_name,
                "release_tarball_blake3": tarball_blake3,
                "release_tarball_sha256": tarball_sha256,
                "signature_scheme": "ed25519-rfc8032",
                "signing_domain": OPENIE_ARTIFACT_SIGN_DOMAIN.decode("ascii"),
                "signer_id": signer_id,
                "signer_pubkey_ed25519": signer_pubkey_hex,
                "signature_ed25519": sig_hex,
                "lineage_parents": parent_ids,
                "lineage_parent_canonical_ids": [entry_canon_id[p] for p in parent_ids],
                "lineage_children": child_ids,
                "timestamp_pointers": timestamp_pointers,
            },
            "modality_variants": modality_variants,
            "interchange_envelope": interchange_envelope,
            "payload": e,
        })

    release_cid = f"blake3:{ARTIFACT_PREFIX}:{tarball_blake3}"
    release_sig_hex = signer_sk.sign(artifact_signing_payload(release_cid, tarball_sha256, tarball_blake3)).hex()
    records.append({
        "schema": "openie.artifact.canonical/v1",
        "artifact_kind": f"{ARTIFACT_PREFIX}_release",
        "canonical_id": release_cid,
        "entry_id": f"release-{version}",
        "entry_index": len(entries),
        "version": version,
        "released_at": release_timestamp,
        "title": f"{CORPUS_TITLE} Quarterly Release {version}",
        "corpus": "all",
        "first_disclosure_date": release_timestamp[:10],
        "disclosure_citation": CORPUS_REPO_URL,
        "license": "CC0-1.0",
        "difficulty_rung": {
            "rung": "R8",
            "label": "Ecology",
            "descriptor_rung": "R6",
            "descriptor_label": "Compiled Descriptor",
            "rationale": "Complete multi-lineage CC0-1.0 defensive prior-art wearable & physiological biosensor commons ecology",
        },
        "energy_cost_j": energy_record,
        "verification_status": {
            "passed": True,
            "gate": "validate.py --strict + chronological_dag_0_cycle",
            "schema_valid": True,
            "strict_quality_bar": True,
            "commons_grade": True,
            "draft": False,
            "dag_cycles": 0,
            "raw_declared_cycles_resolved": raw_cycles_resolved,
            "dag_gate_passed": True,
            "human_in_gate": False,
        },
        "provenance_chain": {
            "content_blake3": tarball_blake3,
            "content_sha256": tarball_sha256,
            "release_tarball": tarball_name,
            "release_tarball_blake3": tarball_blake3,
            "release_tarball_sha256": tarball_sha256,
            "signature_scheme": "ed25519-rfc8032",
            "signing_domain": OPENIE_ARTIFACT_SIGN_DOMAIN.decode("ascii"),
            "signer_id": signer_id,
            "signer_pubkey_ed25519": signer_pubkey_hex,
            "signature_ed25519": release_sig_hex,
            "lineage_parents": [],
            "lineage_parent_canonical_ids": [],
            "lineage_children": [e["id"] for e in entries if not parents_of.get(e["id"])][:64],
            "timestamp_pointers": timestamp_pointers,
        },
        "modality_variants": [
            {"modality": "application/gzip", "locator": tarball_name},
            {"modality": "application/vnd.wai", "locator": wai_filename},
            {"modality": "application/x-ndjson", "locator": "artifacts.canonical.jsonl"},
            {"modality": "application/json", "locator": "WAI_RECEIPT.json"},
            {"modality": "application/json", "locator": "commons_ingest_bundle.json"},
        ],
        "interchange_envelope": interchange_envelope,
        "payload": {
            "version": version,
            "tarball_name": tarball_name,
            "tarball_bytes": tarball_bytes_len,
            "entry_count": len(entries),
            "commons_grade_count": commons_grade_count,
            "draft_count": draft_count,
            "per_corpus_counts": per_corpus_counts,
            "subsystem_tag_count": len(axis_tag_set),
            "lineage_node_count": len(entries),
            "lineage_edge_count": sum(len(v) for v in parents_of.values()),
            "repository": CORPUS_REPO_URL,
        },
    })

    jsonl_bytes = "".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in records).encode("utf-8")
    return records, jsonl_bytes


def _normalize_yyyymmdd(date_str: str | None) -> str:
    if not date_str:
        return "20260101"
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", str(date_str).strip())
    return f"{m.group(1)}{m.group(2) or '01'}{m.group(3) or '01'}" if m else "20260101"


def _extract_year(date_str: str | None) -> int | None:
    if not date_str:
        return None
    m = re.match(r"^(\d{4})", str(date_str).strip())
    return int(m.group(1)) if m else None


def _primary_url(entry: dict[str, Any]) -> str:
    for candidate in [entry.get("disclosure_citation")] + list(entry.get("sources") or []):
        if isinstance(candidate, str):
            m = re.search(r"https?://[^\s)>\"]+", candidate)
            if m:
                return m.group(0).rstrip(".,;)")
    return f"{CORPUS_REPO_URL}/blob/main/corpus.jsonl#{entry['id']}"


def build_commons_ingest_bundle(
    *,
    entries: list[dict[str, Any]],
    canonical_records: list[dict[str, Any]],
    version: str,
    release_timestamp: str,
    wai_filename: str,
    wai_blake3: str,
    wai_sha256: str,
    tarball_name: str,
    tarball_blake3: str,
    tarball_sha256: str,
    parents_of: dict[str, list[str]],
    children_of: dict[str, list[str]],
) -> tuple[dict[str, Any], bytes]:
    canon_id_by_entry = {
        r["entry_id"]: r["canonical_id"]
        for r in canonical_records
        if r["artifact_kind"] == f"{ARTIFACT_PREFIX}_entry"
    }
    by_id = {e["id"]: e for e in entries}
    base_qids = ["wd:Q1662484", "wd:Q167666", "wd:Q1156684"]

    entities: list[dict[str, Any]] = [
        {"id": "wd:Q1662484", "label": "wearable technology", "ty": "concept", "aliases": ["wearable device"]},
        {"id": "wd:Q167666", "label": "biosensor", "ty": "concept", "aliases": ["physiological sensor"]},
        {"id": "wd:Q1156684", "label": "prior art", "ty": "legal_concept", "aliases": ["defensive publication"]},
        {"id": "wd:Q6938433", "label": "CC0", "ty": "license", "aliases": ["CC0-1.0"]},
    ]
    seen_ent = {x["id"] for x in entities}
    creator_set: set[str] = set()
    for e in entries:
        for t in entry_all_tags(e):
            eid = f"e:wearable_tag:{t}"
            if eid not in seen_ent:
                seen_ent.add(eid)
                entities.append({"id": eid, "label": t.replace("-", " "), "ty": "subsystem", "aliases": [t]})
        cr = str(e.get("creator") or "").strip()
        if cr:
            creator_set.add(cr)

    authors = [{"id": "author:openie-commons", "name": "Open Interface Engineering (OpenIE) Commons"}]
    author_id_by_name = {"Open Interface Engineering (OpenIE) Commons": "author:openie-commons"}
    for cr in sorted(creator_set):
        slug = re.sub(r"[^a-z0-9]+", "-", cr.lower()).strip("-")[:64] or "unknown"
        aid = f"author:fwc:{slug}"
        if aid not in {a["id"] for a in authors}:
            authors.append({"id": aid, "name": cr})
        author_id_by_name[cr] = aid

    venues = [{"id": f"venue:{CORPUS_SLUG}", "name": f"{CORPUS_TITLE} (CC0-1.0 Defensive Prior Art Commons)"}]
    release_work_id = f"openie:work:{CORPUS_SLUG}-{version}"
    works: list[dict[str, Any]] = [
        {
            "id": release_work_id,
            "title": f"{CORPUS_TITLE} Release {version} (WAI1 Envelope & Canonical Prior-Art Substrate)",
            "abstract": f"Release {version} WAI1 envelope ({wai_filename}) containing {len(entries)} validated wearable & biosensor disclosures.",
            "year": _extract_year(release_timestamp) or 2026,
            "language": "en",
            "author_ids": ["author:openie-commons"],
            "author_names": ["Open Interface Engineering (OpenIE) Commons"],
            "venue_id": f"venue:{CORPUS_SLUG}",
            "concept_ids": base_qids,
            "source": "commons",
        }
    ]
    work_id_by_entry: dict[str, str] = {}
    for e in entries:
        eid = e["id"]
        wid = f"openie:{ARTIFACT_PREFIX}:{eid}"
        work_id_by_entry[eid] = wid
        cr = str(e.get("creator") or "Unknown Creator").strip()
        works.append({
            "id": wid,
            "title": f"{e.get('canonical_name', eid)} — Prior Art Disclosure ({e.get('first_disclosure_date', 'undated')})",
            "abstract": str(e.get("prior_art_notes") or e.get("disclosure_citation") or ""),
            "year": _extract_year(e.get("first_disclosure_date")),
            "language": "en",
            "author_ids": [author_id_by_name.get(cr, "author:openie-commons")],
            "author_names": [cr],
            "venue_id": f"venue:{CORPUS_SLUG}",
            "concept_ids": base_qids,
            "source": "commons",
        })

    citations: list[dict[str, Any]] = []
    for eid, p_list in sorted(parents_of.items()):
        for anc in p_list:
            citations.append({
                "citing": work_id_by_entry[eid],
                "cited": work_id_by_entry[anc],
                "predicate": "builds_on_prior_art",
            })
    if not citations and entries:
        citations.append({"citing": work_id_by_entry[entries[0]["id"]], "cited": release_work_id, "predicate": "part_of_release"})

    bundle_media: list[dict[str, Any]] = []
    media_records: list[dict[str, Any]] = []
    bundle_ideas: list[dict[str, Any]] = []
    idea_atoms: list[dict[str, Any]] = []
    native_atoms: list[dict[str, Any]] = []

    overview_statement = (
        f"{CORPUS_TITLE} release {version} seals {len(entries)} defensive wearable & biosensor prior-art "
        f"disclosures in WAI1 container {wai_filename} (BLAKE3 {wai_blake3[:16]}...) under CC0-1.0."
    )

    for idx, e in enumerate(entries, start=1):
        eid = e["id"]
        mid = f"{MEDIA_NS}:{eid}"
        corpus_kind = str(e.get("corpus", "open"))
        platform = f"{MEDIA_NS}_{corpus_kind}"
        url = _primary_url(e)
        creator = str(e.get("creator") or "Unknown Creator").strip()
        fdate = str(e.get("first_disclosure_date") or "")
        yyyymmdd = _normalize_yyyymmdd(fdate)
        name = str(e.get("canonical_name") or eid)
        quote_text = str(e.get("prior_art_notes") or e.get("disclosure_citation") or f"{name} ({fdate})")
        tags = entry_all_tags(e)
        statement = f"{name} ({fdate or 'undated'}, {creator}, {corpus_kind}): {quote_text[:320]}"
        conf = 0.65 if e.get("draft") else 1.0

        bundle_media.append({
            "id": mid, "kind": "document", "platform": platform, "url": url,
            "title": f"{name} ({fdate or 'undated'})", "uploader": creator,
            "upload_date": yyyymmdd, "duration_s": None, "native_language": "en",
            "license": "CC0-1.0", "work_id": work_id_by_entry[eid],
        })
        media_records.append({
            "platform": platform, "id": mid, "url": url,
            "title": f"{name} ({fdate or 'undated'})", "uploader": creator,
            "upload_date": yyyymmdd, "duration_s": None, "native_language": "en",
            "available_captions": None, "license": "CC0-1.0",
            "transcript_source": "verified_openie",
            "segments": [{"start": 1.0, "end": 1.0, "text": quote_text, "source": "verified_openie"}],
            "audio_path": None, "kind": "document",
        })
        bundle_ideas.append({
            "media_id": mid, "statement": statement, "kind": "claim", "speaker": creator,
            "quote": quote_text, "t_start": 1.0, "t_end": 1.0, "channel": "metadata",
            "source": "verified_openie", "confidence": conf,
            "entities": [name] + tags[:8], "qids": base_qids, "lang": "en",
        })
        idea_atoms.append({
            "id": f"idea:{MEDIA_NS}:{eid}",
            "canonical_id": canon_id_by_entry[eid],
            "statement": statement, "quote": quote_text, "speaker": creator,
            "channel_owner": creator, "media_id": mid, "modality": "written",
            "media_kind": "document", "platform": platform,
            "title": f"{name} ({fdate or 'undated'})", "date": fdate or None,
            "lang": "en", "citation": url, "locator": f"corpus.jsonl:{idx}",
            "t_start": 1.0, "source": "verified_openie",
            "entities": [{"id": q, "label": q} for q in base_qids],
        })
        native_atoms.append({
            "media_id": mid, "modality": "structure3d",
            "summary": f"{name} wearable morphology: form_factor={e.get('form_factor')}, contact={e.get('contact_surface')}",
            "locator_spec": f"page:1#wearable:{eid}", "t_start": 1.0, "t_end": 1.0,
            "channel": "geometry3d", "source": "d2_mesh_3d", "confidence": conf,
            "work_id": work_id_by_entry[eid], "entities": [name] + tags[:6],
        })

    trail_name = f"{CORPUS_TITLE} {version}"
    ranked_hubs = sorted(
        [e for e in entries if not e.get("draft")],
        key=lambda e: (-len(children_of.get(e["id"], [])), str(e.get("first_disclosure_date") or ""), e["id"]),
    )[:20]
    stars = [
        {
            "item_id": f"idea:{MEDIA_NS}:{h['id']}",
            "item_kind": "idea",
            "title": f"{h.get('canonical_name', h['id'])} ({h.get('first_disclosure_date', '?')})",
            "summary": str(h.get("prior_art_notes") or h.get("disclosure_citation") or "")[:280],
            "citation": _primary_url(h),
            "trail": trail_name,
            "note": f"Lineage anchor ({canon_id_by_entry[h['id']][:36]}...)",
            "pinned_by": "agent",
        }
        for h in ranked_hubs
    ]

    roots_with_desc = sorted(
        [eid for eid in by_id if not parents_of.get(eid) and children_of.get(eid)],
        key=lambda eid: (-len(children_of[eid]), str(by_id[eid].get("first_disclosure_date") or ""), eid),
    )[:20]
    trails_list = []
    for root_id in roots_with_desc:
        visited = {root_id}
        queue = [root_id]
        while queue and len(visited) < 64:
            cur = queue.pop(0)
            for ch in children_of.get(cur, []):
                if ch not in visited:
                    visited.add(ch)
                    queue.append(ch)
        ordered_steps = sorted(visited, key=lambda i: (str(by_id[i].get("first_disclosure_date") or ""), i))
        trails_list.append({
            "trail_id": f"trail:lineage:{root_id}",
            "title": f"{by_id[root_id].get('canonical_name', root_id)} Prior-Art Lineage",
            "root_entry_id": root_id,
            "root_canonical_id": canon_id_by_entry[root_id],
            "step_count": len(ordered_steps),
            "steps": [
                {
                    "entry_id": sid,
                    "canonical_id": canon_id_by_entry[sid],
                    "name": by_id[sid].get("canonical_name", sid),
                    "first_disclosure_date": by_id[sid].get("first_disclosure_date"),
                    "corpus": by_id[sid].get("corpus"),
                    "ancestors": parents_of.get(sid, []),
                    "descendants": children_of.get(sid, []),
                }
                for sid in ordered_steps
            ],
        })
    if not trails_list and entries:
        r0 = entries[0]["id"]
        trails_list.append({
            "trail_id": f"trail:lineage:{r0}",
            "title": f"{entries[0].get('canonical_name', r0)} Prior-Art Lineage",
            "root_entry_id": r0,
            "root_canonical_id": canon_id_by_entry[r0],
            "step_count": 1,
            "steps": [{"entry_id": r0, "canonical_id": canon_id_by_entry[r0], "name": entries[0].get("canonical_name", r0)}],
        })

    bundle_doc: dict[str, Any] = {
        "schema": "openie.commons.ingest_bundle/v1",
        "version": version,
        "license": "CC0-1.0",
        "generated_at": release_timestamp,
        "overview": overview_statement,
        "wai_envelope": {
            "file": wai_filename, "blake3": wai_blake3, "sha256": wai_sha256,
            "tarball_file": tarball_name, "tarball_blake3": tarball_blake3, "tarball_sha256": tarball_sha256,
        },
        "summary": {
            "entries": len(entries), "entities": len(entities), "works": len(works),
            "citations": len(citations), "media_records": len(media_records),
            "idea_atoms": len(idea_atoms), "native_atoms": len(native_atoms),
            "stars": len(stars), "lineage_trails": len(trails_list),
        },
        "stars": stars,
        "lineage_trails": {
            "presence_update": {
                "display_name": f"{CORPUS_TITLE} Prior-Art Release Bot",
                "interests": [CORPUS_TITLE, "wearable biosensor prior art", "PPG ECG EEG", "open medical hardware"],
                "add_trail": trail_name,
            },
            "trails": trails_list,
        },
        "media_records": media_records,
        "idea_atoms": idea_atoms,
        "entities": entities,
        "authors": authors,
        "venues": venues,
        "works": works,
        "citations": citations,
        "media": bundle_media,
        "ideas": bundle_ideas,
        "native_atoms": native_atoms,
    }
    return bundle_doc, (json.dumps(bundle_doc, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build_wai_receipt(
    *,
    version: str,
    release_timestamp: str,
    wai_filename: str,
    wai_bytes: bytes,
    decoded_bytes_len: int,
    decoded_blake3: str,
    decoded_sha256: str,
    tarball_name: str,
    tarball_bytes_len: int,
    tarball_blake3: str,
    tarball_sha256: str,
    artifacts_bytes_len: int,
    artifacts_blake3: str,
    artifacts_sha256: str,
    commons_bytes_len: int,
    commons_blake3: str,
    commons_sha256: str,
    entry_count: int,
    canonical_record_count: int,
    signer_sk: Ed25519PrivateKey,
    signer_pubkey_hex: str,
    signer_id: str,
    signer_key_mode: str,
    energy_record: dict[str, Any],
) -> tuple[dict[str, Any], bytes]:
    env_b3 = blake3_hex(wai_bytes)
    env_sha = sha256_hex(wai_bytes)
    jwp_content_hash = blake3_hex(JWP_OBJECT_DOMAIN + wai_bytes)
    jwp_merkle_root = blake3_hex(JWP_LEAF_DOMAIN + bytes.fromhex(jwp_content_hash))
    joules_micro = int(energy_record.get("joules_micro") or 0)

    jwp_payload = jwp_group_signing_payload(
        track_alias=0, group_id=1, root_hash_hex=jwp_merkle_root, leaf_count=1,
        joules_total=joules_micro, group_start=release_timestamp, group_end=release_timestamp,
        signer_pubkey_hex=signer_pubkey_hex, signer_id=signer_id,
    )
    jwp_sig_bytes = signer_sk.sign(jwp_payload)
    jwp_receipt_link_hash = blake3_hex(JWP_RECEIPT_LINK_DOMAIN + jwp_payload + jwp_sig_bytes)

    jwp_group_receipt = {
        "kind": "group",
        "track_alias": 0,
        "group_id": 1,
        "root_hash": jwp_merkle_root,
        "leaf_count": 1,
        "joules_total": joules_micro,
        "group_start": release_timestamp,
        "group_end": release_timestamp,
        "signer_pubkey": signer_pubkey_hex,
        "signer_id": signer_id,
        "sig": jwp_sig_bytes.hex(),
        "parent_receipt_hash": None,
    }
    jwp_object_receipt = {
        "kind": "object",
        "track_alias": 0,
        "group_id": 1,
        "object_id": 0,
        "content_hash": jwp_content_hash,
        "joules_micro": joules_micro,
        "origin": signer_id,
        "merkle_proof": {"siblings": [], "direction_bits": 0, "leaf_index": 0},
    }

    rel_sig_hex = signer_sk.sign(
        release_receipt_signing_payload(
            version=version, envelope_blake3=env_b3, envelope_sha256=env_sha,
            tarball_blake3=tarball_blake3, tarball_sha256=tarball_sha256,
            artifacts_blake3=artifacts_blake3, artifacts_sha256=artifacts_sha256,
            commons_blake3=commons_blake3, commons_sha256=commons_sha256,
        )
    ).hex()

    receipt_doc: dict[str, Any] = {
        "schema": "openie.wai.receipt/v1",
        "version": version,
        "released_at": release_timestamp,
        "license": "CC0-1.0",
        "corpus": CORPUS_SLUG,
        "corpus_entries": entry_count,
        "canonical_records": canonical_record_count,
        "envelope": {
            "file": wai_filename, "format": "WAI1", "wai": "1.0",
            "capability": "wai.text.zstd", "fallback": None,
            "bytes": len(wai_bytes), "blake3": env_b3, "sha256": env_sha,
            "jwp_content_hash_blake3": jwp_content_hash,
            "jwp_merkle_root_blake3": jwp_merkle_root,
            "jwp_receipt_link_blake3": jwp_receipt_link_hash,
            "decoded_bytes": decoded_bytes_len,
            "decoded_blake3": decoded_blake3,
            "decoded_sha256": decoded_sha256,
        },
        "artifacts": {
            tarball_name: {"bytes": tarball_bytes_len, "blake3": tarball_blake3, "sha256": tarball_sha256},
            "artifacts.canonical.jsonl": {"bytes": artifacts_bytes_len, "blake3": artifacts_blake3, "sha256": artifacts_sha256},
            wai_filename: {"bytes": len(wai_bytes), "blake3": env_b3, "sha256": env_sha},
            "commons_ingest_bundle.json": {"bytes": commons_bytes_len, "blake3": commons_blake3, "sha256": commons_sha256},
        },
        "energy_cost_j": energy_record,
        "signature": {
            "scheme": "ed25519-rfc8032",
            "signing_domain": OPENIE_RELEASE_SIGN_DOMAIN.decode("ascii"),
            "signer_id": signer_id,
            "key_mode": signer_key_mode,
            "signer_pubkey_ed25519": signer_pubkey_hex,
            "release_sig_ed25519": rel_sig_hex,
        },
        "jwp_group_receipt": jwp_group_receipt,
        "jwp_object_receipt": jwp_object_receipt,
        "offline_verify_command": f"python3 tools/emit_wai_commons.py --verify releases/{version}",
    }
    return receipt_doc, (json.dumps(receipt_doc, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write_checksum_files(release_dir: Path, ordered_files: list[str]) -> None:
    sha_lines, b3_lines = [], []
    for fname in ordered_files:
        data = (release_dir / fname).read_bytes()
        sha_lines.append(f"{sha256_hex(data)}  {fname}\n")
        b3_lines.append(f"{blake3_hex(data)}  {fname}\n")
    (release_dir / "SHA256SUMS").write_text("".join(sha_lines), encoding="utf-8")
    (release_dir / "BLAKE3SUMS").write_text("".join(b3_lines), encoding="utf-8")


def verify_offline(target: Path, quiet: bool = False) -> dict[str, Any]:
    self_test_blake3()
    if target.is_dir():
        release_dir = target
        wai_candidates = sorted(release_dir.glob("corpus-*.wai"))
        if not wai_candidates:
            raise ValueError(f"No corpus-*.wai file found in {release_dir}")
        wai_path = wai_candidates[0]
    elif target.is_file():
        wai_path = target
        release_dir = target.parent
    else:
        raise ValueError(f"Verification target not found: {target}")

    wai_bytes = wai_path.read_bytes()
    manifest, manifest_raw, payload = parse_wai1_envelope(wai_bytes)
    cap = manifest["model_requirement"]["capability"]
    decoded = zstd_decompress_checked(payload) if cap == "wai.text.zstd" else payload
    decoded_text = decoded.decode("utf-8")
    dec_sha, dec_b3 = sha256_hex(decoded), blake3_hex(decoded)
    env_b3, env_sha = blake3_hex(wai_bytes), sha256_hex(wai_bytes)

    receipt_path = release_dir / "WAI_RECEIPT.json"
    verified_records = 0
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        env_meta = receipt["envelope"]
        if env_meta["blake3"] != env_b3 or env_meta["sha256"] != env_sha:
            raise ValueError("WAI_RECEIPT envelope hash mismatch")
        if env_meta["decoded_blake3"] != dec_b3 or env_meta["decoded_sha256"] != dec_sha:
            raise ValueError("WAI_RECEIPT decoded hash mismatch")

        expected_jwp_obj = blake3_hex(JWP_OBJECT_DOMAIN + wai_bytes)
        expected_jwp_root = blake3_hex(JWP_LEAF_DOMAIN + bytes.fromhex(expected_jwp_obj))
        grp = receipt["jwp_group_receipt"]
        obj = receipt["jwp_object_receipt"]
        mp = obj.get("merkle_proof")
        if not isinstance(mp, dict) or mp.get("siblings") != [] or mp.get("direction_bits") != 0 or mp.get("leaf_index") != 0:
            raise ValueError("JWP object merkle_proof malformed")
        if obj["content_hash"] != expected_jwp_obj or grp["root_hash"] != expected_jwp_root:
            raise ValueError("JWP content/root hash mismatch")

        vk = Ed25519PublicKey.from_public_bytes(bytes.fromhex(receipt["signature"]["signer_pubkey_ed25519"]))
        jwp_pay = jwp_group_signing_payload(
            track_alias=int(grp["track_alias"]), group_id=int(grp["group_id"]),
            root_hash_hex=grp["root_hash"], leaf_count=int(grp["leaf_count"]),
            joules_total=int(grp["joules_total"]), group_start=grp["group_start"],
            group_end=grp["group_end"], signer_pubkey_hex=grp["signer_pubkey"],
            signer_id=grp["signer_id"],
        )
        try:
            vk.verify(bytes.fromhex(grp["sig"]), jwp_pay)
        except InvalidSignature as exc:
            raise ValueError("JWP group signature invalid") from exc

        art_table = receipt["artifacts"]
        for fname, meta in art_table.items():
            fbytes = (release_dir / fname).read_bytes()
            if len(fbytes) != meta["bytes"] or blake3_hex(fbytes) != meta["blake3"] or sha256_hex(fbytes) != meta["sha256"]:
                raise ValueError(f"Artifact digest mismatch for {fname}")

        version = receipt["version"]
        tarball_name = f"corpus-{version}.tar.gz"
        rel_pay = release_receipt_signing_payload(
            version=version, envelope_blake3=env_b3, envelope_sha256=env_sha,
            tarball_blake3=art_table[tarball_name]["blake3"], tarball_sha256=art_table[tarball_name]["sha256"],
            artifacts_blake3=art_table["artifacts.canonical.jsonl"]["blake3"],
            artifacts_sha256=art_table["artifacts.canonical.jsonl"]["sha256"],
            commons_blake3=art_table["commons_ingest_bundle.json"]["blake3"],
            commons_sha256=art_table["commons_ingest_bundle.json"]["sha256"],
        )
        vk.verify(bytes.fromhex(receipt["signature"]["release_sig_ed25519"]), rel_pay)

        if (release_dir / "artifacts.canonical.jsonl").read_bytes() != decoded:
            raise ValueError("Decoded .wai differs from artifacts.canonical.jsonl")

        tar_b3 = art_table[tarball_name]["blake3"]
        for lineno, line in enumerate(decoded_text.splitlines(), start=1):
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("license") != "CC0-1.0" or rec["verification_status"].get("human_in_gate") is not False:
                raise ValueError(f"Record {lineno}: invariant failure")
            prov = rec["provenance_chain"]
            cid = rec["canonical_id"]
            if rec["artifact_kind"] == f"{ARTIFACT_PREFIX}_entry":
                pbytes = json.dumps(rec["payload"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
                expected_b3, expected_sha = blake3_hex(pbytes), sha256_hex(pbytes)
            else:
                expected_b3, expected_sha = tar_b3, art_table[tarball_name]["sha256"]
            if cid != f"blake3:{ARTIFACT_PREFIX}:{expected_b3}":
                raise ValueError(f"Record {lineno}: canonical_id mismatch")
            vk.verify(bytes.fromhex(prov["signature_ed25519"]), artifact_signing_payload(cid, expected_sha, tar_b3))
            verified_records += 1

        for sums_name, fn in (("SHA256SUMS", sha256_hex), ("BLAKE3SUMS", blake3_hex)):
            sp = release_dir / sums_name
            if sp.exists():
                for line in sp.read_text(encoding="utf-8").splitlines():
                    if line.strip():
                        digest, fname = line.split("  ", 1)
                        if fn((release_dir / fname).read_bytes()) != digest:
                            raise ValueError(f"{sums_name} mismatch for {fname}")

    if not quiet:
        print(f"  PASS: WAI1 header & SPEC §2 limits ({len(manifest_raw)} B manifest, {len(payload)} B payload)")
        print(f"  PASS: Envelope BLAKE3 `{env_b3}` -> {verified_records} signed `{ARTIFACT_PREFIX}` records")
    return {"ok": True, "envelope_blake3": env_b3, "verified_records": verified_records}


def sync_commons_scholar(*, release_dir: Path, version: str, commons_url: str | None = None, dry_run: bool = False, offline: bool = False) -> None:
    if offline:
        return
    base_raw = commons_url or os.environ.get("COMMONS_BASE_URL", "").strip() or DEFAULT_COMMONS_URL
    base_url = re.sub(r"/api/.*$", "", base_raw.rstrip("/")) or DEFAULT_COMMONS_URL
    if dry_run:
        print(f"  [commons] dry-run: ready-to-ingest bundle at {release_dir / 'commons_ingest_bundle.json'}")
        return
    req = urllib.request.Request(f"{base_url}/api/stats", headers={"User-Agent": f"{CORPUS_SLUG}/{version}"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=4.0) as resp:
            print(f"  [commons] health ping {base_url}/api/stats -> HTTP {resp.status}")
    except (urllib.error.URLError, TimeoutError, OSError):
        print(f"  [commons] health ping {base_url}/api/stats unreachable; continuing non-blocking")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Emit and verify WAI1 envelopes for {CORPUS_TITLE}.")
    parser.add_argument("--verify", metavar="PATH")
    parser.add_argument("--push-commons-only", action="store_true")
    parser.add_argument("--version")
    parser.add_argument("--release-dir")
    parser.add_argument("--tarball")
    parser.add_argument("--corpus", default="corpus.jsonl")
    parser.add_argument("--lineage", default="lineage.json")
    parser.add_argument("--encoding", choices=("zstd", "utf8"), default="zstd")
    parser.add_argument("--timestamp")
    parser.add_argument("--signing-key")
    parser.add_argument("--reported-energy-j", type=float, default=None)
    parser.add_argument("--energy-class", default="unmetered")
    parser.add_argument("--push-commons", action="store_true")
    parser.add_argument("--commons-url")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if args.verify:
        try:
            verify_offline(Path(args.verify))
            return 0
        except Exception as exc:
            print(f"VERIFY FAILED: {exc}", file=sys.stderr)
            return 1

    if args.push_commons_only:
        sync_commons_scholar(release_dir=Path(args.release_dir), version=args.version, commons_url=args.commons_url, dry_run=args.dry_run, offline=args.offline)
        return 0

    if not args.version or not args.release_dir or not args.tarball:
        parser.error("Emission requires --version, --release-dir, and --tarball")

    self_test_blake3()
    version = args.version
    release_dir = Path(args.release_dir)
    tarball_path = Path(args.tarball)
    corpus_path = Path(args.corpus)
    lineage_path = Path(args.lineage)
    release_dir.mkdir(parents=True, exist_ok=True)
    release_ts = derive_release_timestamp(version, args.timestamp)

    entries = load_and_validate_strict(corpus_path)
    lineage_doc = json.loads(lineage_path.read_text(encoding="utf-8")) if lineage_path.exists() else None
    parents_of, children_of, raw_cycles_resolved, _ = build_acyclic_lineage_dag(entries, lineage_doc)

    tar_bytes = tarball_path.read_bytes()
    tar_b3, tar_sha = blake3_hex(tar_bytes), sha256_hex(tar_bytes)
    tarball_name = tarball_path.name

    energy_rec = make_energy_cost_record(args.reported_energy_j, args.energy_class)
    signer_sk, signer_pk_bytes, signer_id, signer_mode = load_or_derive_ed25519_signer(args.signing_key)
    signer_pk_hex = signer_pk_bytes.hex()

    canon_records, canon_bytes = build_canonical_artifacts(
        entries=entries, version=version, release_timestamp=release_ts,
        tarball_name=tarball_name, tarball_bytes_len=len(tar_bytes),
        tarball_blake3=tar_b3, tarball_sha256=tar_sha,
        parents_of=parents_of, children_of=children_of, raw_cycles_resolved=raw_cycles_resolved,
        signer_sk=signer_sk, signer_pubkey_hex=signer_pk_hex, signer_id=signer_id, energy_record=energy_rec,
    )
    (release_dir / "artifacts.canonical.jsonl").write_bytes(canon_bytes)
    canon_b3, canon_sha = blake3_hex(canon_bytes), sha256_hex(canon_bytes)

    wai_filename = f"corpus-{version}.wai"
    wai_payload = zstd_compress_deterministic(canon_bytes, level=19) if args.encoding == "zstd" else canon_bytes
    manifest_obj = {
        "wai": "1.0",
        "media": "text",
        "intent": "replicate",
        "model_requirement": {"capability": "wai.text.zstd" if args.encoding == "zstd" else "wai.text.utf8", "fallback": None},
        "conditioning": {"kind": "zstd" if args.encoding == "zstd" else "utf8"},
        "security": {"encryption": "none", "kid": 0},
        "target": {
            "schema": "openie.artifact.canonical/v1",
            "format": "application/x-ndjson",
            "encoding": "utf-8",
            "corpus": CORPUS_SLUG,
            "version": version,
            "license": "CC0-1.0",
            "records": len(canon_records),
            "corpus_entries": len(entries),
            "decoded_bytes": len(canon_bytes),
            "decoded_sha256": canon_sha,
            "decoded_blake3": canon_b3,
        },
    }
    wai_bytes = build_wai1_envelope(manifest_obj, wai_payload)
    (release_dir / wai_filename).write_bytes(wai_bytes)
    wai_b3, wai_sha = blake3_hex(wai_bytes), sha256_hex(wai_bytes)

    _, commons_bytes = build_commons_ingest_bundle(
        entries=entries, canonical_records=canon_records, version=version, release_timestamp=release_ts,
        wai_filename=wai_filename, wai_blake3=wai_b3, wai_sha256=wai_sha,
        tarball_name=tarball_name, tarball_blake3=tar_b3, tarball_sha256=tar_sha,
        parents_of=parents_of, children_of=children_of,
    )
    (release_dir / "commons_ingest_bundle.json").write_bytes(commons_bytes)
    commons_b3, commons_sha = blake3_hex(commons_bytes), sha256_hex(commons_bytes)

    _, receipt_bytes = build_wai_receipt(
        version=version, release_timestamp=release_ts, wai_filename=wai_filename, wai_bytes=wai_bytes,
        decoded_bytes_len=len(canon_bytes), decoded_blake3=canon_b3, decoded_sha256=canon_sha,
        tarball_name=tarball_name, tarball_bytes_len=len(tar_bytes), tarball_blake3=tar_b3, tarball_sha256=tar_sha,
        artifacts_bytes_len=len(canon_bytes), artifacts_blake3=canon_b3, artifacts_sha256=canon_sha,
        commons_bytes_len=len(commons_bytes), commons_blake3=commons_b3, commons_sha256=commons_sha,
        entry_count=len(entries), canonical_record_count=len(canon_records),
        signer_sk=signer_sk, signer_pubkey_hex=signer_pk_hex, signer_id=signer_id,
        signer_key_mode=signer_mode, energy_record=energy_rec,
    )
    (release_dir / "WAI_RECEIPT.json").write_bytes(receipt_bytes)

    write_checksum_files(release_dir, [
        tarball_name, "artifacts.canonical.jsonl", wai_filename, "WAI_RECEIPT.json", "commons_ingest_bundle.json",
    ])
    verify_offline(release_dir, quiet=True)
    print(f"  Canonical OpenIE JSONL: {release_dir / 'artifacts.canonical.jsonl'} ({len(canon_records)} records)")
    print(f"  WAI1 Envelope:          {release_dir / wai_filename} ({len(wai_bytes)} bytes, BLAKE3 {wai_b3[:16]}...)")
    if args.push_commons or args.dry_run:
        sync_commons_scholar(release_dir=release_dir, version=version, commons_url=args.commons_url, dry_run=args.dry_run, offline=args.offline)
    return 0


if __name__ == "__main__":
    sys.exit(main())
