# Free Wearable Corpus

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

A structured prior art commons covering wearable devices and body
measurement — watches, bracelets, rings, eyewear, hearables, headbands,
patches, garments, exoskeletons, implantables, and ingestibles — disclosed
in private patents, open source, science fiction (film/TV/comics/games/
literature), academic literature, regulatory filings (FDA 510(k), De Novo,
CE MDR), and standards bodies.

**The corpus IS the prior art commons.** Every entry, at the moment of
timestamped commit and quarterly release, is a defensive publication. The
structured data here, combined with the cryptographic timestamping in
`releases/`, is itself the invalidity-contention material.

The corpus is a **lexicon**, not a catalog. Retrieval equals citation.

## License

CC0-1.0. Public domain dedication. See [LICENSE](LICENSE).

## Two design commitments that differ from the Free Humanoid Corpus

### Multi-axis tagging

Wearable patent claims read on component combinations: form factor × sensor
× algorithm. The corpus indexes each axis independently. Cross-cuts are
generated per single tag and per (tag × tag) intersection.

### Component cross-cuts + one combination template

Combining a known sensor with a known wearable form factor is per se
obvious under KSR / MPEP § 2143 Rationale A. The §103 argument for any
(form factor × sensor) tuple is boilerplate — see
[OBVIOUSNESS_TEMPLATE.md](OBVIOUSNESS_TEMPLATE.md). Entries supply
component disclosures. The template supplies the combination argument.
The corpus is component cross-cuts plus one template, not thousands of
pre-built combinations.

## What's in here

```
SCHEMA.md               — schema spec (currently v0.1)
OBVIOUSNESS_TEMPLATE.md — canonical §103 combination argument
TIMESTAMPING.md         — release ceremony for cryptographic timestamping
RELEASE_RUNBOOK.md      — step-by-step release procedure
CONTRIBUTING.md         — how to add an entry
README.md               — this file

corpus.jsonl            — master corpus (one JSON object per line)
private.jsonl           — generated mirror, entries with corpus="private"
open.jsonl              — generated mirror
fictional.jsonl         — generated mirror
academic.jsonl          — generated mirror
regulatory.jsonl        — generated mirror
standards.jsonl         — generated mirror

CORPUS_INDEX.md         — generated alphabetical index
lineage.json            — generated ancestor/descendant DAG

cross_cuts/             — generated per-tag prior art views
  INDEX.md              — table of all cross-cuts with counts
  <tag>.md              — chronological view of all entries disclosing <tag>
  <tag1>__<tag2>.md     — chronological view of (tag1 ∩ tag2) entries

tools/
  validate.py           — schema and quality-bar enforcement
  index.py              — generates CORPUS_INDEX.md, lineage.json, per-corpus mirrors
  cross_cuts.py         — generates single-axis and intersection cross-cuts
  lookup.py             — patent-claim → matching prior art entries
  new_entry.py          — interactive entry scaffolder

release.sh              — quarterly release ceremony with timestamping
```

## Quick start

```bash
# Validate the corpus
python3 tools/validate.py corpus.jsonl --strict

# Regenerate derived artifacts after editing corpus.jsonl
python3 tools/index.py .
python3 tools/cross_cuts.py

# Look up prior art for a wearable claim
python3 tools/lookup.py "wristworn device with photoplethysmography sensor and processor configured to detect atrial fibrillation"

# Run a quarterly release with cryptographic timestamping
./release.sh 2026.Q3
```

## Quality bar

An entry is commons-grade (not `draft: true`) when:

1. `disclosure_citation` resolves to a primary source verifiable by a
   third party.
2. `first_disclosure_date` is the earliest verifiable public disclosure,
   defensible against challenge.
3. `prior_art_notes` reads as a 102/103 anticipation analysis someone
   unrelated to us could cite without rewriting.
4. `sources` cite primary references.
5. For patented entries, `ip_citations` lists actual patent numbers.

Entries that don't yet clear this bar are merged with `draft: true` and
have explicit work items in their `notes` field.

## Cross-cuts as the working tool

The cross-cut files (`cross_cuts/<tag>.md`) are the operational form of the
commons. Each file lists every entry disclosing a given component, in
chronological order, with `prior_art_notes` and `disclosure_citation`
inline.

Use them when assessing wearable claims:

- A claim about wristworn PPG? Open `cross_cuts/watch__sensor-ppg.md` —
  anchored at the earliest disclosed wristworn PPG implementation, every
  intervening disclosure listed chronologically.
- A claim about EEG eyewear? Open `cross_cuts/glasses__sensor-eeg.md`.
- A claim about ring-form HRV? Open `cross_cuts/ring__sensor-ppg__algo-hrv.md`.

For each, drop the cited entries into [OBVIOUSNESS_TEMPLATE.md](OBVIOUSNESS_TEMPLATE.md)
and the §103 argument is complete.

## Contributing

Contributions are welcome under CC0-1.0. By submitting an entry you
dedicate the contribution to the public domain.

A good entry holds up as defensive publication. Briefly:

- Cite primary sources, not Wikipedia.
- Identify specific components disclosed using the taxonomy in
  [SCHEMA.md](SCHEMA.md): form factor, sensors, algorithms, outputs.
- Write `prior_art_notes` as element-by-element anticipation analysis.
- For patented entries, point back at academic / fictional / regulatory /
  standards prior art that anticipates the claims.

If unsure, mark the entry `draft: true` and document the work needed to
clear the quality bar.

## Provenance

Originated within Open Interface Engineering (OpenIE) as a sister project
to the Free Humanoid Corpus and Free eVTOL Corpus, applying the same
defensive-publication methodology to a different patent-thicket field. The
corpus serves the wearable and body-measurement field broadly.
