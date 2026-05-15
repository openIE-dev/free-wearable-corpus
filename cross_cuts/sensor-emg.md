---
title: sensor-emg
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-emg`

Axis: **sensors**

**9 corpus entries disclose this tag.**

Earliest disclosure: 1968

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Rechtschaffen & Kales (1968) — standardized sleep-stage scoring manual (1968)

- **id**: `rechtschaffen-kales-1968-sleep-scoring-manual`
- **corpus**: standards
- **form factor**: other
- **creator**: Allan Rechtschaffen / Anthony Kales (eds), for the UCLA Brain Information Service
- **disclosure**: Rechtschaffen A, Kales A (eds). 'A Manual of Standardized Terminology, Techniques and Scoring System for Sleep Stages of Human Subjects.' Public Health Service / U.S. Government Printing Office / UCLA Brain Information Service, NIH Publication No. 204, 1968.
- **ip status**: standards
- **sensors**: sensor-eeg, sensor-eog, sensor-emg
- **algorithms**: algo-sleep-staging
- **prior art notes**: Standardizes the definition of sleep stages and the rules for scoring them from EEG + EOG + EMG (polysomnography). Any wearable claim reciting 'classifying sleep into stages from electrophysiological/physiological signals' rests on the staging framework standardized here. Combined with [[muse-headband-2014]]-type form-factor disclosures, makes wearable automated sleep-staging an obvious combination under [[obviousness-template]].

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

## Kim et al. (Rogers group) (2011) — 'Epidermal Electronics' (electronic-tattoo skin-mounted devices) (2011-08-12)

- **id**: `kim-rogers-2011-epidermal-electronics`
- **corpus**: academic
- **form factor**: tattoo-electronic
- **creator**: Dae-Hyeong Kim et al. / John A. Rogers group (Illinois)
- **disclosure**: Kim D-H, Lu N, Ma R, Kim Y-S, Kim R-H, Wang S, et al. (Rogers JA). 'Epidermal Electronics.' Science 2011;333(6044):838-843.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-emg, sensor-eeg, sensor-skin-temperature, sensor-strain-gauge
- **prior art notes**: Discloses ultrathin, skin-conformal ('epidermal') electronic devices laminated directly onto the skin like a temporary tattoo, integrating electrodes, sensors (ECG, EMG, EEG, temperature, strain), interconnects, and even wireless components, mechanically matched to the skin so they move with it. The foundational disclosure of the 'electronic skin / electronic tattoo' form factor. Any claim reciting 'an ultrathin stretchable electronic device conformally mounted on the skin' for physiological sensing reads on Kim/Rogers 2011. Anchor for the tattoo-electronic form-factor cross-cut on the real side.

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

## Elysium — surgically-integrated powered exoskeleton with neural control (2013-08-09)

- **id**: `elysium-bolt-on-exoskeleton`
- **corpus**: fictional
- **form factor**: exoskeleton
- **creator**: Neill Blomkamp / Media Rights Capital
- **disclosure**: Elysium (TriStar Pictures / Media Rights Capital), released August 9, 2013; a powered exoskeleton bolted to the wearer's skeleton and interfaced to the nervous system (with a head-mounted data port), augmenting strength and serving as a host platform for software/data.
- **ip status**: fictional
- **sensors**: sensor-emg
- **prior art notes**: Discloses a powered exoskeleton rigidly coupled to the wearer's skeleton and interfaced to the nervous system to read movement intent and augment force, while also functioning as an embedded compute/data platform. Relevant to powered-exoskeleton claims combining 'a wearable frame coupled to the body', 'actuators augmenting limb force', 'a neural or EMG interface sensing movement intent', and 'an onboard processor'. § 103 motivation that the neurally-controlled bolt-on powered exoskeleton was an articulated objective by 2013.

## OpenBCI Cyton — open-source 8-channel biosignal (EEG/EMG/ECG) acquisition board and 3D-printed headset (2014-01-22)

- **id**: `openbci-cyton-2014`
- **corpus**: open
- **form factor**: cap
- **creator**: Joel Murphy / Conor Russomanno (OpenBCI)
- **disclosure**: OpenBCI (Joel Murphy, Conor Russomanno). 'OpenBCI: An Open Source Brain-Computer Interface For Makers.' Kickstarter campaign launched 22 January 2014; hardware designs and firmware released open source at github.com/OpenBCI (Cyton board, Ganglion board, Ultracortex Mark IV 3D-printed headset).
- **ip status**: open-permissive
- **sensors**: sensor-saline-eeg-electrode, sensor-dry-eeg-electrode, sensor-emg, sensor-ecg
- **algorithms**: algo-bci-p300, algo-bci-ssvep, algo-bci-motor-imagery
- **prior art notes**: An openly-published, openly-licensed wearable biosignal acquisition system: a multi-channel ADS1299-based board, electrodes, and a 3D-printed head-worn frame for EEG/EMG/ECG, with reference firmware and BCI demonstrations. As open-hardware prior art it is unencumbered: any claim reciting a multi-channel head-worn biopotential acquisition device with the features published here (since 2014) reads on OpenBCI. Anchors the `open` bucket for biosignal wearables; relevant to headband/cap EEG and to EMG/ECG wearable claims.

## Upgrade — 'STEM' spinal AI implant with sensorimotor takeover (2018-03-10)

- **id**: `upgrade-stem-spinal-implant`
- **corpus**: fictional
- **form factor**: implantable
- **creator**: Leigh Whannell / Blumhouse
- **disclosure**: Upgrade (BH Tilt / Blumhouse), 2018; the 'STEM' chip implanted at the base of the spine interfaces with the host's nervous system, restoring and then augmenting motor control, processing sensory input, and acting as an on-board AI co-pilot for the body.
- **ip status**: fictional
- **sensors**: sensor-emg
- **prior art notes**: Discloses a spinal implant that bridges/replaces damaged neural pathways to restore motor control, processes the host's sensory input, and provides on-board computational assistance for movement. Relevant to spinal-cord-stimulation / motor-restoration implant claims combining 'a spinal implant interfacing motor and sensory pathways', 'restoration or augmentation of motor function', and 'an onboard processor'. § 103 motivation as of 2018. Cf. [[elysium-bolt-on-exoskeleton]].

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
