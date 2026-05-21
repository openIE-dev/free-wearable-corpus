---
title: sensor-ecg ∩ algo-sleep-staging
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ecg` ∩ `algo-sleep-staging`

Axes: **sensors × algorithms**

**4 corpus entries disclose both tags.**

Earliest disclosure: 2013

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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

## BioIntelliSense BioSticker (2019) — long-wear adhesive chest patch with extensive multi-parameter monitoring (2019-12)

- **id**: `biointellisense-biosticker-2019`
- **corpus**: private
- **form factor**: patch
- **creator**: BioIntelliSense, Inc.
- **disclosure**: BioIntelliSense, Inc. 'BioSticker' single-use adhesive medical-grade biosensor, FDA-cleared 2019 — a chest patch with up to 30-day wear continuously measuring skin temperature, single-lead ECG-derived heart rate at rest, respiratory rate at rest, body position, activity (steps, cadence, gait), sleep, cough, vomiting events, and falls, with wireless upload.
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature, sensor-microphone-air
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-cough-detection, algo-gait-analysis, algo-sleep-staging
- **prior art notes**: Discloses a single-use 30-day adhesive chest patch combining skin temperature, resting HR-from-ECG, resting RR, posture/activity, sleep, cough and vomiting event detection, and falls — i.e. an unusually broad multi-parameter long-wear patch with explicit event-detection (cough, vomit) classifiers. Anticipates long-wear multi-parameter patch claims from 2019, including the event-detection (cough/vomit) elements that some later patents recite. Product-side anchor for the patch × long-wear multi-parameter cross-cut.

## Withings ScanWatch (2020) — hybrid analog watch with PPG, SpO2 pulse oximetry, single-lead ECG, and accelerometer (2020-01-05)

- **id**: `withings-scanwatch-2020`
- **corpus**: private
- **form factor**: watch
- **creator**: Withings SA
- **disclosure**: Withings (Nokia/Withings). 'ScanWatch', announced January 2020 (CE-marked 2020; FDA cleared 2022) — a hybrid analog wristwatch integrating a reflectance-PPG sensor (heart rate, irregular-rhythm screening), an SpO2 (pulse-oximetry) measurement, a single-lead ECG (back electrode plus a bezel electrode touched by the opposite hand, with AF detection), a 3-axis accelerometer, and an altimeter — with sleep and activity tracking.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-ecg, sensor-accelerometer, sensor-barometer
- **algorithms**: algo-hr, algo-spo2-estimation, algo-afib-detection, algo-arrhythmia-classification, algo-sleep-staging, algo-step-count, algo-respiratory-rate
- **prior art notes**: Discloses a wristwatch combining reflectance-PPG heart rate, pulse-oximetry SpO2, a single-lead ECG with AF detection, accelerometry, and an altimeter, with sleep-apnea screening (from the SpO2/respiration signals) — multiple regulated cardiorespiratory measurements in one consumer watch. Anticipates multi-modal medical-smartwatch claims reciting combinations of wrist PPG-HR + wrist SpO2 + single-lead ECG from 2020. Product-side anchor for the watch × {PPG, SpO2, ECG} multi-sensor cross-cut.

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
