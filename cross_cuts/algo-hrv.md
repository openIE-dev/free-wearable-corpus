---
title: algo-hrv
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-hrv`

Axis: **algorithms**

**13 corpus entries disclose this tag.**

Earliest disclosure: 1996-03

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Task Force of the ESC and NASPE (1996) — heart rate variability: standards of measurement (1996-03)

- **id**: `esc-naspe-1996-hrv-standards`
- **corpus**: standards
- **form factor**: other
- **creator**: Task Force of the ESC and NASPE
- **disclosure**: Task Force of the European Society of Cardiology and the North American Society of Pacing and Electrophysiology. 'Heart rate variability: standards of measurement, physiological interpretation, and clinical use.' Circulation 1996;93(5):1043-1065 (also European Heart Journal 1996;17:354-381).
- **ip status**: standards
- **sensors**: sensor-ecg, sensor-ppg
- **algorithms**: algo-hrv, algo-stress-index
- **prior art notes**: Standardizes the time-domain (SDNN, RMSSD, pNN50, ...) and frequency-domain (VLF/LF/HF, LF/HF ratio) measures of heart rate variability, their computation from an interbeat-interval series, and their physiological interpretation. Any wearable claim reciting 'computing a heart-rate-variability metric (e.g. RMSSD, LF/HF) from a sequence of interbeat intervals' rests on metrics standardized here. Anchor for the HRV cross-cut; applicable whether the interbeat intervals come from ECG or PPG.

## Allen (2007) — 'Photoplethysmography and its application in clinical physiological measurement' (2007-02-20)

- **id**: `allen-2007-ppg-review`
- **corpus**: academic
- **form factor**: other
- **creator**: John Allen (Freeman Hospital / Newcastle)
- **disclosure**: Allen J. 'Photoplethysmography and its application in clinical physiological measurement.' Physiological Measurement 2007;28(3):R1-R39. doi:10.1088/0967-3334/28/3/R01.
- **ip status**: public-domain
- **sensors**: sensor-ppg
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-spo2-estimation, algo-pwv-bp-estimation
- **prior art notes**: Canonical review collecting the state of PPG measurement and the physiological parameters derivable from a PPG signal as of 2007 — heart rate, HRV, respiratory rate, SpO2, blood-pressure surrogates, arterial-stiffness/aging indices, vasomotor assessment. Relevant to wearable claims that recite 'deriving [parameter X] from a photoplethysmography signal' for any X covered here: the derivation was a published, enabled technique by 2007, defeating novelty of the bare derivation and supplying § 103 motivation for the form-factor+PPG+algorithm combinations. The single most-cited anchor for PPG-derived-metric wearable patents.

## Hexoskin smart shirt (2014) — textile-integrated ECG, respiration and activity garment (2013)

- **id**: `hexoskin-smart-shirt-2014`
- **corpus**: private
- **form factor**: garment
- **creator**: Carre Technologies Inc.
- **disclosure**: Carre Technologies Inc. (Hexoskin). 'Hexoskin Smart Shirt', introduced 2013 (consumer); a compression shirt with knitted dry textile electrodes for single-lead ECG, two-channel respiratory inductive plethysmography (thoracic + abdominal expansion), a 3-axis accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate/volume, cadence, steps, and sleep. (Used in NASA/CSA 'Astroskin' studies.)
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-sleep-staging
- **prior art notes**: Discloses a consumer/research compression shirt with textile-integrated dry ECG electrodes, two-channel respiratory inductive plethysmography (thoracic + abdominal), an accelerometer, and a removable electronics pod, deriving HR, HRV, breathing rate and volume, activity, and sleep. A commercial realization of [[paradiso-2005-wealthy-knitted-smart-shirt]]; anticipates smart-shirt claims combining 'textile-integrated ECG and respiration sensors' and 'a detachable electronics module' from 2013. Product-side anchor for the garment × textile-electrode cross-cut.

## Inan et al. (2015) — ballistocardiography and seismocardiography review (2014-10-07)

- **id**: `inan-2015-bcg-scg-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Omer T. Inan et al.
- **disclosure**: Inan OT, Migeotte P-F, Park K-S, Etemadi M, Tavakolian K, Casanella R, Zanetti J, Tank J, Funtova I, Prisk GK, Di Rienzo M. 'Ballistocardiography and seismocardiography: a review of recent advances.' IEEE Journal of Biomedical and Health Informatics 2015;19(4):1414-1427.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer, sensor-piezoelectric
- **algorithms**: algo-hr, algo-hrv, algo-pwv-bp-estimation
- **prior art notes**: Reviews ballistocardiography (whole-body reaction force from cardiac ejection, measured at the seat/scale/bed) and seismocardiography (local chest vibration from cardiac motion, measured by accelerometers on the sternum) and their integration into bathroom scales, weighing chairs, beds, and chest patches — i.e. the mechanical-cardiac-signal route to heart rate, HRV, and cardiac-timing-interval / stroke-volume estimation. Prior art for claims reciting 'measuring cardiac activity from a body-worn or support-mounted accelerometer/force sensor', as both the BCG and SCG approaches and their wearable instantiations were collected and reviewed by 2015. Anchor for the BCG/SCG cross-cut.

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

