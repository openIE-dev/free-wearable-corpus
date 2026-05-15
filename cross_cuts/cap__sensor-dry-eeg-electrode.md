---
title: cap ∩ sensor-dry-eeg-electrode
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `cap` ∩ `sensor-dry-eeg-electrode`

Axes: **form_factor × sensors**

**4 corpus entries disclose both tags.**

Earliest disclosure: 1982-07

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

## Neuromancer — 'trodes' (head-worn cyberspace interface) and 'simstim' (worn sensory-broadcast rig) (1982-07)

- **id**: `neuromancer-cyberspace-deck-trodes-and-simstim`
- **corpus**: fictional
- **form factor**: headband
- **creator**: William Gibson
- **disclosure**: Gibson, William. 'Burning Chrome', Omni, July 1982 (and Neuromancer, Ace Books, 1984); 'simstim' — a worn rig that records and broadcasts one person's complete sensory experience for another to inhabit — and the head-worn electrode set ('trodes') by which a 'console cowboy' jacks into the 'matrix'/cyberspace.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode
- **prior art notes**: Discloses (a) a head-worn, non-implanted electrode set providing bidirectional neural interface to a virtual/data environment, and (b) a worn rig that captures one wearer's full multisensory stream and broadcasts it for another to experience. Relevant to wearable-BCI and wearable-sensory-broadcast claims. § 103 motivation as of 1982 — predating [[strange-days-squid-recorder]] (1995) for sensory broadcast, and a head-worn (non-implanted) alternative to [[the-matrix-headjack]]. Non-enabling.

## Strange Days — SQUID head-worn neural experience recorder (1995-10-13)

- **id**: `strange-days-squid-recorder`
- **corpus**: fictional
- **form factor**: cap
- **creator**: Kathryn Bigelow / James Cameron (writer) / Lightstorm
- **disclosure**: Strange Days (Lightstorm Entertainment / 20th Century Fox), released October 13, 1995; the 'SQUID' — a fine wire-mesh cap worn under a hat that records the wearer's full multisensory and emotional experience directly from the cerebral cortex for later playback into another person's cortex.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **prior art notes**: Discloses a head-worn mesh of scalp electrodes that records a rich, multi-channel signal of the wearer's perceptual and affective experience for storage and later replay. Relevant to wearable neural-recording claims combining 'a head-worn array of scalp electrodes', 'acquisition of a multi-channel cortical signal', 'encoding of perceptual/affective content', and 'storage for later playback'. § 103 motivation that the wearable experience-recording headset was an articulated objective by 1995. Non-enabling on the encoding/playback; pair with enabling EEG/BCI art.

## Surrogates — head-worn neural interface rig for robot-body telepresence (2005-08-17)

- **id**: `surrogates-neural-teleoperation-rig`
- **corpus**: fictional
- **form factor**: headband
- **creator**: Robert Venditti and Brett Weldele
- **disclosure**: Venditti, Robert; Weldele, Brett. The Surrogates #1. Top Shelf Productions, 2005 (film adaptation: Touchstone Pictures, 2009); operators recline in a chair wearing a head-mounted neural interface that captures their volition and sensory channels to remotely embody and control a humanoid robot 'surrogate', receiving its sensory feedback in return.
- **ip status**: fictional
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **prior art notes**: Discloses a head-worn neural-interface rig that reads the wearer's motor intent and routes sensory feedback, used to teleoperate a humanoid robot with the operator perceiving through the robot's sensors. Relevant to wearable-BCI teleoperation claims combining 'a head-worn neural sensor array', 'decoding of motor intent', 'transmission of commands to a remote robot', and 'return of the robot's sensory data to the wearer'. § 103 motivation that the wearable neural-interface telepresence rig was an articulated objective by 2005. Non-enabling; pair with enabling BCI/teleop art.

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
