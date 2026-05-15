---
title: sensor-eeg ∩ algo-sleep-staging
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-eeg` ∩ `algo-sleep-staging`

Axes: **sensors × algorithms**

**5 corpus entries disclose both tags.**

Earliest disclosure: 1953-09-04

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Aserinsky & Kleitman (1953) — discovery of REM sleep via electrooculography (1953-09-04)

- **id**: `aserinsky-kleitman-1953-rem-sleep`
- **corpus**: academic
- **form factor**: other
- **creator**: Eugene Aserinsky / Nathaniel Kleitman (University of Chicago)
- **disclosure**: Aserinsky E, Kleitman N. 'Regularly occurring periods of eye motility, and concomitant phenomena, during sleep.' Science 1953;118(3062):273-274.
- **ip status**: public-domain
- **sensors**: sensor-eog, sensor-eeg
- **algorithms**: algo-sleep-staging
- **prior art notes**: Establishes that sleep is not homogeneous — that there are recurring periods of rapid eye movement detectable by electrooculography (with concomitant EEG changes) — i.e. the existence of distinguishable sleep states detectable from ocular/cortical electrophysiology. Foundational prior art for any sleep-staging wearable: the premise that sleep states are detectable from EOG/EEG signals is public since 1953. Anchor for the sleep-staging cross-cut.

## Rechtschaffen & Kales (1968) — standardized sleep-stage scoring manual (1968)

- **id**: `rechtschaffen-kales-1968-sleep-scoring-manual`
- **corpus**: standards
- **form factor**: other
- **creator**: Allan Rechtschaffen / Anthony Kales (eds), for the UCLA Brain Information Service
- **disclosure**: Rechtschaffen A, Kales A (eds). 'A Manual of Standardized Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects.' Public Health Service / U.S. Government Printing Office / UCLA Brain Information Service, NIH Publication No. 204, 1968.
- **ip status**: standards
- **sensors**: sensor-eeg, sensor-eog, sensor-emg
- **algorithms**: algo-sleep-staging
- **prior art notes**: Standardizes the definition of sleep stages and the rules for scoring them from EEG + EOG + EMG (polysomnography). Any wearable claim reciting 'classifying sleep into stages from electrophysiological/physiological signals' rests on the staging framework standardized here. Combined with [[muse-headband-2014]]-type form-factor disclosures, makes wearable automated sleep-staging an obvious combination under [[obviousness-template]].

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

## Muse headband (InteraXon, 2014) — multi-channel dry-electrode EEG headband for meditation and sleep (2014-05)

- **id**: `muse-headband-2014`
- **corpus**: private
- **form factor**: headband
- **creator**: InteraXon Inc.
- **disclosure**: InteraXon Inc. 'Muse' brain-sensing headband, shipped 2014 — a forehead-band EEG device with frontal (AF7/AF8/Fp1/Fp2-region) and behind-the-ear (TP9/TP10) dry/conductive-rubber electrodes, giving real-time neurofeedback for meditation (and, in 'Muse S', sleep tracking).
- **ip status**: patented
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-attention-state, algo-cognitive-workload, algo-sleep-staging
- **prior art notes**: Discloses a forehead-band wearable EEG device with frontal and behind-the-ear (TP9/TP10) dry electrodes providing real-time neurofeedback for meditation training and (later) sleep staging. Anticipates EEG-headband claims combining 'a forehead band', 'frontal and mastoid/behind-ear dry electrodes', and 'real-time feedback on a meditation or sleep state' from 2014. Note: its TP9/TP10 around-ear pickup is the same general region used by [[zanetti-aminifar-atienza-eglass-2025]] — relevant prior art for around-ear-EEG wearable claims. Product-side anchor for the headband × EEG cross-cut.

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