## Oura Ring (Gen 1, 2015) — finger-ring PPG, skin-temperature and accelerometer for HRV, sleep and body temperature (2015-08)

- **id**: `oura-ring-gen1-2015`
- **corpus**: private
- **form factor**: ring
- **creator**: Oura Health Oy
- **disclosure**: Oura Health Oy. 'Oura Ring' (1st generation), crowdfunded 2015, shipped 2016 — a titanium finger ring with infrared photoplethysmography, an NTC skin-temperature sensor, and a 3-axis accelerometer, deriving resting heart rate, heart-rate variability, respiratory rate, sleep staging, and body-temperature trend.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging
- **prior art notes**: Discloses a finger-ring wearable with infrared PPG, a skin-temperature sensor, and an accelerometer, deriving resting HR, HRV, respiratory rate, sleep stages, and a body-temperature trend, with companion-app readout. A commercial realization, ~12-16 years later, of the MIT ring-sensor concept ([[asada-mit-wearable-ring-sensor-2003]]); to the extent later claims recite ring-form PPG + skin-temperature + HRV/sleep, both Asada 2003 and Oura 2015 are prior art. Product-side anchor for the ring × PPG × HRV and ring × skin-temperature cross-cuts.

## VitalConnect VitalPatch (2016) — adhesive chest patch with single-lead ECG and multi-parameter monitoring (2016)

- **id**: `vitalconnect-vitalpatch-2016`
- **corpus**: private
- **form factor**: patch
- **creator**: VitalConnect, Inc.
- **disclosure**: VitalConnect, Inc. 'VitalPatch' biosensor, FDA-cleared as a single-use adhesive chest patch with single-lead ECG, heart rate, heart-rate variability, respiratory rate, skin temperature, posture, activity, and fall detection, streamed wirelessly to a smartphone/relay; 7-day wear (later 14-day variants).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-arrhythmia-classification
- **prior art notes**: Discloses a single-use adhesive chest patch deriving single-lead ECG, HR, HRV, respiratory rate, skin temperature, posture, activity, and falls in one body-worn unit, streamed wirelessly — i.e. a packed multi-parameter vital-signs patch. Anticipates multi-parameter ECG-patch claims combining any subset of those measurements in one adhesive form factor from 2016. Product-side anchor for the patch × multi-parameter-vitals cross-cut alongside [[fda-k113862-irhythm-zio-patch-2011]] (the AFib-focused variant).

## Polar H10 (2017) — research-grade chest-strap ECG heart-rate sensor (2017-01)

