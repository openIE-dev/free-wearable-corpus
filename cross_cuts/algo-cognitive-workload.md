---
title: algo-cognitive-workload
parent: Cross-cuts
layout: default
---

# Cross-cut: `algo-cognitive-workload`

Axis: **algorithms**

**4 corpus entries disclose this tag.**

Earliest disclosure: 2007

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

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

## e-Glass (Zanetti, Aminifar, Atienza; EPFL, 2025) — wearable EEG eyeglasses (2025-11-29)

- **id**: `zanetti-aminifar-atienza-eglass-2025`
- **corpus**: academic
- **form factor**: glasses
- **creator**: Renato Zanetti / Amir Aminifar / David Atienza (EPFL ESL)
- **disclosure**: Zanetti R, Aminifar A, Atienza D, et al. 'e-Glass: ...' (wearable EEG monitoring in an eyeglasses form factor with edge ML for seizure detection and cognitive-workload monitoring). Scientific Reports 2025. doi:10.1038/s41598-025-29893-4.
- **ip status**: unknown
- **sensors**: sensor-dry-eeg-electrode, sensor-eeg
- **algorithms**: algo-seizure-detection, algo-cognitive-workload
- **prior art notes**: Discloses an eyeglasses-form-factor wearable EEG monitor with dry electrodes at the temples / around the ears (temporal/occipital pickup, validated against a reference montage at r≈0.93) and on-device machine learning for two applications — ambulatory seizure detection and cognitive-workload monitoring. Relevant to AR-glasses / smart-eyewear claims reciting 'EEG electrodes integrated into an eyeglasses frame' and 'an on-device classifier operating on the EEG'. Anchor for the glasses × EEG cross-cut. Bounds the application space: temple/around-ear contact supports seizure, drowsiness, attention, SSVEP — not frontal ERP or motor-imagery BCI.
