---
title: headband ∩ sensor-dry-eeg-electrode
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `headband` ∩ `sensor-dry-eeg-electrode`

Axes: **form_factor × sensors**

**9 corpus entries disclose both tags.**

Earliest disclosure: 1979-04-07

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Mobile Suit Gundam — 'psycommu' head-worn neural interface for remote weapon control (1979-04-07)

- **id**: `gundam-psycommu-interface`
- **corpus**: fictional
- **form factor**: helmet
- **creator**: Yoshiyuki Tomino / Nippon Sunrise
- **disclosure**: Mobile Suit Gundam (Nippon Sunrise television series, premiered 7 April 1979); the 'psycommu' system — a head-worn interface that reads the pilot's brainwaves to direct remote weapon units ('funnels'/'bits') and control the mobile suit without manual input.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode
- **prior art notes**: Discloses a head-worn neural sensor that decodes the wearer's intent from brain activity and uses it to command remote machines/weapons and a piloted vehicle hands-free. Relevant to wearable-BCI claims combining 'a head-worn neural sensor array', 'decoding of operator intent', and 'transmission of commands to remote devices'. § 103 motivation that the wearable neural-control interface for remote devices was an articulated objective by 1979 — predating [[surrogates-neural-teleoperation-rig]].

## Neuromancer — 'trodes' (head-worn cyberspace interface) and 'simstim' (worn sensory-broadcast rig) (1982-07)

- **id**: `neuromancer-cyberspace-deck-trodes-and-simstim`
- **corpus**: fictional
- **form factor**: headband
- **creator**: William Gibson
- **disclosure**: Gibson, William. 'Burning Chrome', Omni, July 1982 (and Neuromancer, Ace Books, 1984); 'simstim' — a worn rig that records and broadcasts one person's complete sensory experience for another to inhabit — and the head-worn electrode set ('trodes') by which a 'console cowboy' jacks into the 'matrix'/cyberspace.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode
- **prior art notes**: Discloses (a) a head-worn, non-implanted electrode set providing bidirectional neural interface to a virtual/data environment, and (b) a worn rig that captures one wearer's full multisensory stream and broadcasts it for another to experience. Relevant to wearable-BCI and wearable-sensory-broadcast claims. § 103 motivation as of 1982 — predating [[strange-days-squid-recorder]] (1995) for sensory broadcast, and a head-worn (non-implanted) alternative to [[the-matrix-headjack]]. Non-enabling.

## Neon Genesis Evangelion — 'plug suit' and 'A10 nerve clips' (bio-monitoring suit + head-worn neural sync interface) (1995-10-04)

- **id**: `nge-plug-suit-and-a10-clips`
- **corpus**: fictional
- **form factor**: garment
- **creator**: Hideaki Anno / Gainax
- **disclosure**: Neon Genesis Evangelion (Gainax television series, premiered 4 October 1995); pilots wear a skin-tight pressurized 'plug suit' with continuous bio-monitoring and a measured 'synchronization ratio' with the mecha, plus 'A10 nerve clips' worn on the head that interface the pilot's nervous system to the machine.
- **ip status**: fictional
- **sensors**: sensor-ecg, sensor-dry-eeg-electrode, sensor-respiration-impedance
- **algorithms**: algo-hr, algo-respiratory-rate
- **prior art notes**: Discloses (a) a form-fitting body garment with continuous vital-sign monitoring and a derived operator-machine synchronization metric, and (b) head-worn clips coupling the wearer's nervous system to an external system. Relevant to instrumented-bodysuit claims combining 'a close-fitting garment with distributed physiological sensors' and 'a derived synchronization/engagement metric', and to head-worn neural-interface claims. § 103 motivation as of 1995. Cf. [[pacific-rim-drivesuit-and-conn-pod]] (a later dual-pilot variant).

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

## Black Mirror 'Crocodile' — portable memory-extraction device ('the recaller') (2017-12-29)

- **id**: `black-mirror-crocodile-recaller`
- **corpus**: fictional
- **form factor**: headband
- **creator**: Charlie Brooker / House of Tomorrow
- **disclosure**: Black Mirror, 'Crocodile' (Netflix, 29 December 2017); a portable device with a small sensor placed on a person's temple reads and displays their memories of an event for insurance/forensic corroboration.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode
- **prior art notes**: Discloses a portable temple-applied sensor that decodes and displays a subject's recalled visual memory of a target event. Relevant to neural-decoding claims combining 'a scalp/temple electrode', 'evocation of a specific episodic memory', and 'reconstruction of a visual representation'. § 103 motivation that portable memory readout was an articulated objective by 2017. Cf. [[strange-days-squid-recorder]] (recording rather than later readout).
