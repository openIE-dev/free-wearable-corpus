---
title: watch ∩ sensor-gyroscope
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `watch` ∩ `sensor-gyroscope`

Axes: **form_factor × sensors**

**6 corpus entries disclose both tags.**

Earliest disclosure: 2012-04-20

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Patel et al. (2012) — 'A review of wearable sensors and systems with application in rehabilitation' (2012-04-20)

- **id**: `patel-bonato-2012-wearable-sensors-rehab-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Shyamal Patel / Hyung Park / Paolo Bonato et al.
- **disclosure**: Patel S, Park H, Bonato P, Chan L, Rodgers M. 'A review of wearable sensors and systems with application in rehabilitation.' Journal of NeuroEngineering and Rehabilitation 2012;9:21.
- **ip status**: public-domain
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-emg, sensor-ecg, sensor-ppg, sensor-pressure-skin
- **algorithms**: algo-gait-analysis, algo-activity-classification, algo-fall-detection, algo-tremor-detection, algo-bradykinesia-detection, algo-posture-detection
- **prior art notes**: Reviews, as of 2012, wearable inertial/EMG/pressure sensor systems for movement and physiological monitoring in rehabilitation and chronic-disease management — gait analysis, activity and posture classification, fall detection, tremor and bradykinesia quantification (Parkinson's), with the sensor placements (foot/insole, shank, thigh, trunk, wrist, forearm) and algorithms. Prior art for wearable movement-disorder and gait-monitoring claims reciting any of the placements/analytics surveyed; collected and published by 2012. General anchor for the gait / tremor / activity cross-cuts.

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

## Apple Watch (1st generation, 2015) — wrist green-PPG heart rate and activity (2015-04-24)

- **id**: `apple-watch-original-2015`
- **corpus**: private
- **form factor**: watch
- **creator**: Apple Inc.
- **disclosure**: Apple Inc. 'Apple Watch', announced September 2014, available 24 April 2015 — a wrist-worn device with a green/infrared photoplethysmography heart-rate sensor against the dorsal wrist, accelerometer and gyroscope, and activity/exercise tracking.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-multi-wavelength-ppg, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification
- **prior art notes**: Discloses a wristworn device with a dorsal-wrist green-LED photoplethysmography heart-rate sensor (with IR for low-perfusion conditions), inertial sensors, and continuous HR/activity tracking. Anticipates wristworn-PPG-HR claims to the extent they postdate April 2015; combined with the much earlier PPG principle ([[hertzman-1937-photoplethysmography]]) and wrist form factor, the combination is in any case obvious under [[obviousness-template]]. Product-side anchor for the watch × PPG cross-cut.

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

## Open-Watch (Salar Motlaqolahi, 2021) — fully documented open STM32 smartwatch (BSc thesis) (2021)

- **id**: `smotlaq-open-watch-2021`
- **corpus**: open
- **form factor**: watch
- **creator**: Salar Motlaqolahi
- **disclosure**: Motlaqolahi S. 'Open-Watch' — fully open-source smartwatch released as BSc thesis output (MIT license). Hardware: STM32 ARM Cortex-M MCU, MPU6050 6-axis IMU, MAX30102 reflectance PPG + SpO2, 4-layer PCB sponsored by PCBWay, full schematics + Gerbers + firmware published. https://github.com/SMotlaq/open-watch
- **ip status**: open-permissive
- **sensors**: sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-gyroscope
- **algorithms**: algo-hr, algo-spo2-estimation, algo-step-count
- **prior art notes**: Discloses, as an MIT-licensed open-hardware smartwatch with full PCB design files (4-layer, PCBWay-sponsored fabrication) and firmware published, a wrist-worn device with reflectance PPG + SpO2 + 6-axis IMU + MCU + display. Demonstrates that the entire smartwatch design — schematic, layout, firmware — can be reproduced from undergraduate-thesis-level public work, defeating any claim that the integrated smartwatch is novel as a combination.

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
