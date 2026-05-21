---
title: sensor-accelerometer ∩ algo-pwv-bp-estimation
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `sensor-accelerometer` ∩ `algo-pwv-bp-estimation`

Axes: **sensors × algorithms**

**3 corpus entries disclose both tags.**

Earliest disclosure: 2014-10-07

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
