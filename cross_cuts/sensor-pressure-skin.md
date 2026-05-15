---
title: sensor-pressure-skin
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-pressure-skin`

Axis: **sensors**

**4 corpus entries disclose this tag.**

Earliest disclosure: 1973

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Peñáz (1973) — the volume-clamp (vascular unloading) method of continuous finger blood pressure (1973)

- **id**: `penaz-1973-volume-clamp-finger-bp`
- **corpus**: academic
- **form factor**: other
- **creator**: Jan Peñáz
- **disclosure**: Peñáz J. 'Photoelectric measurement of blood pressure, volume and flow in the finger.' Digest of the 10th International Conference on Medical and Biological Engineering, Dresden, 1973, p. 104. (Basis of the Finapres / volume-clamp continuous BP monitors.)
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-cuffless-bp-volume-clamp, sensor-pressure-skin
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Discloses the volume-clamp / vascular-unloading method: a finger cuff servo-controlled by a photoplethysmographic feedback loop to hold the arterial volume constant, so the applied counter-pressure tracks the arterial pressure waveform continuously and non-invasively. Any cuffless/continuous-BP wearable claim reciting 'a photoplethysmographic feedback loop controlling an applied pressure to maintain constant vascular volume' reads on Peñáz 1973. Anchor for the volume-clamp cuffless-BP cross-cut (the finger/ring form-factor variants are obvious combinations under [[obviousness-template]]).

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

## Sensoria Smart Socks (2014) — pressure-sensing sock + electronic anklet for gait/running analysis (2014-01)

- **id**: `sensoria-smart-socks-2014`
- **corpus**: private
- **form factor**: sock
- **creator**: Sensoria Inc. (formerly Heapsylon)
- **disclosure**: Sensoria Inc. 'Sensoria Fitness Smart Socks', announced January 2014 — running socks with three pressure-sensitive textile sensors woven into the sole (under the heel, ball of foot, and toes) and a magnetically-attached 'Sensoria Core' anklet (accelerometer + Bluetooth) that derives cadence, foot strike pattern (heel/mid/forefoot), foot landing zone, pace, distance, and provides real-time audio coaching.
- **ip status**: patented
- **sensors**: sensor-pressure-skin, sensor-piezoelectric, sensor-accelerometer
- **algorithms**: algo-step-count, algo-gait-analysis, algo-activity-classification
- **prior art notes**: Discloses a sock with multiple pressure-sensitive textile sensors woven into the sole, paired with a removable ankle-worn electronics module that derives cadence, foot-strike pattern, pressure distribution, and pace. Anticipates smart-sock/sole-pressure-sensing claims combining 'a sock with one or more textile pressure sensors at multiple positions of the foot sole' and 'a paired electronics module deriving gait metrics' from 2014. Product-side anchor for the sock form-factor cross-cut (the only `sock` entry); cf. [[nike-plus-ipod-sport-kit-2006]] (the earlier shoe/insole route).

## Omron HeartGuide (2019) — wristwatch with an inflatable oscillometric blood-pressure cuff in the band (2019-01-08)

- **id**: `omron-heartguide-2019`
- **corpus**: private
- **form factor**: watch
- **creator**: Omron Healthcare Co., Ltd.
- **disclosure**: Omron Healthcare. 'HeartGuide' (model BP8000-M), announced January 2019, FDA-cleared — a wristwatch whose band contains an inflatable cuff and an oscillometric pressure transducer, taking a clinically-validated brachial-style blood-pressure measurement at the wrist on demand, alongside heart rate, steps, and sleep.
- **ip status**: patented
- **sensors**: sensor-pressure-skin, sensor-accelerometer, sensor-ppg
- **algorithms**: algo-hr, algo-step-count, algo-sleep-staging
- **prior art notes**: Discloses a wristwatch whose strap incorporates an inflatable cuff and pressure transducer, performing an oscillometric blood-pressure measurement at the wrist (occlude-and-release, automatically positioned at heart level by the wearer) in a watch form factor, plus activity and sleep tracking. Distinct from cuffless-PPG approaches: it is a true oscillometric cuff miniaturized into a watch band. Anticipates watch-with-integrated-inflatable-cuff BP claims from 2019. Product-side anchor for the watch × oscillometric-BP cross-cut (vs. the cuffless-PPG variant in [[samsung-galaxy-watch-bp-ecg-2020]] and [[aktiia-bracelet-cuffless-bp-2021]]).
