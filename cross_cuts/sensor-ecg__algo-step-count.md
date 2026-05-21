---
title: sensor-ecg ∩ algo-step-count
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-ecg` ∩ `algo-step-count`

Axes: **sensors × algorithms**

**4 corpus entries disclose both tags.**

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

## Continua Health Alliance — Design Guidelines (first edition, 2007) (2007)

- **id**: `continua-design-guidelines-2007`
- **corpus**: standards
- **form factor**: other
- **creator**: Continua Health Alliance
- **disclosure**: Continua Health Alliance (later Personal Connected Health Alliance). 'Continua Design Guidelines' (first edition published 2007; subsequently maintained, ITU-T H.810 series). Specifies end-to-end interoperability for personal connected health devices, profiling IEEE 11073, Bluetooth, USB, ZigBee, HL7/IHE.
- **ip status**: standards
- **sensors**: sensor-ppg, sensor-ecg, sensor-glucose-cgm, sensor-accelerometer
- **algorithms**: algo-hr, algo-step-count, algo-glucose-cgm-readout
- **prior art notes**: Publicly-published end-to-end interoperability framework for personal connected health devices — defining how a body-worn sensor (weight scale, blood-pressure cuff, glucose meter, pulse oximeter, activity monitor, ECG, etc.) connects to an application hub and onward to health-record systems, profiling the underlying transport and data standards. Prior art for connected-wearable-system claims reciting the architecture, the device-to-hub-to-record data flow, or the standard profiles assembled here, public from 2007.

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
