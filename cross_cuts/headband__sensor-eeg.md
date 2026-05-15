---
title: headband ∩ sensor-eeg
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `headband` ∩ `sensor-eeg`

Axes: **form_factor × sensors**

**5 corpus entries disclose both tags.**

Earliest disclosure: 2005-08-17

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Surrogates — head-worn neural interface rig for robot-body telepresence (2005-08-17)

- **id**: `surrogates-neural-teleoperation-rig`
- **corpus**: fictional
- **form factor**: headband
- **creator**: Robert Venditti and Brett Weldele
- **disclosure**: Venditti, Robert; Weldele, Brett. The Surrogates #1. Top Shelf Productions, 2005 (film adaptation: Touchstone Pictures, 2009); operators recline in a chair wearing a head-mounted neural interface that captures their volition and sensory channels to remotely embody and control a humanoid robot 'surrogate', receiving its sensory feedback in return.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **prior art notes**: Discloses a head-worn neural-interface rig that reads the wearer's motor intent and routes sensory feedback, used to teleoperate a humanoid robot with the operator perceiving through the robot's sensors. Relevant to wearable-BCI teleoperation claims combining 'a head-worn neural sensor array', 'decoding of motor intent', 'transmission of commands to a remote robot', and 'return of the robot's sensory data to the wearer'. § 103 motivation that the wearable neural-interface telepresence rig was an articulated objective by 2005. Non-enabling; pair with enabling BCI/teleop art.

## NeuroSky MindSet / MindWave (2007) — single dry-electrode consumer EEG headset (2007)

- **id**: `neurosky-mindset-2007`
- **corpus**: private
- **form factor**: headband
- **creator**: NeuroSky, Inc.
- **disclosure**: NeuroSky, Inc. 'MindSet' (and later 'MindWave') consumer EEG headset, with the 'ThinkGear' single dry forehead (Fp1) electrode and ear-clip reference, output as 'eSense' attention and meditation metrics plus raw EEG, first shown 2007.
- **ip status**: patented
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-attention-state, algo-cognitive-workload
- **prior art notes**: Discloses a low-cost head-worn single-channel dry-electrode EEG device (forehead pickup, ear reference) outputting raw EEG plus derived 'attention' and 'meditation/relaxation' metrics to a paired device. Anticipates consumer-EEG-headband claims combining 'a head-worn dry forehead electrode with an ear reference', 'on-device band-power feature extraction', and 'a derived attention/relaxation index' from 2007. Product-side anchor for the headband × EEG cross-cut; predates Muse (2014) and Emotiv EPOC (2009).

## Emotiv EPOC (2009) — 14-channel wireless saline-electrode consumer EEG headset (2009-12)

- **id**: `emotiv-epoc-2009`
- **corpus**: private
- **form factor**: headband
- **creator**: Emotiv Systems
- **disclosure**: Emotiv Systems. 'EPOC' EEG headset, released December 2009 — a 14-channel (plus 2 reference) wireless headset with saline-felt electrodes covering frontal/temporal/parietal/occipital sites, with SDKs for mental-command, facial-expression and 'affective' detections.
- **ip status**: patented
- **sensors**: sensor-saline-eeg-electrode, sensor-eeg
- **algorithms**: algo-cognitive-workload, algo-emotion-recognition, algo-bci-motor-imagery
- **prior art notes**: Discloses a wireless multi-channel (14+2) consumer EEG headset with saline-wetted contact electrodes at standard scalp sites and on-device/SDK classifiers for mental commands, facial expressions, and affective states. Anticipates multi-channel consumer-EEG-headset claims combining 'a wireless head-worn array of ≥8 contact electrodes', 'wet/saline electrode coupling', and 'classification of cognitive/affective state or intent' from 2009. Product-side anchor for the headband/cap × EEG cross-cut.

## Muse headband (InteraXon, 2014) — multi-channel dry-electrode EEG headband for meditation and sleep (2014-05)

- **id**: `muse-headband-2014`
- **corpus**: private
- **form factor**: headband
- **creator**: InteraXon Inc.
- **disclosure**: InteraXon Inc. 'Muse' brain-sensing headband, shipped 2014 — a forehead-band EEG device with frontal (AF7/AF8/Fp1/Fp2-region) and behind-the-ear (TP9/TP10) dry/conductive-rubber electrodes, giving real-time neurofeedback for meditation (and, in 'Muse S', sleep tracking).
- **ip status**: patented
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-attention-state, algo-cognitive-workload, algo-sleep-staging
- **prior art notes**: Discloses a forehead-band wearable EEG device with frontal and behind-the-ear (TP9/TP10) dry electrodes providing real-time neurofeedback for meditation training and (later) sleep staging. Anticipates EEG-headband claims combining 'a forehead band', 'frontal and mastoid/behind-ear dry electrodes', and 'real-time feedback on a meditation or sleep state' from 2014. Note: its TP9/TP10 around-ear pickup is the same general region used by [[zanetti-aminifar-atienza-eglass-2025]] — relevant prior art for around-ear-EEG wearable claims. Product-side anchor for the headband × EEG cross-cut.

## Debener et al. (2015) — cEEGrid: unobtrusive around-the-ear EEG with flexible printed electrodes (2015-11-17)

- **id**: `debener-2015-ceegrid-around-ear-eeg`
- **corpus**: academic
- **form factor**: patch
- **creator**: Stefan Debener / Martin G. Bleichner et al. (Oldenburg)
- **disclosure**: Debener S, Emkes R, De Vos M, Bleichner MG. 'Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear.' Scientific Reports 2015;5:16743.
- **ip status**: public-domain
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-erp-classification, algo-sleep-staging, algo-drowsiness-detection
- **prior art notes**: Discloses a flexible, printed, C-shaped electrode array worn around the ear (behind and below the auricle) for unobtrusive ambulatory EEG, recorded to a smartphone-class device. Any wearable claim reciting 'an array of EEG electrodes arranged around/behind the ear of the wearer' (the geometry used by EEG glasses, EEG earbuds, and EEG behind-the-ear stickers) reads on Debener et al. 2015. Directly relevant prior art for [[zanetti-aminifar-atienza-eglass-2025]] (which uses temporal/around-ear pickup) and for around-ear-EEG hearable claims; anchor for that cross-cut.
