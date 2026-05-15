---
title: Timestamping
layout: default
nav_order: 7
---

# Timestamping the Corpus

## Why this matters

The corpus is the prior art commons. For an entry to function as defensive
publication, the date of public disclosure must be defensible against
challenge. Git commit timestamps are not third-party attested — they can
be rewritten, and they are not the kind of evidence courts expect. We
need external timestamping by recognized third parties.

This document specifies the ceremony, the choices, the verification
procedure, and the alternatives evaluated and rejected.

## What gets timestamped

A release tarball containing:

- `corpus.jsonl` — the master corpus at release time
- `SCHEMA.md` — schema spec at release time
- `OBVIOUSNESS_TEMPLATE.md` — combination-argument template at release time
- `CORPUS_INDEX.md`, `lineage.json` — derived artifacts
- Per-corpus mirrors (private/open/fictional/academic/regulatory/standards
  `.jsonl` files)
- `cross_cuts/` — all single-axis and intersection cross-cut analyses

A SHA-256 hash is computed over the tarball and submitted to the
timestamping authorities. The timestamp asserts "this exact byte sequence
existed at this exact time" — the strongest form of pre-existence proof.

## The three layers

### Layer 1: RFC 3161 — FreeTSA

FreeTSA is a free public RFC 3161 timestamping authority. Verifiable with
standard `openssl ts -verify` tooling.

**Trust profile**: medium. Well-regarded but not the most broadly trusted
in legal contexts. Always-on free option.

### Layer 2: RFC 3161 — DigiCert

DigiCert operates a free public RFC 3161 endpoint at
`http://timestamp.digicert.com`. Among the most-trusted commercial CAs and
TSAs worldwide.

**Trust profile**: high. Accepted in nearly any court that accepts digital
evidence.

### Layer 3: OpenTimestamps (Bitcoin anchoring)

OpenTimestamps is a free, decentralized timestamping protocol that anchors
hashes into the Bitcoin blockchain. Once anchored, falsifying the timestamp
would require rewriting Bitcoin proof-of-work history.

**Trust profile**: cryptographically maximal. No trust in any single
authority.

**Latency**: initial proof in seconds, upgraded to Bitcoin-anchored proof
in ~1-6 hours. Run `ots upgrade *.ots` later to fetch the upgraded proof
and commit it.

## Why all three

Belt and braces. Each layer fails differently:

- FreeTSA could go offline or rotate keys. Other timestamps survive.
- DigiCert could change endpoint policy. Other timestamps survive.
- Bitcoin could face a 51% attack rewriting recent history
  (extraordinarily unlikely). Other timestamps survive.

For zero marginal cost (all three are free) we get three independent
proofs of pre-existence.

## Release cadence

Quarterly tags are the minimum: 2026.Q3, 2026.Q4, 2027.Q1, etc. Each
release captures corpus state at that moment with full timestamping.

For high-value individual entries — particularly those added specifically
to function as prior art against a known patent threat — interim
timestamping of just that entry is worth doing. Just hash the entry's
JSON line, submit hash to the three layers, commit receipts under
`releases/interim/<entry-id>/`.

## Verification by third parties

```
# 1. Fetch the release tarball
git clone https://github.com/openie-dev/free-wearable-corpus
cd free-wearable-corpus
TAG=2026.Q3

# 2. Verify the SHA-256
cd releases/${TAG}
sha256sum -c SHA256SUMS

# 3. Verify the FreeTSA RFC 3161 timestamp
openssl ts -verify -in freetsa.tsr \
  -data corpus-${TAG}.tar.gz \
  -CAfile cacert.pem -untrusted tsa.crt

# 4. Verify the DigiCert RFC 3161 timestamp
openssl ts -verify -in digicert.tsr \
  -data corpus-${TAG}.tar.gz \
  -CAfile digicert-cacert.pem

# 5. Verify the OpenTimestamps Bitcoin proof
ots verify corpus-${TAG}.tar.gz.ots -f corpus-${TAG}.tar.gz
```

If all three verify, the third party has cryptographic proof that the
exact contents of the corpus.jsonl in that release existed at the
timestamp moment. Anything in that corpus.jsonl is therefore a public
disclosure as of that moment, citable as 102 prior art against any patent
with a later effective filing date.

## Alternatives evaluated and rejected

**IP.com defensive publications**. Real legal weight,
examiner-discoverable, but costs $200+ per publication. Not scalable for
a 1000+ entry commons. Use IP.com selectively for highest-value entries.

**Bulletin board posting**. Old-school (USENET, mailing lists with
archives). Less rigorous than cryptographic timestamping. Skip.

**Notarization (RFC 3161 with notary signature)**. Adds physical-world
trust at high per-document cost. Skip for routine releases.

**Wayback Machine**. Indexes content but does not produce a verifiable
cryptographic timestamp. Useful supplement, not substitute. Submit the
GitHub repo and release tarball URLs to Wayback after each release for
additional informal timestamping.

## Examiner discoverability (separate from timestamping)

Timestamping proves WHEN. Discoverability ensures examiners FIND it.

Per release:

1. **Google Patents non-patent literature corpus** — Google Scholar
   indexing (the repo's GitHub Pages site gets crawled).
2. **IP.com Prior Art Database** — selective, paid, highest-value
   entries.
3. **Crossref / OSF / Zenodo preprints** — release as a citable preprint
   with a DOI. Among the cheapest paths into examiner search tools.
4. **arXiv** — if framed as a paper, releases can be submitted to arXiv
   (cs.CY or cs.HC for wearables methodology papers).
5. **CPC classification tags** — applied at entry level, ensure the
   corpus shows up in classification-based examiner searches. A61B 5/*
   (measuring for diagnostic purposes), A61B 5/02416 (PPG), A61B 5/24
   (electroencephalography), G04G 21/* (smartwatches) are the dense
   classes.
