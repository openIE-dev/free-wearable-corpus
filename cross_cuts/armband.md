---
title: armband
parent: Cross-cuts
layout: default
---

# Cross-cut: `armband`

Axis: **form_factor**

**9 corpus entries disclose this tag.**

Earliest disclosure: 1982

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Polar Sport Tester PE2000 — first wireless wrist heart-rate monitor (1982)

- **id**: `polar-sport-tester-pe2000-1982`
- **corpus**: private
- **form factor**: watch
- **creator**: Polar Electro Oy (Seppo Säynäjäkangas)
- **disclosure**: Polar Electro Oy. 'Sport Tester PE2000' wrist heart-rate monitor, introduced 1982 — a chest electrode strap transmitting ECG-derived heart rate wirelessly to a wrist-worn receiver/display. Underlying invention: Seppo Säynäjäkangas, wireless heart-rate measurement, patents filed from c. 1977 (Polar Electro).
- **ip status**: patented
- **sensors**: sensor-ecg
- **algorithms**: algo-hr
- **prior art notes**: Discloses a body-worn heart-rate monitoring system: a chest strap with electrodes deriving heart rate from the ECG and transmitting it wirelessly to a wrist-worn receiver that displays it. Anticipates claims combining 'a chest-worn electrode assembly sensing heart rate' and 'wireless transmission to a wrist-worn display' (the chest-strap-plus-watch architecture), and the bare 'wristworn heart-rate display' concept, from 1982 (invention c. 1977). Anchor for the wristworn-HR cross-cut on the product side; [[bluetooth-sig-heart-rate-profile-2011]] later standardized the comms link.

## Fallout — the 'Pip-Boy' (forearm-worn personal computer with multi-parameter health and radiation monitoring) (1997-10-10)

- **id**: `fallout-pip-boy`
- **corpus**: fictional
- **form factor**: watch
- **creator**: Interplay / Black Isle Studios
- **disclosure**: Fallout (Interplay, released 10 October 1997; the wrist/forearm-worn 'Pip-Boy' device); a forearm-mounted personal computer with a display showing the wearer's overall and limb-by-limb health, radiation exposure dose ('rads'), addiction/affliction status, plus inventory, local and world maps with positioning, a radio receiver, and a clock.
- **ip status**: fictional
- **sensors**: sensor-uv
- **algorithms**: algo-uv-dose-tracking
- **prior art notes**: Discloses a forearm-worn personal computer that continuously displays the wearer's health (overall and per-limb), accumulated radiation dose, and affliction status, alongside maps with positioning, a radio, an inventory, and a clock. Relevant to wrist/forearm-worn-monitor claims combining 'a body-worn display device', 'continuous multi-parameter physiological/exposure monitoring (including ionizing-radiation dosimetry)', 'mapping with positioning', and 'a media receiver'. § 103 motivation that the forearm-worn multi-parameter health/dosimetry computer was an articulated objective by 1997. Cf. [[inspector-gadget-wrist-computer]], [[pokemon-poketch]].

## Englehart & Hudgins (2003) — robust real-time multifunction myoelectric (surface-EMG) control (2003-07)

- **id**: `englehart-hudgins-2003-myoelectric-control`
- **corpus**: academic
- **form factor**: armband
- **creator**: Kevin Englehart / Bernard Hudgins (UNB)
- **disclosure**: Englehart K, Hudgins B. 'A robust, real-time control scheme for multifunction myoelectric control.' IEEE Transactions on Biomedical Engineering 2003;50(7):848-854.
- **ip status**: public-domain
- **sensors**: sensor-emg
- **algorithms**: algo-hand-gesture-emg, algo-keystroke-emg
- **prior art notes**: Discloses a real-time scheme that classifies the intended hand/finger action from multi-channel surface EMG (feature extraction over short windows, pattern-recognition classifier, continuous decision streaming) — the basis of EMG gesture-control wristbands/armbands. Any wearable claim reciting 'classifying a hand gesture or movement intent from surface electromyography electrodes worn around the forearm/wrist' reads on Englehart & Hudgins 2003 for the classification method; combined with the armband form factor it makes an EMG gesture-control band obvious under [[obviousness-template]]. Anchor for the EMG × gesture-recognition cross-cut; [[myo-armband-2014]] is the product.

## Mass Effect — the 'omni-tool' (forearm-worn device with projected holographic interface and medical scanning) (2007-11-20)

- **id**: `mass-effect-omni-tool`
- **corpus**: fictional
- **form factor**: armband
- **creator**: BioWare / Microsoft Game Studios
- **disclosure**: Mass Effect (BioWare / Microsoft Game Studios, released 20 November 2007); the 'omni-tool' — a forearm-mounted device that projects a holographic interface from the wrist/forearm and performs on-the-spot fabrication, hacking/data access, medical scanning and 'medi-gel' application, communication, and object analysis.
- **ip status**: fictional
- **prior art notes**: Discloses a forearm-worn device that projects an interactive holographic interface above the wearer's forearm and provides medical scanning and treatment delivery, fabrication, data access, comms, and object analysis. Relevant to forearm/wrist-worn-device claims combining 'a body-worn device', 'a projected/holographic interactive interface', and 'an integrated medical scanning/treatment function'. § 103 motivation that the forearm device with a projected UI and medical functions was an articulated objective by 2007. Cf. [[fallout-pip-boy]], [[black-panther-kimoyo-beads]].

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

## CTRL-labs (later Meta) wrist surface-EMG band (2018) — neural-interface wristband for finger/hand intent decoding (2018-10)

- **id**: `ctrl-labs-meta-wrist-emg-2018`
- **corpus**: private
- **form factor**: armband
- **creator**: CTRL-Labs Corp. (Thomas Reardon, Patrick Kaifosh, Tim Machado); later Meta Reality Labs
- **disclosure**: CTRL-Labs Corp. (Thomas Reardon, Patrick Kaifosh, Tim Machado) — surface-EMG wristband ('CTRL-kit') publicly demonstrated October 2018 at TechCrunch Disrupt and elsewhere: a wrist-worn band of dry EMG electrodes that decodes individual motor-unit firings on the wrist/forearm to infer finger/hand intent (including individuated finger movement and even imagined movement) as an input modality. CTRL-labs was acquired by Facebook (later Meta) in September 2019; the Meta production wristband for AR glasses is the descendant.
- **ip status**: patented
- **sensors**: sensor-emg, sensor-dry-eeg-electrode
- **algorithms**: algo-hand-gesture-emg, algo-keystroke-emg
- **prior art notes**: Discloses a wrist-worn band of dry surface-EMG electrodes that decodes individual motor-unit firings to infer fine finger and hand intent — including individuated single-finger motions and 'imagined' movements with no overt muscle contraction — as a continuous neural-control input modality. Distinct from gross-gesture EMG decoders ([[myo-armband-2014]]) in its motor-unit-level resolution. Anticipates neural-interface-wristband claims combining 'a wrist band of surface-EMG electrodes', 'motor-unit-level decoding', and 'individual finger / imagined-movement output' from 2018. Product-side anchor for the wrist × EMG × neural-input cross-cut; the Meta production wristband descends from it.
