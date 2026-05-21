---
title: other ∩ sensor-accelerometer
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `other` ∩ `sensor-accelerometer`

Axes: **form_factor × sensors**

**5 corpus entries disclose both tags.**

Earliest disclosure: 2007

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
