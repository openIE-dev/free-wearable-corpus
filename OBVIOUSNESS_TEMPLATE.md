---
title: Obviousness Template
layout: default
nav_order: 5
---

# Obviousness Template — §103 Combination Argument for Wearable Claims

## What this is

Wearable patent claims overwhelmingly take the form:

> A [FORM FACTOR] comprising [SENSOR] and [PROCESSOR/MEMORY] configured
> to [ALGORITHM], wherein the device [OUTPUT].

These are claims of combination. Under KSR Int'l Co. v. Teleflex Inc., 550
U.S. 398 (2007) and MPEP § 2143, combining prior art elements according to
known methods to yield predictable results is per se obvious — no specific
motivation to combine need be shown when each element performs its
established function in the combination.

This document is the canonical 35 U.S.C. § 103 obviousness argument
applicable to any wearable claim of this form. Component disclosures live
in the corpus cross-cuts. The combination argument lives here, once, and
plugs in.

**The artifact is: cross-cuts + this template = the §103 proof.**

## How to use it

1. Read the asserted claim. Identify three (sometimes four) elements:
   - the form factor element (e.g., "a wristworn device")
   - the sensor element(s) (e.g., "a photoplethysmography sensor")
   - the algorithm / processor element (e.g., "configured to compute heart rate variability")
   - optionally an output element (e.g., "a display indicating ...")
2. Open the relevant cross-cut files:
   - `cross_cuts/<form-factor>.md` for the form factor element
   - `cross_cuts/<sensor-tag>.md` for the sensor element
   - `cross_cuts/<algorithm-tag>.md` for the algorithm element
   - If the intersection cross-cut exists (e.g.,
     `cross_cuts/watch__sensor-ppg.md`), it already lists every disclosure
     that combines the two elements — strong 102 / single-reference 103
     candidates.
3. Pick the earliest pre-priority-date disclosure from each cross-cut.
4. Fill in the template below. The boilerplate is doctrinally complete; only
   the cited entries change per claim.

## The template

