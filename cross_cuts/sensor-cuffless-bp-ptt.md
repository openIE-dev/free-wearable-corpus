---
title: sensor-cuffless-bp-ptt
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-cuffless-bp-ptt`

Axis: **sensors**

**4 corpus entries disclose this tag.**

Earliest disclosure: 1981-01

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Geddes et al. (1981) — pulse transit time as an indicator of arterial blood pressure (1981-01)

- **id**: `geddes-1981-pulse-transit-time-bp`
- **corpus**: academic
- **form factor**: other
- **creator**: Leslie A. Geddes et al. (Purdue)
- **disclosure**: Geddes LA, Voelz MH, Babbs CF, Bourland JD, Tacker WA. 'Pulse transit time as an indicator of arterial blood pressure.' Psychophysiology 1981;18(1):71-74.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Establishes that pulse transit time — the delay between a proximal timing reference (e.g. the ECG R-wave) and the arrival of the pulse at a distal site (e.g. a finger PPG) — varies inversely with arterial blood pressure, and can therefore be used to estimate BP without a cuff. Any cuffless-BP wearable claim reciting 'estimating blood pressure from a pulse transit time (or pulse arrival time / pulse wave velocity) derived from two physiological signals' reads on Geddes 1981. Earliest anchor for the PTT-cuffless-BP cross-cut; [[mukkamala-2015-ptt-cuffless-bp-review]] is the modern survey.

## Mukkamala et al. (2015) — 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice' (2015-08)

- **id**: `mukkamala-2015-ptt-cuffless-bp-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Ramakrishna Mukkamala et al.
- **disclosure**: Mukkamala R, Hahn J-O, Inan OT, Mestha LK, Kim C-S, Töreyin H, Kyal S. 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice.' IEEE Transactions on Biomedical Engineering 2015;62(8):1879-1901.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt, sensor-cuffless-bp-tonometry
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Canonical 2015 review of cuffless blood-pressure estimation by pulse transit time / pulse arrival time / pulse wave velocity: the physiological models, the practical sensor configurations (ECG+PPG, dual PPG, ballistocardiogram+PPG), the calibration strategies, and the accuracy limitations. Prior art for cuffless-BP wearable claims reciting any of the configurations or calibration approaches surveyed here — they were collected, modeled, and published by 2015. Combined with watch/ring/patch form-factor disclosures, makes wearable PTT-based BP an obvious combination under [[obviousness-template]].

## Samsung Galaxy Watch3 / Samsung Health Monitor (2020) — wrist single-lead ECG and optical-PPG cuffless blood pressure (2020-08)

- **id**: `samsung-galaxy-watch-bp-ecg-2020`
- **corpus**: private
- **form factor**: watch
- **creator**: Samsung Electronics Co., Ltd.
- **disclosure**: Samsung Electronics. 'Samsung Health Monitor' app on Galaxy Watch3 / Watch Active2, 2020 — wrist single-lead ECG (between a back-crystal electrode and a side-button electrode touched by the opposite hand, with AF/sinus classification) and a cuffless blood-pressure feature using the optical (PPG) pulse-wave signal calibrated against a periodic conventional cuff reading. (Cleared in Korea 2020; subsequently in other markets.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt
- **algorithms**: algo-afib-detection, algo-arrhythmia-classification, algo-pwv-bp-estimation, algo-hr
- **prior art notes**: Discloses a wristworn device that takes a single-lead ECG with on-device AF classification and, separately, estimates blood pressure from the wrist optical-PPG pulse waveform after calibration against a periodic conventional cuff measurement (a calibrated-cuffless approach). Anticipates wrist-cuffless-BP claims reciting 'estimating blood pressure from a wrist photoplethysmography signal calibrated by a reference cuff reading' from 2020 — the underlying PTT/PWV-BP technique is much older ([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the watch × cuffless-BP cross-cut.

## Aktiia bracelet (2021) — optical-PPG-based continuous cuffless blood-pressure monitoring bracelet (2021-01)

- **id**: `aktiia-bracelet-cuffless-bp-2021`
- **corpus**: private
- **form factor**: bracelet
- **creator**: Aktiia SA
- **disclosure**: Aktiia SA. 'Aktiia bracelet' (later 'Hilo'), CE-marked and launched in Europe January 2021 — a slim wristband with optical photoplethysmography that, after a one-time initialization against a conventional cuff (and periodic re-calibration), estimates systolic and diastolic blood pressure several times a day automatically, day and night, from the wrist PPG pulse waveform.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-cuffless-bp-ptt, sensor-accelerometer
- **algorithms**: algo-pwv-bp-estimation, algo-hr
- **prior art notes**: Discloses a slim wristband that, after a one-time cuff initialization (and periodic re-calibration), automatically estimates systolic and diastolic blood pressure multiple times per day and night purely from the wrist optical-PPG pulse waveform — i.e. continuous, fully cuffless, calibration-initialized wrist BP monitoring. Anticipates continuous-cuffless-wrist-BP claims from 2021; the PPG-pulse-feature-to-BP mapping rests on the much older PTT/PWV-BP and pulse-contour literature ([[geddes-1981-pulse-transit-time-bp]], [[mukkamala-2015-ptt-cuffless-bp-review]]). Product-side anchor for the bracelet × cuffless-BP cross-cut.
