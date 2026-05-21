---
title: watch ∩ sensor-skin-temperature
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `watch` ∩ `sensor-skin-temperature`

Axes: **form_factor × sensors**

**6 corpus entries disclose both tags.**

Earliest disclosure: 2010-01

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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

## Microsoft Band (2014) — ten-sensor wristband (optical HR, GPS, GSR, UV, skin temp, barometer, ambient light, capacitive, microphone, IMU) (2014-10-30)

- **id**: `microsoft-band-2014`
- **corpus**: private
- **form factor**: watch
- **creator**: Microsoft Corp.
- **disclosure**: Microsoft Corp. 'Microsoft Band', released 30 October 2014 — a wristband integrating ten sensors: an optical (PPG) heart-rate sensor, a 3-axis accelerometer/gyroscope, GPS, an ambient-light sensor, a skin-temperature sensor, a UV sensor, a capacitive (wear-detection) sensor, a galvanic-skin-response sensor, a microphone, and a barometer (added in Band 2).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-gyroscope, sensor-skin-temperature, sensor-uv, sensor-gsr, sensor-barometer, sensor-photodiode-ambient, sensor-microphone-air
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-sleep-staging, algo-stress-index, algo-uv-dose-tracking
- **prior art notes**: Discloses a single wristband integrating an unusually broad sensor suite — reflectance-PPG HR, IMU, GPS, skin temperature, UV exposure, galvanic skin response (electrodermal activity), barometer, ambient light, capacitive wear-detection, and a microphone — feeding HR, activity, sleep, UV dose, and stress-index estimations. Prior art for multi-sensor-wristband claims reciting combinations of these sensors (notably wrist GSR/EDA + PPG + skin temperature for stress) from October 2014. Product-side anchor for the multi-sensor wristband cross-cut.

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.

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
