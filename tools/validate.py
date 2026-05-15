#!/usr/bin/env python3
"""validate.py — schema and quality-bar validation for corpus.jsonl.

Usage:
    python3 tools/validate.py corpus.jsonl
    python3 tools/validate.py corpus.jsonl --strict   # gate releases

In default mode, validates structural correctness only:
    - each line is valid JSON
    - required fields present
    - ids unique
    - corpus is one of {private, open, fictional, academic, regulatory, standards}
    - schema_version is 1
    - form_factor is in the controlled taxonomy
    - sensors / algorithms / form_factor_tags / output_modalities are lists
    - lineage references are reported as warnings (not errors)

In --strict mode, additionally enforces the v0.1 quality bar for any
entry with draft != true:
    Tier 1 entries (tier == 1 or unset):
      - prior_art_notes is non-empty
      - disclosure_citation is non-empty
      - first_disclosure_date is non-empty
      - sources is a non-empty list
      - at least one of {sensors, algorithms, form_factor} tagged
    Tier 2 entries (tier == 2):
      - disclosure_citation is non-empty
      - first_disclosure_date is non-empty
      - sources is a non-empty list

Exits 0 if everything passes for the requested mode; nonzero otherwise.
"""
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = (
    "id",
    "canonical_name",
    "corpus",
    "first_disclosure_date",
    "form_factor",
    "schema_version",
)

VALID_CORPUS = {"private", "open", "fictional", "academic", "regulatory", "standards"}

VALID_FORM_FACTORS = {
    "watch", "bracelet", "ring", "glasses", "goggles", "contact-lens",
    "earbud", "over-ear-headphone", "hearing-aid", "headband", "cap",
    "helmet", "patch", "garment", "belt", "pendant", "armband", "legband",
    "sock", "insole", "shoe", "body-camera", "exoskeleton", "implantable",
    "ingestible", "dental", "tattoo-electronic", "fictional-other", "other",
}

LIST_FIELDS = (
    "aliases", "form_factor_tags", "anatomical_target", "sensors", "actuators",
    "algorithms", "output_modalities", "clinical_endpoints",
    "regulatory_predicates", "clinical_trials", "ip_citations",
    "lineage_ancestors", "lineage_descendants", "sources",
    "cpc_classifications",
)


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if not a.startswith("--")]
    if not args:
        sys.exit("usage: validate.py corpus.jsonl [--strict]")
    path = Path(args[0])
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")

    errors = []
    warnings = []
    entries = []
    seen_ids = set()

    raw = path.read_text().splitlines() if path.stat().st_size else []

    for lineno, line in enumerate(raw, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {lineno}: invalid JSON ({e})")
            continue
        entries.append(entry)

        for f in REQUIRED_FIELDS:
            if f not in entry or entry[f] in (None, ""):
                errors.append(
                    f"line {lineno} ({entry.get('id', '?')}): missing required field `{f}`"
                )

        if entry.get("corpus") not in VALID_CORPUS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): corpus must be one of {sorted(VALID_CORPUS)}"
            )

        ff = entry.get("form_factor")
        if ff is not None and ff not in VALID_FORM_FACTORS:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): form_factor `{ff}` not in controlled taxonomy "
                f"(see SCHEMA.md form-factor taxonomy)"
            )

        if entry.get("schema_version") != 1:
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): schema_version must be 1 (got {entry.get('schema_version')!r})"
            )

        tier = entry.get("tier", 1)
        if tier not in (1, 2):
            errors.append(
                f"line {lineno} ({entry.get('id', '?')}): tier must be 1 or 2 (got {tier!r})"
            )

        for lf in LIST_FIELDS:
            v = entry.get(lf)
            if v is not None and not isinstance(v, list):
                errors.append(
                    f"line {lineno} ({entry.get('id', '?')}): field `{lf}` must be a list"
                )

        eid = entry.get("id")
        if eid:
            if eid in seen_ids:
                errors.append(f"line {lineno}: duplicate id `{eid}`")
            seen_ids.add(eid)

    # Lineage reference checks (warnings only)
    for entry in entries:
        for field in ("lineage_ancestors", "lineage_descendants"):
            for ref in entry.get(field) or []:
                if ref not in seen_ids:
                    warnings.append(
                        f"{entry['id']}.{field} references unknown id `{ref}`"
                    )

    # Quality bar (strict mode only)
    quality_failures = []
    if strict:
        for entry in entries:
            if entry.get("draft"):
                continue
            tier = entry.get("tier", 1)
            # Common to both tiers
            for f in ("disclosure_citation", "first_disclosure_date"):
                v = entry.get(f)
                if v in (None, ""):
                    quality_failures.append(
                        f"{entry['id']}: missing `{f}` (commons-grade entries must have it)"
                    )
            srcs = entry.get("sources")
            if not isinstance(srcs, list) or not srcs:
                quality_failures.append(
                    f"{entry['id']}: `sources` must be a non-empty list for commons-grade entries"
                )
            if tier == 1:
                # Tier 1 additionally requires prior_art_notes and component tagging
                if not (entry.get("prior_art_notes") or "").strip():
                    quality_failures.append(
                        f"{entry['id']}: missing `prior_art_notes` "
                        f"(Tier 1 commons-grade entries must have element-by-element analysis; "
                        f"flag tier:2 or draft:true if not yet ready)"
                    )
                tagged = any(
                    (entry.get(f) or []) for f in ("sensors", "algorithms", "form_factor_tags")
                ) or bool(entry.get("form_factor"))
                if not tagged:
                    quality_failures.append(
                        f"{entry['id']}: Tier 1 entries must tag at least one of "
                        f"{{form_factor, form_factor_tags, sensors, algorithms}}"
                    )

    n = len(entries)
    drafts = sum(1 for e in entries if e.get("draft"))
    tier2 = sum(1 for e in entries if e.get("tier") == 2)
    commons = n - drafts

    print(f"  Entries:        {n}")
    print(f"  Commons-grade:  {commons}")
    print(f"  Tier 2:         {tier2}")
    print(f"  Drafts:         {drafts}")
    print(f"  Unique ids:     {len(seen_ids)}")
    print(f"  Errors:         {len(errors)}")
    print(f"  Warnings:       {len(warnings)}")
    if strict:
        print(f"  Quality fails:  {len(quality_failures)}")

    for w in warnings:
        print(f"  WARN: {w}")
    for e in errors:
        print(f"  ERROR: {e}")
    if strict:
        for qf in quality_failures:
            print(f"  QUALITY: {qf}")

    if errors:
        sys.exit(1)
    if strict and quality_failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
