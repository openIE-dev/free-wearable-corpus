---
title: Schema
layout: default
nav_order: 4
---

# Free Wearable Corpus — Schema v0.1

## Purpose

A structured catalog of every wearable and body-measurement device — wristworn,
finger, eyewear, ear, head, torso, limb, foot, garment, patch, implantable,
ingestible — disclosed in private patents, open source, science fiction
(film/TV/comics/games/literature), academic literature, regulatory filings,
and standards bodies.

**The corpus IS the prior art commons.** Every entry, at the moment of
timestamped commit and quarterly release, is a defensive publication
artifact. `prior_art_notes` is not editorial commentary — it is the
element-by-element analysis a competent examiner or invalidity-contention
attorney can cite.

The corpus is a **lexicon**, not a catalog. A lexicon entry isn't
annotation: it is the demonstration that a specific disclosure anticipates
or motivates obviousness toward a specific claim phrase. Retrieval equals
citation.

## Two structural commitments that differ from the Free Humanoid Corpus

### 1. Multi-axis tagging — form factor × sensor × algorithm

Wearable claims are component-anchored, not platform-anchored. A claim of
"a wristworn device comprising a photoplethysmography sensor and a processor
configured to compute heart rate variability" reads on a *combination* of
three independent elements:

- form factor (`watch`, `ring`, `glasses`, `patch`, ...)
- sensor (`ppg`, `ecg`, `eeg`, `accelerometer`, ...)
- algorithm / output (`hrv`, `afib-detection`, `sleep-staging`, ...)

The corpus indexes by component, not by combination. Each entry is
multi-tagged across all three axes. Cross-cuts are generated per tag and
also per tag-intersection where useful. This is what lets the corpus scale
to wearable density (1000+ entries) without bottlenecking on editorial.

### 2. Combination obviousness is template, not per-combination work

Because adding a known sensor to a known wearable form factor is per se
obvious under KSR / MPEP § 2143 Rationale A (combining prior art elements
according to known methods to yield predictable results), the §103 proof
for any (form factor × sensor) tuple is **boilerplate that plugs into the
template**, not bespoke per-combination analysis. See
[OBVIOUSNESS_TEMPLATE.md](OBVIOUSNESS_TEMPLATE.html).

Entries supply the component disclosures. The template supplies the
combination argument. The corpus is component cross-cuts plus one template.

## Quality bar for entries

An entry is **commons-grade** (not `draft: true`) when:

- `disclosure_citation` resolves to a primary source verifiable by a
  third party (paper DOI, patent number, regulatory filing ID, episode
  ID with first-air-date, standards-document number, archive URL).
- `first_disclosure_date` is the earliest verifiable public disclosure,
  defensible against challenge.
- `prior_art_notes` reads as a 102/103 anticipation analysis someone
  unrelated to us could cite without rewriting. It identifies specific
  components disclosed (form factor, sensor modalities, algorithms,
  output channels) and what claims those disclosures could anticipate.
- `sources` cite primary references.
- For patented entries, `ip_citations` lists actual patent numbers.

Entries below the bar may be merged with `draft: true` to make
incremental progress visible.

## Entry tiers

Density without editorial bottleneck requires tiered entries.

- **Tier 1 (commons-grade, full):** complete `prior_art_notes`, full
  multi-axis tagging, primary citations. Used as anchor entries in
  cross-cuts.
- **Tier 2 (reference-only):** title, date, citation, bucket, minimal
  tags. Populates the long tail so lookups don't return empty. Marked
  `tier: 2` and not subject to the full quality bar (still requires a
  resolvable primary citation).

Both tiers participate in cross-cut generation. Tier 1 entries get full
rendering; Tier 2 entries get one-line rendering with date + citation.

## License posture

CC0-1.0. The corpus is public domain dedication. Individual entries cite
their sources but the structured catalog is unencumbered.

## Timestamping

Same ceremony as the Free Humanoid Corpus. Three independent layers per
release: FreeTSA (RFC 3161), DigiCert (RFC 3161), OpenTimestamps
(Bitcoin-anchored). See [TIMESTAMPING.md](TIMESTAMPING.html).

## Entry schema

Each entry is one record. Required [R], optional [O].

