---
title: algo-bci-motor-imagery
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-bci-motor-imagery`

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

## Emotiv EPOC (2009) — 14-channel wireless saline-electrode consumer EEG headset (2009-12)

- **id**: `emotiv-epoc-2009`
- **corpus**: private
- **form factor**: headband
- **creator**: Emotiv Systems
- **disclosure**: Emotiv Systems. 'EPOC' EEG headset, released December 2009 — a 14-channel (plus 2 reference) wireless headset with saline-felt electrodes covering frontal/temporal/parietal/occipital sites, with SDKs for mental-command, facial-expression and 'affective' detections.
- **ip status**: patented
- **sensors**: sensor-saline-eeg-electrode, sensor-eeg
- **algorithms**: algo-cognitive-workload, algo-emotion-recognition, algo-bci-motor-imagery
- **prior art notes**: Discloses a wireless multi-channel (14+2) consumer EEG headset with saline-wetted contact electrodes at standard scalp sites and on-device/SDK classifiers for mental commands, facial expressions, and affective states. Anticipates multi-channel consumer-EEG-headset claims combining 'a wireless head-worn array of ≥8 contact electrodes', 'wet/saline electrode coupling', and 'classification of cognitive/affective state or intent' from 2009. Product-side anchor for the headband/cap × EEG cross-cut.

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