> **Asserted Claim.** [QUOTE CLAIM AS ISSUED]
>
> **Effective filing date.** [DATE] (priority chain analyzed below if relevant).
>
> **Element-by-element prior art mapping.**
>
> *Element 1 — form factor: "[CLAIM PHRASE FOR FORM FACTOR]".*
>
> The [FORM FACTOR] form factor for body-worn sensing was publicly disclosed
> by [PRIOR ART ENTRY id], [YEAR], in [CITATION]. [ONE SENTENCE DESCRIBING
> WHAT THE PRIOR ART DISCLOSED]. Additional prior disclosures of the same
> form factor are catalogued in `cross_cuts/<form-factor>.md`, the earliest
> being [EARLIEST ENTRY], [YEAR].
>
> *Element 2 — sensor: "[CLAIM PHRASE FOR SENSOR]".*
>
> [SENSOR MODALITY] sensing in body-worn applications was publicly disclosed
> by [PRIOR ART ENTRY id], [YEAR], in [CITATION]. [ONE SENTENCE DESCRIBING
> SENSOR DISCLOSURE INCLUDING ANY GEOMETRY / WAVELENGTH / SAMPLING
> PARAMETERS RELEVANT TO CLAIM]. The full catalogue of body-worn [SENSOR
> MODALITY] disclosures appears at `cross_cuts/<sensor-tag>.md`, anchored
> at [EARLIEST ENTRY], [YEAR].
>
> *Element 3 — algorithm: "[CLAIM PHRASE FOR ALGORITHM]".*
>
> The [ALGORITHM] computation from [SENSOR MODALITY] signals was publicly
> disclosed by [PRIOR ART ENTRY id], [YEAR], in [CITATION]. [ONE SENTENCE
> DESCRIBING ALGORITHM DISCLOSURE INCLUDING SAMPLING / FEATURE EXTRACTION
> RELEVANT TO CLAIM]. See `cross_cuts/<algorithm-tag>.md` for additional
> disclosures.
>
> *Optional Element 4 — output: "[CLAIM PHRASE FOR OUTPUT]".*
>
> [OUTPUT MODALITY] in wearable contexts is disclosed by [PRIOR ART ENTRY],
> [YEAR], [CITATION].
>
> **Combination obviousness.**
>
> The claim combines three (or four) elements, each independently disclosed
> in the prior art before the effective filing date. Under MPEP § 2143
> Rationale A — "Combining prior art elements according to known methods to
> yield predictable results" — the combination is prima facie obvious where
> each element performs its established function in the combination. *KSR*
> requires no explicit teaching, suggestion, or motivation when prior art
> elements yield predictable results in known ways. *KSR*, 550 U.S. at 416
> ("the combination of familiar elements according to known methods is
> likely to be obvious when it does no more than yield predictable
> results").
>
> Here:
>
> 1. The [SENSOR MODALITY] sensor performs its established function —
>    transducing [PHYSIOLOGICAL SIGNAL] — exactly as disclosed in
>    [SENSOR PRIOR ART ENTRY].
> 2. The [FORM FACTOR] form factor performs its established function —
>    body-worn enclosure on the [ANATOMICAL SITE] — exactly as disclosed
>    in [FORM FACTOR PRIOR ART ENTRY].
> 3. The [ALGORITHM] computation performs its established function —
>    extracting [CLINICAL OUTPUT] from the sensor signal — exactly as
>    disclosed in [ALGORITHM PRIOR ART ENTRY].
>
> The combination yields the predictable result of body-worn [CLINICAL
> OUTPUT] sensing, with no new function emerging from the combination
> beyond the sum of the individual element functions. The claim is
> obvious under 35 U.S.C. § 103.
>
> **Secondary considerations.**
>
> No secondary considerations of nonobviousness (commercial success, long-felt
> need, unexpected results, copying, industry skepticism) reasonably attach
> to the bare element combination. Where applicant pleads commercial success,
> the commercial product practices many features beyond the claim; a nexus
> between the claim and the commercial success is not established by
> commercial success of the product alone. *Ormco Corp. v. Align Tech., Inc.*,
> 463 F.3d 1299, 1311–12 (Fed. Cir. 2006).
>
> **Reasonable expectation of success.**
>
> A POSITA practicing in wearable physiological monitoring as of the
> effective filing date would have had a reasonable expectation of success
> in combining these elements, as evidenced by the multiple prior
> implementations catalogued in the cited cross-cuts.

## Why this works as a template, not as bespoke per-combination work

The cross-cut model decouples component disclosure from combination
argument. Every (form factor × sensor) tuple in the wearable design space
maps onto:

1. The form-factor cross-cut (already enumerates every disclosure)
2. The sensor cross-cut (already enumerates every disclosure)
3. The intersection cross-cut where ≥3 entries exist (already enumerates
   every prior combination)
4. This template (already states the doctrinal argument)

For any new claim, the invalidity-contention author fills in entry ids and
ships. The corpus is not a database of pre-baked combinations; it is the
component substrate plus the combination argument.

## Important doctrinal limits

This template addresses **obviousness** under § 103. Some claim limitations
require **anticipation** under § 102 (single-reference disclosure of every
element). The cross-cut for the intersection (e.g., `watch__sensor-ppg.md`)
is where § 102 candidates live — if a single prior art entry discloses all
the claim elements, § 102 applies and § 103 is unnecessary.

Some claim limitations also require **enablement**. Fictional disclosures
are often non-enabling and therefore poor § 102 candidates. They remain
strong § 103 motivation-to-combine references for the broader concept,
under MPEP § 2141 (level of ordinary skill). Use academic, regulatory,
standards, or private/open prior art as the enabling reference; use
fictional prior art to establish motivation.

The Federal Circuit has held that prior art need not enable a *claimed*
invention, only the disclosed embodiment it teaches. *In re Antor Media
Corp.*, 689 F.3d 1282, 1287–88 (Fed. Cir. 2012).

## Quick-pick combination cells

The intersection cross-cuts below are the highest-traffic targets — the
combinations most often claimed in modern wearable patents. Each lists the
earliest anchor entry and the count of disclosures behind it.

(Generated alongside cross-cuts; see `cross_cuts/INDEX.md` for the full
table after the first seed pass.)

- `watch__sensor-ppg` — wristworn PPG (claimed in dozens of issued patents)
- `watch__sensor-ecg` — wristworn ECG
- `watch__sensor-accelerometer__algo-fall-detection`
- `watch__sensor-ppg__algo-afib-detection`
- `watch__sensor-ppg__algo-hrv`
- `watch__sensor-ppg__algo-sleep-staging`
- `bracelet__sensor-gsr__algo-stress-index`
- `bracelet__sensor-accelerometer__algo-step-count`
- `ring__sensor-ppg__algo-hrv`
- `ring__sensor-skin-temperature`
- `glasses__sensor-eeg`
- `glasses__sensor-camera-eye__algo-eye-gaze-tracking`
- `glasses__sensor-ppg`
- `headband__sensor-eeg__algo-sleep-staging`
- `patch__sensor-ecg`
- `patch__sensor-glucose-cgm`
- `patch__sensor-accelerometer__algo-fall-detection`
- `garment__sensor-ecg`
- `earbud__sensor-ppg`
- `earbud__sensor-eeg`

Each cell, once populated, is a drop-in §103 argument under this template.
