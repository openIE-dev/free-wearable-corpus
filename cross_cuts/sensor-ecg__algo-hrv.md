---
title: sensor-ecg ∩ algo-hrv
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ecg` ∩ `algo-hrv`

Axes: **sensors × algorithms**

**5 corpus entries disclose both tags.**

Earliest disclosure: 1996-03

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

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
