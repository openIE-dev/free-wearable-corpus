---
title: algo-seizure-detection
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-seizure-detection`

Axis: **algorithms**

**4 corpus entries disclose this tag.**

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

## FDA 510(k) K181861 (2018) — Empatica Embrace physiological-signal-based seizure monitoring system (2018)

- **id**: `fda-k181861-empatica-embrace-seizure-system-2018`
- **corpus**: regulatory
- **form factor**: watch
- **creator**: U.S. Food and Drug Administration (CDRH); submitter Empatica Inc.
- **disclosure**: U.S. FDA, 510(k) Premarket Notification K181861 (Empatica Inc., 'Embrace' physiological-signal-based seizure monitoring system) — a wrist-worn device using accelerometry plus electrodermal activity to detect probable generalized tonic-clonic seizures and alert caregivers; reported as the first FDA-cleared smartwatch indicated for use in neurology (clearance announced February 2018). (Verify which Embrace generation K181861 maps to; the original clearance may carry a different K-number.)
- **ip status**: regulatory-filing
- **sensors**: sensor-accelerometer, sensor-gsr
- **algorithms**: algo-seizure-detection
- **prior art notes**: A public, dated FDA record of a wrist-worn device detecting probable generalized tonic-clonic seizures from combined accelerometry and electrodermal activity, with caregiver alerting — the non-EEG route to wearable seizure detection. Establishes the public availability of that device as of 2018; the 510(k) cites a predicate chain that is itself prior art. Prior art for wrist-based seizure-detection claims using motion + EDA; regulatory anchor pairing with [[empatica-embrace2-seizure-watch-2018]] (the EEG route is anchored separately by [[zanetti-aminifar-atienza-eglass-2025]] and [[chb-mit-scalp-eeg-database-2009]]).

## Empatica Embrace2 (2018) — first FDA-cleared seizure-monitoring smartwatch (accelerometer + electrodermal activity) (2018-01-31)

- **id**: `empatica-embrace2-seizure-watch-2018`
- **corpus**: private
- **form factor**: watch
- **creator**: Empatica Inc. (Rosalind Picard, Matteo Lai, et al.)
- **disclosure**: Empatica Inc. 'Embrace2' smartwatch, FDA-cleared January 2018 — a wrist-worn device with a 3-axis accelerometer/gyroscope, an electrodermal-activity (EDA) sensor, and a peripheral skin-temperature sensor, running an on-device classifier that detects probable generalized tonic-clonic seizures from the combined motion + EDA signature and alerts caregivers; the first FDA-cleared smartwatch for seizure monitoring. (Descends from the MIT Media Lab 'iCalm'/'Q sensor' EDA wristband research, Picard et al.)
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-gsr, sensor-skin-temperature
- **algorithms**: algo-seizure-detection, algo-stress-index, algo-activity-classification
- **prior art notes**: Discloses a wristworn device that detects probable generalized tonic-clonic seizures by combining a motion (accelerometer/gyroscope) signature with an electrodermal-activity (sympathetic-surge) signature in an on-device classifier, and alerts caregivers — i.e. multimodal wrist-based seizure detection, distinct from the EEG-based approach. Anticipates wrist-seizure-detection claims combining 'a wrist-worn accelerometer and an electrodermal-activity sensor' and 'a classifier flagging a seizure from their combined signal' from 2018. Product-side anchor for the wrist × seizure-detection cross-cut; complementary to the EEG route in [[zanetti-aminifar-atienza-eglass-2025]] and [[chb-mit-scalp-eeg-database-2009]].

## e-Glass (Zanetti, Aminifar, Atienza; EPFL, 2025) — wearable EEG eyeglasses (2025-11-29)

- **id**: `zanetti-aminifar-atienza-eglass-2025`
- **corpus**: academic
- **form factor**: glasses
- **creator**: Renato Zanetti / Amir Aminifar / David Atienza (EPFL ESL)
- **disclosure**: Zanetti R, Aminifar A, Atienza D, et al. 'e-Glass: ...' (wearable EEG monitoring in an eyeglasses form factor with edge ML for seizure detection and cognitive-workload monitoring). Scientific Reports 2025. doi:10.1038/s41598-025-29893-4.
- **ip status**: unknown
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-seizure-detection, algo-cognitive-workload
- **prior art notes**: Discloses an eyeglasses-form-factor wearable EEG monitor with dry electrodes at the temples / around the ears (temporal/occipital pickup, validated against a reference montage at r≈0.93) and on-device machine learning for two applications — ambulatory seizure detection and cognitive-workload monitoring. Relevant to AR-glasses / smart-eyewear claims reciting 'EEG electrodes integrated into an eyeglasses frame' and 'an on-device classifier operating on the EEG'. Anchor for the glasses × EEG cross-cut. Bounds the application space: temple/around-ear contact supports seizure, drowsiness, attention, SSVEP — not frontal ERP or motor-imagery BCI.