```
id                       [R]  slug, kebab-case, globally unique within corpus
canonical_name           [R]  the name most commonly used in literature
aliases                  [O]  list of alternate names, model numbers, codenames
corpus                   [R]  one of: private | open | fictional | academic | regulatory | standards
first_disclosure_date    [R]  ISO 8601 date or year; earliest verifiable public reference
disclosure_citation      [R]  source for the first_disclosure_date (DOI, ISBN, URL, patent #, 510(k) #, episode ID, standards doc #)
creator                  [R]  company / lab / studio / author / collective / agency / SDO
creator_country          [O]  ISO country code of creator

form_factor              [R]  primary form factor; see form-factor taxonomy
form_factor_tags         [O]  additional form-factor tags (multi-form devices)
contact_surface          [O]  skin | scalp | ear | nasal | dental | ocular | sublingual | intra-abdominal | vascular | sub-dermal | textile-mediated | non-contact
anatomical_target        [O]  list of body regions targeted (wrist, temporal-lobe, finger, chest, scalp-Fpz, etc.)

sensors                  [O]  list of sensor tags from sensor taxonomy
sensor_details           [O]  free text — wavelengths, electrode geometry, sampling rate, DR, channel count
actuators                [O]  list of actuator/output tags (haptic-eccentric, haptic-piezo, electrical-stim-tens, optical-stim, audio, display, ...)
compute                  [O]  on-device chip / MCU / accelerator, edge-vs-cloud split
connectivity             [O]  ble | wifi | nfc | lte-m | thread | wired | sneakernet | none
power_source             [O]  cr2032 | li-ion-rechargeable | nfc-harvested | piezoharvest | tethered | fictional | unknown
runtime                  [O]  hours or days

algorithms               [O]  list of algorithm tags (hrv, afib-detection, sleep-staging, fall-detection, seizure-detection, ...)
output_modalities        [O]  haptic | visual-display | audio | electrical-stim | thermal | drug-delivery | data-only
clinical_endpoints       [O]  list of claimed/disclosed clinical outputs (spo2, glucose, blood-pressure, eeg-bandpower, ...)

ip_status                [R]  patented | open-permissive | open-copyleft | public-domain | fictional | regulatory-filing | standards | trade-secret | unknown
ip_citations             [O]  patent numbers, license identifiers, 510(k) numbers, NCT trial IDs, repo URLs, standards doc IDs

regulatory_pathway       [O]  fda-510k | fda-de-novo | fda-pma | ce-mdr | ce-ivdr | exempt | none | fictional
regulatory_predicates    [O]  list of predicate device IDs (for 510(k) entries)
clinical_trials          [O]  list of NCT/ISRCTN identifiers

prior_art_notes          [O]  element-by-element 102/103 analysis; what claims this entry could anticipate
lineage_ancestors        [O]  ids of entries this design descends from
lineage_descendants      [O]  ids of entries that descend from this (filled in later passes)

sources                  [R]  list of citations (papers, books, articles, repos, episodes, filings, standards)
cpc_classifications      [O]  CPC codes for examiner discoverability (e.g., A61B 5/02416 for PPG)
notes                    [O]  free-text observations
draft                    [O]  boolean; true if the entry has not yet cleared the quality bar
tier                     [O]  integer 1 (full, default) or 2 (reference-only)
schema_version           [R]  integer matching schema spec version
last_updated             [R]  ISO 8601 date
```

## Form-factor taxonomy

The primary axis. Patent claims tend to read on a specific form factor.
Fiction's wearable coverage is densest in `watch`, `bracelet`, and
`glasses`.

- `watch` — wrist-mounted device with display
- `bracelet` — wrist-mounted device without display (or jewelry-style)
- `ring` — finger-worn
- `glasses` — eyewear, with or without display / HUD
- `goggles` — fully enclosed eyewear, includes VR/AR HMDs
- `contact-lens` — corneal contact
- `earbud` — in-ear
- `over-ear-headphone` — over-ear / on-ear with sensors
- `hearing-aid` — behind-the-ear / in-canal hearing aid form factor
- `headband` — forehead / scalp band
- `cap` — full-head cap (EEG cap, helmet)
- `helmet` — protective helmet with embedded electronics
- `patch` — adhesive skin patch
- `garment` — clothing-integrated (shirt, sock, glove, sports bra, smart-fabric)
- `belt` — waist-mounted
- `pendant` — neck-worn
- `armband` — upper-arm band
- `legband` — leg or thigh band
- `sock` — foot-worn textile
- `insole` — shoe insert
- `shoe` — full footwear
- `body-camera` — chest-mounted camera
- `exoskeleton` — wearable exoskeleton
- `implantable` — surgically implanted
- `ingestible` — swallowed sensor
- `dental` — tooth-mounted / mouthguard
- `tattoo-electronic` — epidermal electronics, sub-dermal printed
- `fictional-other` — fiction with no real-world form-factor match
- `other` — escape hatch with explanation in notes

