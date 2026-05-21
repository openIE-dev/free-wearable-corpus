---
title: sensor-ppg ∩ algo-respiratory-rate
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ppg` ∩ `algo-respiratory-rate`

Axes: **sensors × algorithms**

**9 corpus entries disclose both tags.**

Earliest disclosure: 2007-02-20

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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

## H-Watch (Magno et al., 2024) — open-source ARM Cortex-M4F + ML + NB-IoT + energy-harvesting research smartwatch (2024)

- **id**: `h-watch-magno-2024`
- **corpus**: academic
- **form factor**: watch
- **creator**: Michele Magno et al. (ETH Zürich and collaborators)
- **disclosure**: Magno M, et al. 'H-Watch: A Multi-Sensor Smart Wearable for COVID-19 Symptom Monitoring with ML and Energy Harvesting.' arXiv:2407.21501 (2024). Fully open-source smartwatch hardware + firmware for symptom monitoring: ARM Cortex-M4F MCU, on-device ML inference, NB-IoT cellular connectivity, integrated energy harvesting + battery. https://arxiv.org/abs/2407.21501
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-spo2, sensor-skin-temperature, sensor-accelerometer
- **algorithms**: algo-hr, algo-spo2-estimation, algo-respiratory-rate, algo-activity-classification
- **prior art notes**: Discloses a fully open-source research smartwatch combining multi-sensor vitals (PPG/SpO2/temperature/IMU), on-device ML inference, NB-IoT direct cellular connectivity (no phone required), and integrated energy harvesting to extend battery life — published with full hardware design and firmware. Prior art for symptom-monitoring smartwatch claims reciting any of those elements from 2024. Establishes that the cellular-connected open-hardware ML-enabled smartwatch is a published research design.

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
