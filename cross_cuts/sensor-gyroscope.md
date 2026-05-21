---
title: sensor-gyroscope
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-gyroscope`

Axis: **sensors**

**11 corpus entries disclose this tag.**

Earliest disclosure: 1992-03-06

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

- **The Lawnmower Man — VR rig (gyro chair, headset, full-body cybersuit)** (1992-03-06) — `lawnmower-man-vr-cybersuit` [fictional] — The Lawnmower Man (New Line Cinema), released 6 March 1992; a virtual-reality rig comprising a motorized gyroscopic chair, a head-mounted display, and a full-body 'cybersuit' that tracks the wearer's …
## Ready Player One full-body haptic suit and visor (2011-08-16)

- **id**: `ready-player-one-haptic-suit`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Ernest Cline
- **disclosure**: Cline, Ernest. Ready Player One. Crown Publishers, 2011 — a head-mounted VR visor plus a full-body haptic-feedback suit (with haptic gloves and boots) that renders touch sensations across the wearer's body and tracks body motion for immersive virtual presence.
- **ip status**: fictional
- **sensors**: sensor-accelerometer, sensor-gyroscope
- **prior art notes**: Discloses an integrated VR rig: a near-eye display visor plus a full-body garment with distributed haptic actuators and distributed motion sensors, providing whole-body force/tactile feedback registered to a virtual environment and capturing the wearer's posture and gestures. Relevant to haptic-garment claims combining 'a body-worn garment', 'an array of haptic actuators at multiple body sites', 'motion sensors capturing body pose', and 'coupling to a head-mounted display'. § 103 motivation that the full-body haptic VR suit was an articulated objective by 2011.

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

## Thalmic Labs Myo armband (2014) — consumer surface-EMG gesture-control armband (2013-02-25)

- **id**: `myo-armband-2014`
- **corpus**: private
- **form factor**: armband
- **creator**: Thalmic Labs Inc. (later North)
- **disclosure**: Thalmic Labs Inc. 'Myo gesture control armband', announced February 2013, shipped 2014 — a forearm-worn band of eight medical-grade stainless-steel surface-EMG electrode segments plus a 9-axis IMU, recognizing hand and finger gestures from the forearm-muscle electrical activity and arm orientation/motion, and transmitting them over Bluetooth as input to computers/devices.
- **ip status**: patented
- **sensors**: sensor-emg, sensor-accelerometer, sensor-gyroscope, sensor-magnetometer
- **algorithms**: algo-hand-gesture-emg, algo-keystroke-emg
- **prior art notes**: Discloses a forearm-worn band with an array of eight surface-EMG electrodes plus a 9-axis IMU that recognizes hand/finger gestures from forearm-muscle EMG combined with arm motion/orientation and transmits them wirelessly as a control input. A consumer realization of the myoelectric pattern-recognition approach ([[englehart-hudgins-2003-myoelectric-control]]); anticipates EMG-gesture-armband claims combining 'a band of surface-EMG electrodes worn around the forearm', 'an inertial sensor', and 'a classifier mapping the combined signal to a hand gesture / control command' from 2014. Product-side anchor for the armband × EMG cross-cut (the only `armband` form-factor entry besides [[mass-effect-omni-tool]] and [[fallout-pip-boy]]).

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

## Mojo Vision Mojo Lens (2022) — wearable AR contact lens with embedded microLED display (2022-06)

- **id**: `mojo-vision-ar-contact-lens-2022`
- **corpus**: private
- **form factor**: contact-lens
- **creator**: Mojo Vision, Inc.
- **disclosure**: Mojo Vision, Inc. 'Mojo Lens', publicly demonstrated June 2022 — a scleral contact lens with an embedded ~14k-PPI microLED display in the wearer's central field of view, an ARM Cortex processor, eye-tracking via motion sensors, a magnetometer for gaze direction, a microwave radio for offload, and a wirelessly charged battery; rendering an AR information overlay on the cornea. (The consumer AR-glucose pivot followed; production halted c. 2023.)
- **ip status**: patented
- **sensors**: sensor-accelerometer, sensor-gyroscope, sensor-magnetometer
- **algorithms**: algo-eye-gaze-tracking
- **prior art notes**: Discloses a contact lens with an embedded microLED display in the central visual field, on-lens processing, gaze tracking via inertial/magnetic sensors, wireless RF link, and a wirelessly charged on-lens battery — i.e. an AR display contact lens worn on the cornea. Anticipates AR-contact-lens claims combining 'a contact lens', 'an embedded near-eye microdisplay', 'on-lens processing and motion sensors for gaze', and 'a wireless link' from 2022. Product-side anchor for the contact-lens × visual-display cross-cut; cf. [[rainbows-end-ar-contact-lens]] (the 2006 fictional anticipation).

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
