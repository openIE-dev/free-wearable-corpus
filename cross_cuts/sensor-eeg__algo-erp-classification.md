---
title: sensor-eeg ∩ algo-erp-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-eeg` ∩ `algo-erp-classification`

Axes: **sensors × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 2002-06

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Wolpaw et al. (2002) — 'Brain-computer interfaces for communication and control' (2002-06)

- **id**: `wolpaw-2002-bci-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jonathan R. Wolpaw et al.
- **disclosure**: Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM. 'Brain-computer interfaces for communication and control.' Clinical Neurophysiology 2002;113(6):767-791.
- **ip status**: public-domain
- **sensors**: sensor-eeg
- **algorithms**: algo-bci-p300, algo-bci-ssvep, algo-bci-motor-imagery, algo-erp-classification
- **prior art notes**: Canonical review establishing, as of 2002, the major non-invasive EEG-based BCI paradigms (sensorimotor rhythms / motor imagery, P300 evoked potentials, SSVEP, slow cortical potentials) and the signal-processing pipeline for translating EEG into control output. Prior art for wearable-BCI claims reciting any of these paradigms with scalp EEG: the paradigms and methods were published and enabled by 2002. Anchor for the BCI algorithm cross-cuts.

## Looney et al. (2012) — 'The in-the-ear recording concept' (ear-EEG) (2012-11)

- **id**: `looney-mandic-2012-in-ear-eeg`
- **corpus**: academic
- **form factor**: earbud
- **creator**: David Looney / Preben Kidmose / Danilo P. Mandic et al.
- **disclosure**: Looney D, Kidmose P, Park C, Ungstrup M, Rank ML, Rosenkranz K, Mandic DP. 'The in-the-ear recording concept: user-centered and wearable brain monitoring.' IEEE Pulse 2012;3(6):32-42. (See also Kidmose P, et al. 'A study of evoked potentials from ear-EEG.' IEEE Trans Biomed Eng 2013;60(10):2824-2830.)
- **ip status**: public-domain
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-drowsiness-detection, algo-sleep-staging, algo-bci-ssvep, algo-erp-classification
- **prior art notes**: Discloses recording EEG from electrodes placed inside the ear canal / concha of an individually-fitted earpiece — i.e. EEG in an earbud / hearing-aid form factor, demonstrated to capture alpha modulation, auditory steady-state and evoked responses. Any wearable claim reciting 'EEG electrodes disposed on an in-ear earpiece to measure an electroencephalographic signal of the wearer' reads on Looney et al. 2012. Anchor for the earbud/hearing-aid × EEG cross-cut; complementary to [[debener-2015-ceegrid-around-ear-eeg]] and [[zanetti-aminifar-atienza-eglass-2025]] (around-ear / temporal pickup).

## Debener et al. (2015) — cEEGrid: unobtrusive around-the-ear EEG with flexible printed electrodes (2015-11-17)

- **id**: `debener-2015-ceegrid-around-ear-eeg`
- **corpus**: academic
- **form factor**: patch
- **creator**: Stefan Debener / Martin G. Bleichner et al. (Oldenburg)
- **disclosure**: Debener S, Emkes R, De Vos M, Bleichner MG. 'Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear.' Scientific Reports 2015;5:16743.
- **ip status**: public-domain
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-erp-classification, algo-sleep-staging, algo-drowsiness-detection
- **prior art notes**: Discloses a flexible, printed, C-shaped electrode array worn around the ear (behind and below the auricle) for unobtrusive ambulatory EEG, recorded to a smartphone-class device. Any wearable claim reciting 'an array of EEG electrodes arranged around/behind the ear of the wearer' (the geometry used by EEG glasses, EEG earbuds, and EEG behind-the-ear stickers) reads on Debener et al. 2015. Directly relevant prior art for [[zanetti-aminifar-atienza-eglass-2025]] (which uses temporal/around-ear pickup) and for around-ear-EEG hearable claims; anchor for that cross-cut.
