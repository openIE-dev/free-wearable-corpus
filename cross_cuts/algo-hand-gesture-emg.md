---
title: algo-hand-gesture-emg
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-hand-gesture-emg`

Axis: **algorithms**

**3 corpus entries disclose this tag.**

Earliest disclosure: 2003-07

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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