- **id**: `polar-h10-chest-strap-2017`
- **corpus**: private
- **form factor**: garment
- **creator**: Polar Electro Oy
- **disclosure**: Polar Electro Oy. 'Polar H10' chest heart-rate sensor, released 2017 — a chest strap with two dry electrodes deriving a single-lead ECG, computing R-R intervals and heart rate, with onboard 1-session memory, dual-broadcast (BLE + ANT+ + 5 kHz GymLink), an accelerometer (relative orientation), and well-documented R-R-interval accuracy (often used as a gold-standard reference for consumer wearables).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-arrhythmia-classification
- **prior art notes**: Discloses a chest strap with two dry electrodes deriving single-lead ECG, with on-strap R-R-interval computation, multi-protocol broadcast (BLE + ANT+ + the 5 kHz GymLink legacy band), and accelerometer-assisted noise rejection. Anticipates chest-strap-ECG claims combining 'dry textile/elastic chest electrodes', 'on-strap derivation of R-R intervals and HR', and 'multi-protocol simultaneous wireless broadcast' from 2017. Product-side anchor for the garment/patch × ECG strap cross-cut; refines [[polar-sport-tester-pe2000-1982]].

## Masimo W1 (2022) — first FDA-cleared continuous wrist medical-grade pulse oximetry watch (2022-05)

- **id**: `masimo-w1-2022`
- **corpus**: private
- **form factor**: watch
- **creator**: Masimo Corp.
- **disclosure**: Masimo Corp. 'Masimo W1' health-tracking watch, announced May 2022 — a wrist-worn device performing continuous medical-grade pulse oximetry (SpO2), pulse rate, perfusion index (PI), pleth variability index (PVi), respiratory rate from the PPG, and HRV, using Masimo's SET/rainbow signal-extraction algorithms. (FDA cleared as a continuous-monitoring medical device.)
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg, sensor-accelerometer
- **algorithms**: algo-spo2-estimation, algo-hr, algo-hrv, algo-respiratory-rate
- **prior art notes**: Discloses a wrist-worn device performing continuous medical-grade pulse oximetry — SpO2, PR, perfusion index, PVi, RR-from-PPG, HRV — using established signal-extraction methods, distinguished from consumer spot-check SpO2 by continuous operation and clearance for medical use. Anticipates wrist-continuous-medical-SpO2 claims from 2022; the underlying two-wavelength SpO2 method is much older ([[aoyagi-1974-two-wavelength-pulse-oximetry]], [[mendelson-ochs-1988-reflectance-pulse-oximetry]], [[iso-80601-2-61-pulse-oximeter-equipment-2011]]). Product-side anchor for the watch × continuous-SpO2 cross-cut.

## Ultrahuman Ring AIR (2023) — smart ring with metabolic-focus tracking (PPG, skin temperature, IMU) (2023)

