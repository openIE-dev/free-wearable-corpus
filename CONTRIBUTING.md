---
title: Contributing
layout: default
nav_order: 6
---

# Contributing to the Free Wearable Corpus

Thank you for considering a contribution. Before you write an entry,
please read this carefully — the contribution model here is unusual.

## What you are doing when you contribute

**You are writing a defensive publication, not a Wikipedia entry.**

Every entry in this corpus is, at the moment of timestamped release, a
public disclosure citable as 102 prior art (or as a 103 element-disclosure
that feeds the obviousness template) against any patent with a later
effective filing date. That is the corpus's reason for existing and the
reason it works.

Tight, primary-sourced, element-by-element entries strengthen the commons.
Sloppy citations, fuzzy dates, or hand-wavy prior art notes weaken it for
everyone.

## CC0 dedication

By submitting a contribution you dedicate it to the public domain under
CC0 1.0. The contribution must be your own work or already in the public
domain. Do not copy text wholesale from copyrighted sources — paraphrase
in your own words and cite the source.

## What counts as a good entry

An entry is **commons-grade** (`draft: false`, `tier: 1`) when it
satisfies all five criteria:

### 1. The disclosure citation resolves to a primary source

`disclosure_citation` must point at something a third party can retrieve
and verify:

- Paper with a DOI or stable URL
- Patent number
- Book with an ISBN
- TV / film with first-air-date
- Episode ID
- arXiv identifier
- FDA 510(k) number / De Novo decision / PMA approval order
- CE technical file reference where publicly available
- IEEE / ISO / IEC / Bluetooth SIG standards document number
- Archived URL (Wayback Machine snapshot with date)
- GitHub commit at a specific SHA

Not acceptable: "Wikipedia," "company website" without a specific page and
date, "I read this somewhere," uncited secondhand summaries.

### 2. The first disclosure date is defensible

`first_disclosure_date` is the earliest verifiable public disclosure, not
the earliest plausible date.

If a wearable was demoed at CES in January 2018 but the company filed
510(k) clearance documentation that became public in November 2017, the
November 2017 date is correct. If a sci-fi device first appeared in a
1956 short story that was later adapted into a 2002 film, the 1956 story
is correct.

When in doubt, choose the earliest date you can cite to a primary source.

### 3. The prior art notes are element-by-element analysis

This field does the most work. `prior_art_notes` should read as the kind
of analysis a competent patent examiner or invalidity-contention attorney
would write. It identifies *specific* components disclosed — form factor,
sensor modalities, algorithms, outputs, anatomical contact site — and
what claims those disclosures could anticipate.

Bad example:
> An early smartwatch with health features.

Good example:
> Wristworn form factor with two-LED green-PPG (525 nm, 50 Hz sampling)
> over the radial artery, three-axis accelerometer, on-device HR derivation
> via peak detection in the 40-220 bpm band. Disclosed in product
> documentation dated 2014-09-09 and FCC filing TXR-MEMS-A1502. Anticipates
> wristworn green-PPG HR claims post-2014. The on-device peak-detection
> algorithm is not novel relative to the Allen 2007 PPG review (academic
> entry `allen-2007-ppg`).

If you cannot write the second kind, mark the entry `draft: true` and
note in `notes` what work would be needed to clear the bar. Or submit it
as `tier: 2` — see Tiers below.

### 4. Sources are primary references

`sources` lists papers, patents, books, episodes, regulatory filings, or
standards documents. Aggregators are acceptable only as supplements, not
as the primary citation.

### 5. Patented entries enumerate patents

If `ip_status` is `patented`, then `ip_citations` must list at least one
actual patent number.

## Tiers

The corpus uses two tiers to allow density without editorial bottleneck.

**Tier 1 (default, commons-grade):** complete `prior_art_notes`, full
multi-axis tagging, primary citations. Used as anchor entries in
cross-cuts.

**Tier 2 (reference-only):** title, date, citation, bucket, minimal tags.
Populates the long tail so that lookups don't return empty. Marked
`"tier": 2`. Still requires a resolvable primary citation but does not
need full prior_art_notes. Useful for high-volume sources (FDA 510(k)
predicate chains, large patent batches, academic-paper batch imports).

A Tier 2 entry can be promoted to Tier 1 by any contributor who writes
the `prior_art_notes`.

## Submitting an entry below the quality bar

Mark the entry `"draft": true` and document in `notes` what work would
be needed to clear the bar. Drafts are welcome — they make incremental
progress visible without polluting the commons-grade entry pool.

## Practical workflow

```bash
# Scaffold a new entry interactively
python3 tools/new_entry.py

# After editing corpus.jsonl directly or merging the scaffolded entry:
python3 tools/validate.py corpus.jsonl --strict
python3 tools/index.py .
python3 tools/cross_cuts.py

# Commit the regenerated artifacts alongside your entry.
git add -A
git commit -m "corpus: add <id>"
```

## Choosing a good slug

The `id` field is a kebab-case slug used in lineage edges, cross-cuts,
and citations.

- Commercial products: `<company>-<product>` (e.g., `fitbit-charge`,
  `whoop-4`, `oura-ring-gen3`)
- Academic platforms: `<lab-or-institution>-<name>` (e.g.,
  `epfl-eglass`, `openbci-cyton`)
- Fictional entities: `<franchise>-<name>` (e.g., `dick-tracy-wrist-radio`,
  `geordi-visor-tng`, `rainbows-end-glasses`)
- Regulatory filings: `<510k-or-de-novo>-<number>` (e.g.,
  `510k-k153026-zio-patch`, `denovo-den180044-irhythm`)
- Standards: `<sdo>-<doc>` (e.g., `ieee-11073-10406`, `bt-sig-hrp`)

Slugs are immutable once another entry references them. Choose carefully.

## Multi-axis tagging

Every entry tags every axis it discloses. An EEG headband with
on-device sleep staging would carry:

```json
{
  "form_factor": "headband",
  "sensors": ["sensor-dry-eeg-electrode", "sensor-eeg"],
  "algorithms": ["algo-sleep-staging"],
  "output_modalities": ["audio", "data-only"]
}
```

Do not invent new tags casually. Propose them in a separate PR with a
rationale and pinpoint to where the first entry to use the tag documents
its scope.

## Questions

Open an issue. Discussion of methodology, taxonomy gaps, and quality bar
calibration is welcome.
