---
title: sensor-ppg ∩ algo-activity-classification
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ppg` ∩ `algo-activity-classification`

Axes: **sensors × algorithms**

**10 corpus entries disclose both tags.**

Earliest disclosure: 2003

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Garmin Forerunner 201 (2003) — wristworn GPS running watch with pace/distance and heart-rate (strap) integration (2003)

- **id**: `garmin-forerunner-201-2003`
- **corpus**: private
- **form factor**: watch
- **creator**: Garmin Ltd.
- **disclosure**: Garmin Ltd. 'Forerunner 101/201', introduced 2003 — a wrist-worn GPS receiver/watch logging pace, distance, route, and (with a paired chest strap) heart rate, with workout history and a web/PC sync. Later Garmin watches (Fenix/Forerunner with the 'Elevate' optical sensor, c. 2015) moved heart rate, and subsequently SpO2 (pulse ox) and respiration, onto the wrist.
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-ecg, sensor-ppg
- **algorithms**: algo-hr, algo-step-count, algo-calorie-estimation, algo-activity-classification
- **prior art notes**: Discloses a wrist-worn GPS sport watch deriving pace, distance, and route, integrating heart rate from a paired electrode chest strap, and syncing workout history to a host — and, in later Garmin models, on-wrist optical-PPG heart rate, SpO2, and respiration. Anticipates GPS-sport-watch claims from 2003 and (for the later models) wrist-optical-vitals claims. Product-side anchor for the watch × GPS-fitness cross-cut.

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

## Bragi Dash (2014) — the first true 'hearable': in-ear PPG heart rate, accelerometer, storage and touch control inside wireless earbuds (2014-02-25)

- **id**: `bragi-dash-2014`
- **corpus**: private
- **form factor**: earbud
- **creator**: Bragi GmbH
- **disclosure**: Bragi GmbH. 'The Dash' wireless smart earphones, crowdfunded February 2014 (shipped 2016) — fully wireless in-ear earbuds with a reflectance-PPG heart-rate sensor and oxygen-saturation estimation against the ear-canal wall, a 3-axis accelerometer (head-gesture and step/activity tracking), 4 GB onboard music storage, bone-conduction microphone, and capacitive touch control.
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-spo2, sensor-accelerometer, sensor-microphone-bone
- **algorithms**: algo-hr, algo-spo2-estimation, algo-step-count, algo-activity-classification
- **prior art notes**: Discloses fully-wireless in-ear earbuds with a reflectance-PPG heart-rate and SpO2 sensor against the ear-canal wall, an accelerometer for head-gesture and step/activity tracking, onboard music storage, a bone-conduction microphone, and capacitive touch control — i.e. physiological sensing integrated into wireless earbuds. Anticipates hearable claims combining 'a wireless earbud housing', 'an in-ear PPG/SpO2 sensor', 'an accelerometer for activity or head gesture', and 'on-device media and controls' from 2014. Product-side anchor for the earbud × PPG cross-cut.

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

## Bangle.js 2 (Espruino, 2021) — open JavaScript-app smartwatch validated in academic research (2021)

- **id**: `bangle-js-2-2021`
- **corpus**: open
- **form factor**: watch
- **creator**: Pur3 Ltd. (Gordon Williams, Espruino)
- **disclosure**: Espruino / Pur3 Ltd. 'Bangle.js 2', released 2021 — Nordic nRF52840 (ARM Cortex-M4), GPS, heart rate, 3-axis accelerometer, magnetometer, pressure sensor; 4-week battery life; JavaScript app development with web-based app loader. https://banglejs.com . Validated for step counting and heart-rate measurement in academic research (multi-subject MDPI study).
- **ip status**: open-permissive
- **sensors**: sensor-ppg, sensor-accelerometer, sensor-magnetometer, sensor-barometer
- **algorithms**: algo-hr, algo-step-count, algo-activity-classification
- **prior art notes**: Discloses an open-hardware smartwatch with PPG + IMU + magnetometer + barometer + GPS, web-loaded JavaScript apps, and 4-week battery life — validated against reference devices in peer-reviewed studies for step counting and HR. As open-source hardware released in 2021 it is unencumbered prior art against patents reciting the open-firmware-platform smartwatch with this sensor set.

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