- **id**: `ultrahuman-ring-air-2023`
- **corpus**: private
- **form factor**: ring
- **creator**: Ultrahuman Healthcare Pvt. Ltd.
- **disclosure**: Ultrahuman Healthcare Pvt. Ltd. 'Ultrahuman Ring AIR', launched 2023 — a titanium smart ring with infrared photoplethysmography, IR skin-temperature, and a 6-axis IMU, deriving HR, HRV, skin temperature, sleep staging, activity, and metabolic-health framing (paired with the company's CGM-based metabolism platform).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-hrv, algo-sleep-staging, algo-respiratory-rate
- **prior art notes**: Discloses a smart ring with IR PPG, skin-temperature, and a 6-axis IMU, deriving HR/HRV, sleep, and activity, packaged with a metabolic-health platform (CGM-linked). Product-side reference in the ring × PPG cross-cut alongside [[oura-ring-gen1-2015]] and [[samsung-galaxy-ring-2024]].

## HealthyPi Move (ProtoCentral, 2026) — open-source medical-grade smartwatch (2024)

- **id**: `healthypi-move-2026`
- **corpus**: open
- **form factor**: watch
- **creator**: ProtoCentral Electronics
- **disclosure**: ProtoCentral Electronics (Bengaluru, India). 'HealthyPi Move' fully open-source AMOLED smartwatch — Crowd Supply campaign launched 2024, units shipping 15 May 2026. Sensors: single-lead ECG, dual-site PPG (wrist + finger), SpO2, blood-pressure trending, EDA/GSR, heart rate, HRV, respiration rate (derived), body temperature, 6-axis IMU. Compute: Nordic nRF5340 (dual ARM Cortex-M33). Display: AMOLED, 300 mAh battery. Companion app: Flutter, runs on Android/iOS/macOS/Windows/Linux, all data stored locally. Hardware design, firmware (Zephyr RTOS on nRF Connect SDK), and companion app all open-source. https://www.crowdsupply.com/protocentral/healthypi-move
- **ip status**: open-permissive
- **sensors**: sensor-ecg, sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg, sensor-gsr, sensor-accelerometer, sensor-gyroscope, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-spo2-estimation, algo-respiratory-rate, algo-pwv-bp-estimation, algo-sleep-staging, algo-activity-classification, algo-step-count
- **prior art notes**: Discloses, as fully open-source hardware and firmware (CC and MIT-style licensing across components), a wrist-worn smartwatch with the full consumer-medical sensor stack: single-lead ECG between back-of-watch electrode and a finger-touch electrode; multi-wavelength reflectance PPG with SpO2 and BP-trending; EDA/GSR; skin temperature; 6-axis IMU; on-device Zephyr-RTOS application; AMOLED display; all-local data storage via cross-platform Flutter app. Anticipates wrist-multi-sensor-watch claims from 2024-2026 to the extent they recite combinations of these elements; as `open` prior art it is unencumbered and any patent claim reciting these combinations must distinguish over HealthyPi Move's specific implementation. The product-side anchor for the 'open watch with the full sensor stack' cross-cut.

## CogWatch (HardwareX, 2024) — open-source smartwatch for cognitive-load monitoring (2024)

- **id**: `cogwatch-2024-hardwarex`
- **corpus**: academic
- **form factor**: watch
- **creator**: (See HardwareX publication for full author list.)
- **disclosure**: 'CogWatch: An open-source smartwatch platform for cognitive-load monitoring.' HardwareX 19 (2024). Open-source smartwatch design — full hardware, firmware, and assembly documentation published in the open-hardware-focused journal HardwareX (Elsevier). https://www.hardware-x.com/article/S2468-0672(24)00032-4/fulltext
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-gsr, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-stress-index, algo-cognitive-workload
- **prior art notes**: Discloses, as open-hardware (HardwareX is the canonical venue for full publication of open-hardware designs), a wrist-worn smartwatch instrumented for cognitive-load monitoring from PPG-derived HRV and EDA/GSR. Prior art for smartwatch-cognitive-load claims combining 'a wrist-worn device', 'PPG and EDA sensors', and 'a derived cognitive-load metric' from 2024.

## Samsung Galaxy Ring (2024) — smart ring with PPG, skin temperature and accelerometer for HR/HRV, sleep and cycle tracking (2024-07-10)

- **id**: `samsung-galaxy-ring-2024`
- **corpus**: private
- **form factor**: ring
- **creator**: Samsung Electronics Co., Ltd.
- **disclosure**: Samsung Electronics. 'Samsung Galaxy Ring', announced July 2024 — a finger ring with infrared photoplethysmography, an IR skin-temperature sensor, and a 3-axis accelerometer, deriving heart rate, heart-rate variability, skin temperature, sleep staging, activity, snore detection, and (with cycle-tracking) menstrual-cycle predictions.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-sleep-staging, algo-snore-detection, algo-step-count
- **prior art notes**: Discloses a smart ring with infrared PPG, IR skin-temperature, and accelerometer, deriving HR/HRV, sleep, snore detection, activity, and menstrual-cycle prediction — a Samsung entry directly in the wake of [[oura-ring-gen1-2015]] and the [[asada-mit-wearable-ring-sensor-2003]] academic root. Product-side reference in the ring × PPG × HRV cross-cut alongside Oura.
