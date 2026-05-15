---
title: bracelet ∩ algo-activity-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `bracelet` ∩ `algo-activity-classification`

Axes: **form_factor × algorithms**

**7 corpus entries disclose both tags.**

Earliest disclosure: 1992

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Cole & Kripke et al. (1992) — automatic sleep/wake identification from wrist activity (the Cole-Kripke algorithm) (1992)

- **id**: `cole-kripke-1992-wrist-actigraphy-sleep`
- **corpus**: academic
- **form factor**: watch
- **creator**: Roger J. Cole / Daniel F. Kripke et al.
- **disclosure**: Cole RJ, Kripke DF, Gruen W, Mullaney DJ, Gillin JC. 'Automatic sleep/wake identification from wrist activity.' Sleep 1992;15(5):461-469.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer
- **algorithms**: algo-sleep-staging, algo-activity-classification
- **prior art notes**: Discloses an algorithm that classifies each epoch as sleep or wake from a wrist-worn activity (accelerometer) recording, validated against polysomnography — i.e. wrist actigraphy as a wearable sleep monitor. Any consumer-wearable claim reciting 'estimating sleep/wake state from a wrist-worn accelerometer signal' (the method underlying Fitbit/Jawbone-class sleep tracking) reads on Cole-Kripke 1992. Anchor for the accelerometry sleep-staging cross-cut; combined with the wrist form factor it makes wristworn sleep tracking obvious under [[obviousness-template]].

## Sadeh et al. (1994) — activity-based sleep-wake identification (the Sadeh algorithm) (1994)

- **id**: `sadeh-1994-actigraphy-sleep-wake-algorithm`
- **corpus**: academic
- **form factor**: watch
- **creator**: Avi Sadeh / Katherine M. Sharkey / Mary A. Carskadon
- **disclosure**: Sadeh A, Sharkey KM, Carskadon MA. 'Activity-based sleep-wake identification: an empirical test of methodological issues.' Sleep 1994;17(3):201-207.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer
- **algorithms**: algo-sleep-staging, algo-activity-classification
- **prior art notes**: A second widely-used wrist-actigraphy sleep/wake scoring algorithm, with explicit treatment of the methodological choices (epoch length, scoring window, scaling). Prior art alongside [[cole-kripke-1992-wrist-actigraphy-sleep]] for any wearable claim reciting an actigraphy-based sleep-detection method or its parameters; both were published and validated by 1994.

## Fitbit Tracker (2009) — clip-on accelerometer activity and sleep monitor (2009-10)

- **id**: `fitbit-tracker-2009`
- **corpus**: private
- **form factor**: pendant
- **creator**: Fitbit, Inc. (James Park, Eric Friedman)
- **disclosure**: Fitbit, Inc. 'Fitbit Tracker', launched October 2009 — a clip-worn device with a 3-axis accelerometer estimating steps, distance, calories burned, active minutes, and sleep quality, syncing wirelessly to a web dashboard. (The wrist PPG heart-rate variant, Fitbit Charge HR, followed in January 2015.)
- **ip status**: patented
- **sensors**: sensor-accelerometer
- **algorithms**: algo-step-count, algo-calorie-estimation, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a small body-worn (clip) device with a 3-axis accelerometer that estimates step count, distance, calories, active minutes, and sleep quality on-device and syncs wirelessly to a cloud dashboard. Anticipates consumer-activity-tracker claims combining 'a body-worn accelerometer', 'on-device estimation of steps/calories/activity/sleep', and 'wireless sync to a remote service' from 2009. Anchor for the step-count and consumer-sleep-tracking cross-cuts on the product side.

## Pantelopoulos & Bourbakis (2010) — survey on wearable sensor-based systems for health monitoring and prognosis (2010-01)

- **id**: `pantelopoulos-bourbakis-2010-wearable-health-survey`
- **corpus**: academic
- **form factor**: other
- **creator**: Alexandros Pantelopoulos / Nikolaos G. Bourbakis
- **disclosure**: Pantelopoulos A, Bourbakis NG. 'A survey on wearable sensor-based systems for health monitoring and prognosis.' IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 2010;40(1):1-12.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-skin-temperature, sensor-respiration-impedance
- **algorithms**: algo-hr, algo-arrhythmia-classification, algo-spo2-estimation, algo-fall-detection, algo-activity-classification
- **prior art notes**: Surveys, as of 2010, the architecture and components of wearable health-monitoring systems — sensors (ECG, PPG, SpO2, accelerometry, temperature, respiration), garment- and patch- and watch-based form factors, on-body processing, wireless body-area networking, and the analytics (arrhythmia, fall, activity, deterioration prediction). Prior art establishing that the general 'multi-sensor wearable + body-area network + cloud analytics' system architecture and its building blocks were collected and published by 2010 — useful against later claims to the bare system architecture. General anchor.

## WHOOP Strap (2015) — display-less wrist/bicep PPG band for continuous HR/HRV, sleep and recovery (2015)

- **id**: `whoop-strap-2015`
- **corpus**: private
- **form factor**: bracelet
- **creator**: WHOOP, Inc. (Will Ahmed)
- **disclosure**: WHOOP, Inc. 'WHOOP Strap', launched 2015 — a screenless band worn on the wrist or upper arm with photoplethysmography, a 3-axis accelerometer, and skin-temperature sensing, providing continuous heart rate, heart-rate variability, respiratory rate, sleep staging, and a derived 'recovery' score, with no on-device display.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging, algo-activity-classification
- **prior art notes**: Discloses a display-less band worn on the wrist or upper arm with PPG, accelerometry, and skin-temperature sensing that continuously derives HR, HRV, respiratory rate, and sleep stages and combines them into a daily 'recovery' index, with no screen (companion-app readout). Anticipates screenless-band claims and PPG-derived-HRV/recovery-score claims from 2015. Product-side anchor for the bracelet × PPG cross-cut and the HRV cross-cut.

## Fitbit Charge HR (2015) — wristband with continuous wrist-PPG heart rate ('PurePulse') (2015-01-06)

- **id**: `fitbit-charge-hr-2015`
- **corpus**: private
- **form factor**: watch
- **creator**: Fitbit, Inc.
- **disclosure**: Fitbit, Inc. 'Fitbit Charge HR', announced January 2015 — a wristband with 'PurePulse' continuous optical (green-LED PPG) heart rate, a 3-axis accelerometer, steps/distance/floors/calories/active-minutes, automatic sleep tracking, and call/text notifications.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-barometer
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a wristband with continuous green-LED reflectance-PPG heart rate plus accelerometry and an altimeter, deriving HR, steps, floors, calories, and sleep, with phone notifications. A mainstream realization of [[mendelson-ochs-1988-reflectance-pulse-oximetry]]-geometry wrist PPG; anticipates wrist-PPG-HR-band claims from January 2015. Product-side anchor for the watch × PPG cross-cut alongside [[apple-watch-original-2015]].

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