## Sensor taxonomy

Tags applied to `sensors`. An entry tags every sensor modality it
discloses.

**Optical / photonic**
- `sensor-ppg` — photoplethysmography (HR, HRV, SpO2-base)
- `sensor-spo2` — pulse oximetry (red + IR)
- `sensor-multi-wavelength-ppg` — beyond red/IR, e.g. green/blue/NIR
- `sensor-fnirs` — functional near-infrared spectroscopy
- `sensor-raman` — Raman spectroscopy
- `sensor-optical-glucose` — optical glucose sensing (transcutaneous)
- `sensor-camera-rgb` — visible camera
- `sensor-camera-ir` — infrared camera
- `sensor-camera-thermal` — thermal imager
- `sensor-camera-eye` — eye-tracking camera
- `sensor-photodiode-ambient` — ambient light

**Electrophysiological**
- `sensor-ecg` — electrocardiography
- `sensor-eeg` — electroencephalography
- `sensor-emg` — electromyography
- `sensor-eog` — electrooculography
- `sensor-gsr` — galvanic skin response / EDA
- `sensor-bioimpedance` — body composition / hydration
- `sensor-respiration-impedance` — impedance pneumography

**Mechanical / motion**
- `sensor-accelerometer` — 3-axis accel
- `sensor-gyroscope` — 3-axis gyro
- `sensor-magnetometer` — 3-axis mag
- `sensor-barometer` — pressure altimeter
- `sensor-piezoelectric` — piezo strain / vibration
- `sensor-strain-gauge` — strain
- `sensor-pressure-skin` — skin-pressure / cuff pressure

**Acoustic**
- `sensor-microphone-air` — ambient audio
- `sensor-microphone-bone` — bone-conduction mic
- `sensor-stethoscope-digital` — digital auscultation
- `sensor-ppg-acoustic` — acoustic-PPG variants

**Biochemical**
- `sensor-glucose-cgm` — continuous glucose monitor (electrochemical)
- `sensor-lactate` — sweat / interstitial lactate
- `sensor-cortisol` — sweat / saliva cortisol
- `sensor-electrolyte` — Na/K/Cl in sweat
- `sensor-ph` — pH in sweat / interstitial
- `sensor-ammonia` — ammonia sensing
- `sensor-alcohol-transdermal` — transdermal alcohol
- `sensor-ketone` — ketone sensing
- `sensor-uric-acid` — uric acid
- `sensor-creatinine` — creatinine
- `sensor-cytokine` — cytokine (IL-6 etc.) sensing
- `sensor-dna-onchip` — on-device DNA / nucleic-acid sensing

**Thermal**
- `sensor-skin-temperature` — skin temp
- `sensor-core-temperature` — core temp (ingestible / tympanic)
- `sensor-heat-flux` — heat flux

**Hydration / sweat**
- `sensor-sweat-rate` — sweat rate
- `sensor-microfluidic-sweat-collection` — sweat collection channel

**Hemodynamic / vascular**
- `sensor-cuffless-bp-ptt` — pulse-transit-time cuffless BP
- `sensor-cuffless-bp-tonometry` — applanation tonometry
- `sensor-cuffless-bp-volume-clamp` — finger volume clamp
- `sensor-arterial-stiffness` — arterial stiffness inference

**Neural / brain**
- `sensor-dry-eeg-electrode` — dry contact EEG electrode
- `sensor-saline-eeg-electrode` — wet/saline EEG electrode
- `sensor-microneedle-eeg` — microneedle EEG electrode
- `sensor-meg-mini` — miniature MEG (OPM-based)

**Other**
- `sensor-uv` — UV exposure
- `sensor-tof-distance` — time-of-flight distance
- `sensor-radar-mmwave` — mmWave radar for HR / respiration
- `sensor-ultrasound-wearable` — wearable ultrasound
- `sensor-air-quality` — VOC / PM2.5 wearable

## Algorithm / output taxonomy

Tags applied to `algorithms`. An entry tags every algorithm it discloses,
whether on-device or cloud.

**Cardiovascular**
- `algo-hr` — heart rate
- `algo-hrv` — heart rate variability
- `algo-afib-detection` — atrial fibrillation detection
- `algo-arrhythmia-classification` — multi-class arrhythmia
- `algo-pwv-bp-estimation` — pulse-wave-velocity blood pressure
- `algo-stress-index` — autonomic stress index

**Sleep**
- `algo-sleep-staging` — REM/NREM/wake staging
- `algo-sleep-apnea-detection` — apnea-hypopnea index from wearable
- `algo-snore-detection`

