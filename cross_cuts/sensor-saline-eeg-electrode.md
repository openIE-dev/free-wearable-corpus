---
title: sensor-saline-eeg-electrode
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-saline-eeg-electrode`

Axis: **sensors**

**3 corpus entries disclose this tag.**

Earliest disclosure: 2009-08

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## CHB-MIT Scalp EEG Database (Shoeb, 2009) — benchmark seizure-detection dataset (2009-08)

- **id**: `chb-mit-scalp-eeg-database-2009`
- **corpus**: academic
- **form factor**: other
- **creator**: Ali H. Shoeb (MIT / Boston Children's Hospital)
- **disclosure**: Shoeb AH. 'Application of Machine Learning to Epileptic Seizure Onset Detection and Treatment.' PhD thesis, MIT, 2009 (the CHB-MIT Scalp EEG Database, distributed via PhysioNet, physionet.org/content/chbmit).
- **ip status**: public-domain
- **sensors**: sensor-eeg, sensor-saline-eeg-electrode
- **algorithms**: algo-seizure-detection
- **prior art notes**: Publishes a labelled scalp-EEG corpus and a machine-learning method for patient-specific seizure-onset detection, establishing the public benchmark and the patient-calibrated detection paradigm used by subsequent wearable seizure detectors. Relevant to seizure-detection-wearable claims reciting 'a classifier trained on EEG to detect seizure onset', particularly 'patient-specific' or 'per-subject calibrated' variants — the paradigm and a reference implementation were public by 2009. Anchor for the EEG × seizure-detection cross-cut; [[zanetti-aminifar-atienza-eglass-2025]] reports against it.

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
