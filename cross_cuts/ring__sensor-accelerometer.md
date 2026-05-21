---
title: ring ∩ sensor-accelerometer
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `ring` ∩ `sensor-accelerometer`

Axes: **form_factor × sensors**

**5 corpus entries disclose both tags.**

Earliest disclosure: 2001-07

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## MIT wearable ring sensor (Rhee, Yang, Asada) — finger-ring PPG for ambulatory monitoring (2001-07)

- **id**: `asada-mit-wearable-ring-sensor-2003`
- **corpus**: academic
- **form factor**: ring
- **creator**: Sokwoo Rhee / Boo-Ho Yang / Haruhiko Harry Asada (MIT d'Arbeloff Lab)
- **disclosure**: Rhee S, Yang B-H, Asada HH. 'Artifact-resistant power-efficient design of finger-ring plethysmographic sensors.' IEEE Transactions on Biomedical Engineering 2001;48(7):795-805 (and Asada HH, Shaltis P, Reisner A, Rhee S, Hutchinson RC. 'Mobile monitoring with wearable photoplethysmographic biosensors.' IEEE Engineering in Medicine and Biology Magazine 2003;22(3):28-40).
- **ip status**: patented
- **sensors**: sensor-ppg, sensor-accelerometer
- **algorithms**: algo-hr, algo-spo2-estimation
- **prior art notes**: Discloses a finger-ring-form-factor wearable PPG sensor with motion-artifact-resistant optical/mechanical design, low-power operation, on-body processing, and wireless telemetry of heart rate and SpO2 for ambulatory monitoring — i.e. the smart-ring physiological monitor, ~14 years before the commercial smart-ring wave. Directly anticipates ring-form claims combining 'a ring body', 'a PPG emitter/detector at the inner ring surface', 'motion-artifact compensation', and 'wireless transmission of derived vitals'. Anchor for the ring × PPG cross-cut; [[oura-ring-gen1-2015]] and similar products descend from it.

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

## Tap Strap (Tap Systems, 2018) — finger-mounted gesture and keyboard input device (2018)

- **id**: `tap-systems-tap-strap-2018`
- **corpus**: private
- **form factor**: other
- **creator**: Tap Systems Inc. (founder: Dovid Schick)
- **disclosure**: Tap Systems Inc. (founded 2014, Sherman Oaks, CA). 'Tap Strap' wearable input device, shipped 2018 — five finger-loops connected by a flexible band across the back of the hand, with accelerometers on each finger detecting tapping and gesture; mapped onto a virtual keyboard, mouse, and gesture commands via BLE. Successor 'Tap Strap 2' (2019) and 'TapXR' (a wrist version, 2023). https://www.tapwithus.com
- **ip status**: patented
- **sensors**: sensor-accelerometer
- **algorithms**: algo-hand-gesture-emg
- **prior art notes**: Discloses a hand-worn device of multiple finger-loops linked by a back-of-hand band, with motion sensors on each finger detecting per-finger tap and swipe events and mapping them via BLE to a virtual keyboard / mouse / gesture protocol — wearable per-finger gesture input by motion sensing alone (no EMG). Directly relevant prior art for any finger/hand gesture-input wearable, including [[ctrl-labs-meta-wrist-emg-2018]] (EMG route), [[myo-armband-2014]] (forearm-EMG route), and ring-form gesture input devices. Anticipates per-finger-motion-sensor gesture-recognition wearable claims from 2018.

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