**Activity / motion**
- `algo-step-count`
- `algo-fall-detection`
- `algo-gait-analysis`
- `algo-activity-classification` — walking/running/cycling/etc.
- `algo-calorie-estimation`
- `algo-posture-detection`
- `algo-tremor-detection` — Parkinsonian / essential tremor
- `algo-bradykinesia-detection`

**Neural / cognitive**
- `algo-seizure-detection`
- `algo-cognitive-workload`
- `algo-drowsiness-detection`
- `algo-attention-state`
- `algo-bci-ssvep`
- `algo-bci-motor-imagery`
- `algo-bci-p300`
- `algo-erp-classification`

**Metabolic / chemical**
- `algo-glucose-noninvasive`
- `algo-glucose-cgm-readout`
- `algo-hydration-status`
- `algo-electrolyte-trend`

**Other**
- `algo-hand-gesture-emg`
- `algo-keystroke-emg`
- `algo-speech-bone-conduction`
- `algo-eye-gaze-tracking`
- `algo-pupillometry`
- `algo-emotion-recognition`
- `algo-spo2-estimation`
- `algo-respiratory-rate`
- `algo-cough-detection`
- `algo-uv-dose-tracking`
- `algo-thermoregulation-modeling`

## IP status definitions

- `patented` — known patents asserted, with patent numbers
- `open-permissive` — MIT, BSD, Apache, CERN-OHL-P, etc.
- `open-copyleft` — GPL, CERN-OHL-S, etc.
- `public-domain` — CC0 or equivalent dedication, or expired protection
- `fictional` — exists only in narrative; the engineering description is
  unencumbered as prior art
- `regulatory-filing` — disclosed via FDA / CE filing; the filed disclosure
  is public record
- `standards` — disclosed via standards body document; document is publicly
  citable
- `trade-secret` — claimed but not disclosed
- `unknown` — needs investigation

## Corpus buckets

- `private` — commercial products with disclosed engineering, including
  patent-thicket holders. Reference points for what's been claimed.
- `open` — open-hardware / open-source wearables. Already public-domain
  or permissive.
- `fictional` — film, TV, comics, games, literature. Cited successfully
  as 102 prior art when specific enough; cleanly serves 103
  motivation-to-combine for non-enabling disclosures.
- `academic` — peer-reviewed papers, theses, conference proceedings.
  Already prior art automatically by publication.
- `regulatory` — FDA 510(k) submissions, FDA De Novo / PMA decision
  summaries, CE MDR/IVDR technical documentation, predicate device
  chains. Public-record disclosures that examiners often miss.
- `standards` — IEEE 11073, Bluetooth SIG profiles (Heart Rate, CGMS,
  Pulse Oximeter, Continuous Glucose), Continua Alliance, ISO/IEC 80601
  series, AAMI/ANSI standards drafts. Disclose enabling implementations
  in normative annexes.

## Cross-cut generation

Each entry's tags drive cross-cut file generation. Three cross-cut
families:

1. **Single-axis cross-cuts** — one file per tag in
   `form_factor`/`form_factor_tags`, `sensors`, `algorithms`. The
   foundational view: every disclosure of `sensor-ppg` in chronological
   order, every disclosure of `watch` form factor in chronological
   order, etc.
2. **Form-factor × sensor intersections** — one file per
   (form-factor, sensor) pair that has ≥3 entries. E.g.,
   `watch__sensor-ppg.md`, `glasses__sensor-eeg.md`. These are the
   direct inputs to the obviousness template.
3. **Sensor × algorithm intersections** — one file per (sensor, algorithm)
   pair with ≥3 entries. E.g., `sensor-ppg__algo-hrv.md`,
   `sensor-eeg__algo-seizure-detection.md`.

Intersection cross-cuts are generated automatically; they are not
hand-curated. Single-axis cross-cuts may have hand-written narrative
preambles on the canonical ones.

## Storage format

- Master corpus: `corpus.jsonl` — one JSON object per line, append-only,
  git-tracked.
- Per-corpus mirrors: `private.jsonl`, `open.jsonl`, `fictional.jsonl`,
  `academic.jsonl`, `regulatory.jsonl`, `standards.jsonl`.
- Index: `CORPUS_INDEX.md` — generated, alphabetical by canonical_name.
- Lineage graph: `lineage.json` — derived, ancestor/descendant DAG.

## Versioning

Schema version increments on breaking changes. Entries carry
`schema_version` so older entries can be migrated. v0.1 is the starting
point and should be expected to evolve once seed slices expose
inadequacies.
