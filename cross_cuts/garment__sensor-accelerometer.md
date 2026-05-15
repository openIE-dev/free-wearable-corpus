---
title: garment ∩ sensor-accelerometer
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `garment` ∩ `sensor-accelerometer`

Axes: **form_factor × sensors**

**12 corpus entries disclose both tags.**

Earliest disclosure: 1992

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Snow Crash 'Gargoyle' wearable computer rig (1992)

- **id**: `snow-crash-gargoyle-rig`
- **corpus**: fictional
- **form factor**: glasses
- **creator**: Neal Stephenson
- **disclosure**: Stephenson, Neal. Snow Crash. Bantam Books, 1992 — the 'gargoyles': people wearing head-mounted display goggles, body-worn computers, and continuous-capture sensors, with voice query and head tracking.
- **ip status**: fictional
- **sensors**: sensor-camera-rgb, sensor-microphone-air, sensor-accelerometer
- **prior art notes**: Discloses an integrated head-worn AR rig: near-eye display goggles + body-worn processor + always-on cameras and microphones + head-tracking, with voice queries against a networked database and continuous capture/upload of the wearer's surroundings. Relevant to AR-glasses claims combining 'a near-eye display', 'an outward-facing camera', 'an inertial sensor for head pose', 'a microphone for voice input', and 'continuous data capture/transmission'. § 103 motivation that the always-on capture-and-query AR wearable was a concrete objective by 1992. Non-enabling; pair with enabling HMD/SLAM art.

- **The Lawnmower Man — VR rig (gyro chair, headset, full-body cybersuit)** (1992-03-06) — `lawnmower-man-vr-cybersuit` [fictional] — The Lawnmower Man (New Line Cinema), released 6 March 1992; a virtual-reality rig comprising a motorized gyroscopic chair, a head-mounted display, and a full-body 'cybersuit' that tracks the wearer's …
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

## Paradiso et al. (2005) — 'A wearable health care system based on knitted integrated sensors' (WEALTHY) (2005-09)

- **id**: `paradiso-2005-wealthy-knitted-smart-shirt`
- **corpus**: academic
- **form factor**: garment
- **creator**: Rita Paradiso / Giannicola Loriga / Nicola Taccini (Smartex / CNR, Italy; EU WEALTHY consortium)
- **disclosure**: Paradiso R, Loriga G, Taccini N. 'A wearable health care system based on knitted integrated sensors.' IEEE Transactions on Information Technology in Biomedicine 2005;9(3):337-344. (Output of the EU FP5 'WEALTHY' project, 2002-2005.)
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-respiration-impedance, sensor-piezoelectric, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification
- **prior art notes**: Discloses a smart shirt with electrodes and sensors knitted directly into the textile (conductive yarns forming dry ECG electrodes; piezoresistive yarns forming respiration sensors via thoracic/abdominal expansion; accelerometer; temperature) plus an on-garment electronic interface and wireless link, deriving ECG, heart rate, respiration, posture/activity, and temperature — i.e. a fully integrated textile-electrode wearable. Any claim reciting 'an item of clothing with electrodes/sensors integrated into the fabric structure for physiological monitoring' reads on Paradiso 2005. Anchor for the garment × textile-electrode cross-cut; the foundational EU project for the smart-shirt patent space (Hexoskin, Cityzen, etc. all build on this lineage).

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

## Pacific Rim — Jaeger 'Drivesuit' and 'Conn-Pod' dual-pilot neural bridge (2013-07-12)

- **id**: `pacific-rim-drivesuit-and-conn-pod`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Guillermo del Toro / Legendary Pictures
- **disclosure**: Pacific Rim (Warner Bros. / Legendary), released 12 July 2013; pilots wear a 'Drivesuit' (a body suit capturing motion and monitoring vitals) and a 'relay-gel'/spinal-clamp helmet that creates a shared neural bridge ('the Drift') between two co-pilots and the mecha.
- **ip status**: fictional
- **sensors**: sensor-ecg, sensor-dry-eeg-electrode, sensor-accelerometer
- **algorithms**: algo-hr
- **prior art notes**: Discloses an instrumented pilot suit (motion capture + vital-sign monitoring) combined with head/spine-worn relays that establish a shared neural bridge between two operators and a controlled machine. Relevant to multi-operator neural-interface claims and to instrumented-bodysuit claims combining 'a motion-capturing garment', 'vital-sign monitoring', and 'a head/spine neural relay linking multiple operators'. § 103 motivation as of 2013. Cf. [[nge-plug-suit-and-a10-clips]] (single-pilot), [[surrogates-neural-teleoperation-rig]].

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

## Stark 'Iron Spider' suit with mask HUD and AI ('Karen') (2017-07-07)

- **id**: `stark-iron-spider-suit`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Marvel Studios / Sony Pictures
- **disclosure**: Spider-Man: Homecoming (Marvel Studios / Sony), released July 7, 2017; the Stark-built suit with an in-mask heads-up display, an integrated conversational AI ('Karen'), distributed suit sensors, environmental analysis, biometric monitoring of the wearer, a deployable drone, and configurable web-shooter telemetry.
- **ip status**: fictional
- **sensors**: sensor-camera-rgb, sensor-accelerometer, sensor-microphone-air
- **algorithms**: algo-emotion-recognition
- **prior art notes**: Discloses a smart full-body garment integrating: an in-mask near-eye HUD; a conversational AI assistant resident in the suit; distributed suit sensors and environmental analysis (object/person identification, threat assessment); biometric monitoring of the wearer (HR, respiration, stress); and reconfigurable actuator/output settings. Relevant to smart-garment and helmet-HUD claims combining 'a body-worn garment with distributed sensors', 'a head-mounted display presenting environmental and physiological data', 'a voice AI', and 'wearer biometric monitoring'. § 103 motivation that the integrated sensing/HUD/AI body suit was an articulated objective by 2017.
