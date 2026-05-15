---
title: Home
layout: home
nav_order: 1
description: "A public-domain prior art commons for wearable devices and body measurement. CC0."
permalink: /
---

# Free Wearable Corpus
{: .fs-9 }

A public-domain prior art commons covering watches, bracelets, rings, eyewear, hearables, headbands, patches, garments, exoskeletons, implantables, and ingestibles — across private patents, open source, science fiction, academic literature, regulatory filings, and standards bodies.
{: .fs-6 .fw-300 }

[Schema](SCHEMA.html){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Obviousness template](OBVIOUSNESS_TEMPLATE.html){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Cross-cuts](cross_cuts/){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[GitHub](https://github.com/openIE-dev/free-wearable-corpus){: .btn .fs-5 .mb-4 .mb-md-0 }

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](https://github.com/openIE-dev/free-wearable-corpus/blob/main/LICENSE)

---

**The corpus IS the prior art commons.** Every entry, at the moment of timestamped commit and quarterly release, is a defensive publication. The structured data here, combined with the cryptographic timestamping in `releases/`, is itself the invalidity-contention material.

The corpus is a **lexicon**, not a catalog. Retrieval equals citation.

---

## What's different from the Free Humanoid Corpus

Wearable patent claims read on component combinations: **form factor × sensor × algorithm**. The corpus indexes each axis independently and generates cross-cuts per single tag and per intersection.

Combining a known sensor with a known wearable form factor is per se obvious under KSR / MPEP § 2143 Rationale A. The §103 argument for any (form factor × sensor) tuple is boilerplate — see [OBVIOUSNESS_TEMPLATE.md](OBVIOUSNESS_TEMPLATE.html). Component disclosures live in the cross-cuts. The combination argument lives in the template, once.

**Component cross-cuts + one template = the §103 proof.**

---

## What it covers

Six buckets:

| Bucket | Role |
|:---|:---|
| Private | Commercial products with disclosed engineering, including patent-thicket holders. |
| Open | Open-hardware and open-source wearables. |
| Fictional | Film, TV, comics, games, literature. Strong for §103 motivation-to-combine. |
| Academic | Peer-reviewed papers, theses, conference proceedings. |
| Regulatory | FDA 510(k), De Novo, PMA decision summaries; CE MDR/IVDR filings. |
| Standards | IEEE 11073, Bluetooth SIG profiles, ISO/IEC 80601, Continua Alliance. |

---

## Provenance

Quarterly releases carry three independent cryptographic timestamps attesting pre-existence:

- **FreeTSA** (RFC 3161)
- **DigiCert** (RFC 3161)
- **OpenTimestamps** (Bitcoin-anchored)

→ [Release runbook](RELEASE_RUNBOOK.html) · [Timestamping ceremony](TIMESTAMPING.html)

---

## Use it from the command line

```bash
git clone https://github.com/openIE-dev/free-wearable-corpus.git
cd free-wearable-corpus

# Validate the corpus
python3 tools/validate.py corpus.jsonl --strict

# Look up prior art for a wearable claim
python3 tools/lookup.py "wristworn device with photoplethysmography sensor and atrial fibrillation detection"

# Scaffold a new entry interactively (then submit as a PR)
python3 tools/new_entry.py
```

---

## License

CC0 1.0. Public domain dedication. The corpus exists to be cited, copied, indexed, mirrored, embedded, ingested, and built upon. No usage license required.
