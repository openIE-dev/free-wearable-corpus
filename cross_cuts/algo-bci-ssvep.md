---
title: algo-bci-ssvep
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-bci-ssvep`

Axis: **algorithms**

**3 corpus entries disclose this tag.**

Earliest disclosure: 2002-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

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

## OpenBCI Cyton — open-source 8-channel biosignal (EEG/EMG/ECG) acquisition board and 3D-printed headset (2014-01-22)

- **id**: `openbci-cyton-2014`
- **corpus**: open
- **form factor**: cap
- **creator**: Joel Murphy / Conor Russomanno (OpenBCI)
- **disclosure**: OpenBCI (Joel Murphy, Conor Russomanno). 'OpenBCI: An Open Source Brain-Computer Interface For Makers.' Kickstarter campaign launched 22 January 2014; hardware designs and firmware released open source at github.com/OpenBCI (Cyton board, Ganglion board, Ultracortex Mark IV 3D-printed headset).
- **ip status**: open-permissive
- **sensors**: sensor-saline-eeg-electrode, sensor-dry-eeg-electrode, sensor-emg, sensor-ecg
- **algorithms**: algo-bci-p300, algo-bci-ssvep, algo-bci-motor-imagery
- **prior art notes**: An openly-published, openly-licensed wearable biosignal acquisition system: a multi-channel ADS1299-based board, electrodes, and a 3D-printed head-worn frame for EEG/EMG/ECG, with reference firmware and BCI demonstrations. As open-hardware prior art it is unencumbered: any claim reciting a multi-channel head-worn biopotential acquisition device with the features published here (since 2014) reads on OpenBCI. Anchors the `open` bucket for biosignal wearables; relevant to headband/cap EEG and to EMG/ECG wearable claims.
