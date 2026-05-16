---
title: patch
parent: Cross-cuts
layout: default
---

# Cross-cut: `patch`

Axis: **form_factor**

**24 corpus entries disclose this tag.**

Earliest disclosure: 1961-04-21

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Holter (1961) — continuous ambulatory electrocardiography (the Holter monitor) (1961-04-21)

- **id**: `holter-1961-ambulatory-ecg`
- **corpus**: academic
- **form factor**: garment
- **creator**: Norman J. Holter
- **disclosure**: Holter NJ. 'New method for heart studies: continuous electrocardiography of active subjects over long periods is now practical.' Science 1961;134(3486):1214-1220.
- **ip status**: public-domain
- **sensors**: sensor-ecg
- **algorithms**: algo-arrhythmia-classification
- **prior art notes**: Establishes continuous, ambulatory, body-worn recording of the ECG over hours to days while the subject is active, for later analysis — the foundational 'wearable continuous ECG monitor'. Any claim reciting 'a body-worn device configured to continuously record an electrocardiographic signal of the wearer over an extended period for subsequent arrhythmia analysis' reads on Holter 1961. Anchor for the ambulatory-ECG / ECG-patch cross-cut; [[zio-patch-irhythm-2009]] and Apple Watch's ECG history both build on it.

## Shichiri et al. (1982) — wearable artificial pancreas with needle-type subcutaneous glucose sensor (1982-11-20)

- **id**: `shichiri-1982-wearable-needle-glucose-sensor`
- **corpus**: academic
- **form factor**: patch
- **creator**: Motoaki Shichiri et al. (Osaka University)
- **disclosure**: Shichiri M, Kawamori R, Yamasaki Y, Hakui N, Abe H. 'Wearable artificial endocrine pancreas with needle-type glucose sensor.' The Lancet 1982;320(8308):1129-1131.
- **ip status**: unknown
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses a body-worn device with a needle-type electrochemical glucose sensor inserted into subcutaneous tissue, continuously transducing interstitial glucose and (in the closed-loop variant) driving insulin delivery — i.e. the wearable continuous glucose monitor, ~24 years before commercial CGM. Directly anticipates CGM claims combining 'a wearable housing', 'a percutaneous needle-type enzyme-electrode sensor in subcutaneous tissue', and 'continuous transduction of interstitial glucose'. Anchor for the patch × glucose-CGM cross-cut; Medtronic MiniMed (1999), Dexcom (2006), Abbott Libre (2014) all descend from this form.

## Mendelson & Ochs (1988) — reflectance-mode pulse oximetry / skin-reflectance PPG (1988-10)

- **id**: `mendelson-ochs-1988-reflectance-pulse-oximetry`
- **corpus**: academic
- **form factor**: other
- **creator**: Yitzhak Mendelson / Burt D. Ochs
- **disclosure**: Mendelson Y, Ochs BD. 'Noninvasive pulse oximetry utilizing skin reflectance photoplethysmography.' IEEE Transactions on Biomedical Engineering 1988;35(10):798-805.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-spo2, sensor-multi-wavelength-ppg
- **algorithms**: algo-spo2-estimation, algo-hr
- **prior art notes**: Establishes pulse oximetry by reflectance (light source and detector on the same side of the tissue) rather than transmission — the geometry every wrist, forehead, ring, chest, and earbud PPG/SpO2 wearable uses, since those sites cannot be transilluminated. Any wearable-SpO2 claim reciting 'a reflectance photoplethysmography sensor' or 'a light source and photodetector arranged on a common surface against the skin' reads on Mendelson & Ochs 1988. Anchor for the reflectance-PPG/SpO2 cross-cut on non-fingertip sites.

## Medtronic MiniMed CGMS (1999) — first FDA-cleared continuous glucose monitoring system (1999-06)

- **id**: `medtronic-minimed-cgms-1999`
- **corpus**: private
- **form factor**: patch
- **creator**: MiniMed Inc. / Medtronic Diabetes
- **disclosure**: MiniMed Inc. (later Medtronic Diabetes). 'Continuous Glucose Monitoring System (CGMS)', FDA-cleared June 1999 — the first commercial CGM: a subcutaneous needle-type amperometric glucose sensor coupled to a body-worn recorder logging interstitial-glucose readings for retrospective ('professional') review. (Real-time display followed with the Guardian RT, 2005.)
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses the first commercial continuous glucose monitor: a percutaneous needle-type amperometric glucose sensor in subcutaneous tissue feeding a body-worn recorder that logs interstitial glucose over days for review. Anticipates CGM-system claims combining 'a wearable housing', 'a subcutaneous needle-type enzyme-electrode glucose sensor', and 'logging/transmission of interstitial-glucose readings' from 1999 — a commercial realization of [[shichiri-1982-wearable-needle-glucose-sensor]] (1982). Product-side anchor for the patch × glucose-CGM cross-cut; Dexcom (2006) and Abbott Libre (2014) follow.

## Dexcom STS (2006) — early real-time continuous glucose monitoring system (2006-03)

- **id**: `dexcom-sts-2006`
- **corpus**: private
- **form factor**: patch
- **creator**: DexCom, Inc.
- **disclosure**: DexCom, Inc. 'STS Continuous Glucose Monitoring System', FDA-approved March 2006 — a subcutaneously inserted wire-type amperometric glucose sensor transmitting interstitial-glucose readings every few minutes to a small wireless receiver with trend display and alerts (7-day wear in the successor 'Seven').
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses a real-time CGM: a subcutaneously inserted wire-type amperometric glucose sensor with a body-worn transmitter sending readings every few minutes to a wireless receiver showing the current value, trend arrow, and alerts. Anticipates real-time-CGM claims combining 'a subcutaneous glucose sensor with a wearable transmitter', 'periodic wireless transmission of glucose values', and 'a receiver presenting current value, trend, and threshold alerts' from 2006. Product-side anchor for the patch × glucose-CGM cross-cut alongside [[medtronic-minimed-cgms-1999]].

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

## FDA 510(k) K113862 (~2011) — iRhythm Zio Patch, long-term single-lead adhesive ECG monitor (2011-12)

- **id**: `fda-k113862-irhythm-zio-patch-2011`
- **corpus**: regulatory
- **form factor**: patch
- **creator**: U.S. Food and Drug Administration (CDRH); submitter iRhythm Technologies, Inc.
- **disclosure**: U.S. FDA, 510(k) Premarket Notification K113862 (iRhythm Technologies, Inc., 'Zio Patch') — record at accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K113862; a single-use adhesive chest patch recording a single channel of ECG continuously for up to ~14 days for later analysis, cleared as substantially equivalent to predicate ambulatory-ECG (Holter-class) devices. (Followed by a chain of subsequent iRhythm 510(k)s — e.g. K143513, K163512, K181502 — refining the device, the algorithm/ZEUS software, and the Zio AT mobile-cardiac-telemetry variant.)
- **ip status**: regulatory-filing
- **sensors**: sensor-ecg
- **algorithms**: algo-arrhythmia-classification, algo-afib-detection
- **prior art notes**: A public, dated FDA record of a single-use adhesive chest patch that records one channel of ECG continuously for up to ~14 days for later arrhythmia analysis — the modern 'ECG patch' realization of ambulatory ECG ([[holter-1961-ambulatory-ecg]]). Establishes as of ~2011 the public availability of an adhesive long-wear single-lead ECG patch with downstream automated arrhythmia analysis; and, as a 510(k), it cites a predicate chain back to earlier ambulatory-ECG devices — that chain is itself prior art. Prior art for ECG-patch claims; product-side and regulatory anchor for the patch × ECG cross-cut. Cf. [[apple-watch-series4-ecg-2018]] (the wrist single-lead route).

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

## Bandodkar & Wang (2014) — 'Non-invasive wearable electrochemical sensors: a review' (2014-07)

- **id**: `bandodkar-wang-2014-wearable-electrochemical-sensors-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Amay J. Bandodkar / Joseph Wang (UC San Diego)
- **disclosure**: Bandodkar AJ, Wang J. 'Non-invasive wearable electrochemical sensors: a review.' Trends in Biotechnology 2014;32(7):363-371.
- **ip status**: public-domain
- **sensors**: sensor-lactate, sensor-electrolyte, sensor-ph, sensor-glucose-cgm, sensor-alcohol-transdermal, sensor-uric-acid, sensor-cortisol
- **algorithms**: algo-electrolyte-trend, algo-hydration-status
- **prior art notes**: Surveys, as of 2014, wearable non-invasive electrochemical biosensors across body fluids and form factors — temporary-tattoo electrodes on the skin (sweat lactate, Na+, ammonium, pH), textile-integrated sensors, mouthguard (saliva) sensors, contact-lens (tear glucose) sensors, and the transdermal/interstitial route — including the sampling, transduction, and on-body electronics issues. Prior art for wearable-electrochemical-sensing claims reciting any of the analyte/form-factor combinations collected here; the approaches were published by 2014. General anchor for the electrochemical wearable cross-cuts.

## Abbott FreeStyle Libre (2014) — factory-calibrated flash glucose monitoring (2014-09)

- **id**: `abbott-freestyle-libre-2014`
- **corpus**: private
- **form factor**: patch
- **creator**: Abbott Diabetes Care
- **disclosure**: Abbott Diabetes Care. 'FreeStyle Libre' flash glucose monitoring system, CE-marked / launched in Europe September 2014 (US clearance: FreeStyle Libre Pro 2016; consumer FreeStyle Libre 2017) — a small adhesive coin-sized patch with a subcutaneous wire-type glucose sensor, factory-calibrated (no fingerstick calibration), 14-day wear, read on demand by NFC-scanning the patch with a reader or phone (later 'Libre 2'/'Libre 3' add real-time Bluetooth streaming and alarms).
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses a coin-sized adhesive patch with a subcutaneous wire-type glucose sensor that is factory-calibrated (eliminating fingerstick calibration), worn up to 14 days, and read on demand by NFC-scanning the patch (with later variants adding continuous Bluetooth streaming and threshold alarms). Anticipates flash/CGM claims combining 'a low-profile adhesive patch sensor', 'factory calibration without user blood-glucose calibration', 'extended (≥14-day) wear', and 'on-demand NFC readout' from 2014. Product-side anchor for the patch × glucose-CGM cross-cut.

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

## Mukkamala et al. (2015) — 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice' (2015-08)

- **id**: `mukkamala-2015-ptt-cuffless-bp-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Ramakrishna Mukkamala et al.
- **disclosure**: Mukkamala R, Hahn J-O, Inan OT, Mestha LK, Kim C-S, Töreyin H, Kyal S. 'Toward Ubiquitous Blood Pressure Monitoring via Pulse Transit Time: Theory and Practice.' IEEE Transactions on Biomedical Engineering 2015;62(8):1879-1901.
- **ip status**: public-domain
- **sensors**: sensor-ecg, sensor-ppg, sensor-cuffless-bp-ptt, sensor-cuffless-bp-tonometry
- **algorithms**: algo-pwv-bp-estimation
- **prior art notes**: Canonical 2015 review of cuffless blood-pressure estimation by pulse transit time / pulse arrival time / pulse wave velocity: the physiological models, the practical sensor configurations (ECG+PPG, dual PPG, ballistocardiogram+PPG), the calibration strategies, and the accuracy limitations. Prior art for cuffless-BP wearable claims reciting any of the configurations or calibration approaches surveyed here — they were collected, modeled, and published by 2015. Combined with watch/ring/patch form-factor disclosures, makes wearable PTT-based BP an obvious combination under [[obviousness-template]].

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

## VitalConnect VitalPatch (2016) — adhesive chest patch with single-lead ECG and multi-parameter monitoring (2016)

- **id**: `vitalconnect-vitalpatch-2016`
- **corpus**: private
- **form factor**: patch
- **creator**: VitalConnect, Inc.
- **disclosure**: VitalConnect, Inc. 'VitalPatch' biosensor, FDA-cleared as a single-use adhesive chest patch with single-lead ECG, heart rate, heart-rate variability, respiratory rate, skin temperature, posture, activity, and fall detection, streamed wirelessly to a smartphone/relay; 7-day wear (later 14-day variants).
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature
- **algorithms**: algo-hr, algo-hrv, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-arrhythmia-classification
- **prior art notes**: Discloses a single-use adhesive chest patch deriving single-lead ECG, HR, HRV, respiratory rate, skin temperature, posture, activity, and falls in one body-worn unit, streamed wirelessly — i.e. a packed multi-parameter vital-signs patch. Anticipates multi-parameter ECG-patch claims combining any subset of those measurements in one adhesive form factor from 2016. Product-side anchor for the patch × multi-parameter-vitals cross-cut alongside [[fda-k113862-irhythm-zio-patch-2011]] (the AFib-focused variant).

## Gao et al. (Javey group) (2016) — fully integrated wearable sensor array for multiplexed in-situ perspiration analysis (2016-01-28)

- **id**: `gao-javey-2016-wearable-sweat-sensor-array`
- **corpus**: academic
- **form factor**: headband
- **creator**: Wei Gao et al. / Ali Javey group (UC Berkeley)
- **disclosure**: Gao W, Emaminejad S, Nyein HYY, Challa S, Chen K, Peck A, et al. (Javey A). 'Fully integrated wearable sensor arrays for multiplexed in situ perspiration analysis.' Nature 2016;529(7587):509-514.
- **ip status**: public-domain
- **sensors**: sensor-lactate, sensor-glucose-cgm, sensor-electrolyte, sensor-ph, sensor-skin-temperature, sensor-microfluidic-sweat-collection
- **algorithms**: algo-electrolyte-trend, algo-hydration-status
- **prior art notes**: Discloses a fully integrated wearable (wristband / headband) with an array of electrochemical sensors measuring multiple sweat analytes simultaneously (glucose, lactate, Na+, K+) plus skin temperature for real-time signal compensation, with on-board signal conditioning, microcontroller, and wireless transmission to a phone — i.e. a complete in-situ sweat biochemistry monitor. Any wearable claim reciting 'a band-form device with an array of two or more electrochemical sweat-analyte sensors plus a temperature sensor for compensation, with integrated electronics and wireless output' reads on Gao/Javey 2016. Anchor for the sweat-electrochemical-sensing cross-cuts on the real side; [[bandodkar-wang-2014-wearable-electrochemical-sensors-review]] is the contemporaneous review.

## Koh et al. (Rogers group) (2016) — soft wearable microfluidic device for sweat capture, storage, and colorimetric sensing (2016-11-23)

- **id**: `koh-rogers-2016-soft-microfluidic-sweat-device`
- **corpus**: academic
- **form factor**: patch
- **creator**: Ahyeon Koh et al. / John A. Rogers group (Northwestern)
- **disclosure**: Koh A, Kang D, Xue Y, Lee S, Pielak RM, Kim J, et al. (Rogers JA). 'A soft, wearable microfluidic device for the capture, storage, and colorimetric sensing of sweat.' Science Translational Medicine 2016;8(366):366ra165.
- **ip status**: public-domain
- **sensors**: sensor-microfluidic-sweat-collection, sensor-sweat-rate, sensor-ph, sensor-lactate, sensor-electrolyte, sensor-glucose-cgm
- **algorithms**: algo-hydration-status, algo-electrolyte-trend
- **prior art notes**: Discloses a soft, skin-mounted microfluidic 'sticker' that wicks sweat from the skin into a network of microchannels and reservoirs, measures sweat rate and total sweat loss, and performs colorimetric assays (pH, chloride, lactate, glucose) read out by eye or smartphone camera. Any wearable claim reciting 'a skin-mounted patch with microfluidic channels collecting perspiration' combined with 'rate measurement' and/or 'colorimetric or electrochemical analysis of constituents' reads on Koh/Rogers 2016. Anchor for the patch × microfluidic-sweat-collection cross-cut on the real side; [[dune-stillsuit]] (1965) is the fictional antecedent.

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

## Abilify MyCite (Otsuka / Proteus Digital Health, 2017) — first FDA-approved drug with an ingestible sensor (digital-pill / medication-adherence system) (2017-11-14)

- **id**: `proteus-abilify-mycite-2017`
- **corpus**: private
- **form factor**: ingestible
- **creator**: Otsuka Pharmaceutical Co. / Proteus Digital Health, Inc.
- **disclosure**: Otsuka Pharmaceutical Co., Ltd. and Proteus Digital Health, Inc. 'Abilify MyCite' (aripiprazole with embedded ingestible event marker), FDA-approved 13 November 2017 — the first drug-device combination approved by the FDA with an integrated ingestible sensor: a millimeter-scale sensor embedded in each tablet that activates on contact with stomach fluid and transmits to a skin-worn patch ('MyCite Patch'), which relays an ingestion event to a smartphone, confirming medication adherence.
- **ip status**: patented
- **sensors**: sensor-bioimpedance
- **prior art notes**: Discloses a drug-device combination in which each medication tablet incorporates a tiny edible sensor that activates on contact with stomach fluid (powered by the electrochemical reaction with stomach acid), communicating an ingestion event to a skin-mounted receiver patch that relays it to a smartphone. The first FDA-approved digital-pill / medication-adherence-tracking system. Anticipates ingestible-sensor medication-adherence claims combining 'an ingestible sensor embedded in or co-delivered with a pharmaceutical', 'a skin-worn receiver/patch', and 'transmission of an ingestion-event record' from 2017. Anchor for the ingestible × adherence cross-cut.

## Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects' (2018-01-16)

- **id**: `heikenfeld-2018-wearable-sensors-lab-on-chip-review`
- **corpus**: academic
- **form factor**: other
- **creator**: Jason Heikenfeld et al.
- **disclosure**: Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.
- **ip status**: public-domain
- **sensors**: sensor-ppg, sensor-ecg, sensor-eeg, sensor-glucose-cgm, sensor-lactate, sensor-cortisol, sensor-skin-temperature, sensor-bioimpedance
- **prior art notes**: Authoritative 2018 review collecting wearable sensing across modalities — physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, tears, interstitial), and stimulation-coupled — across form factors (patch, watch, tattoo, contact lens, garment) and the challenges of body-fluid sampling, calibration, motion-artifact handling, and skin-electronics interfacing. Prior art establishing that the modality/form-factor combinations enumerated here were collected and surveyed by 2018; useful against later claims to those combinations. General anchor.

## Dexcom G6 (2018) — no-calibration real-time CGM with predictive low-glucose alert and direct phone streaming (2018-03)

- **id**: `dexcom-g6-2018`
- **corpus**: private
- **form factor**: patch
- **creator**: DexCom, Inc.
- **disclosure**: DexCom, Inc. 'Dexcom G6 Continuous Glucose Monitoring System', FDA-cleared March 2018 — a subcutaneous wire-type glucose sensor with a low-profile on-skin transmitter, factory-calibrated (no fingerstick calibration), 10-day wear, 5-minute readings streamed directly to a phone or receiver, with customizable alerts and a predictive 'urgent low soon' alarm; the successor Dexcom G7 (2022) is smaller with a faster warm-up.
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses a real-time CGM that is factory-calibrated (no user blood-glucose calibration), worn 10 days, streams 5-minute glucose values directly to a phone, and provides a predictive low-glucose alert ('urgent low soon') in addition to threshold and rate alarms. Anticipates CGM claims reciting 'factory calibration without user calibration', 'direct streaming to a general-purpose mobile device', and 'a predictive (forecast-based) hypoglycemia alert' from 2018. Product-side anchor for the patch × glucose-CGM cross-cut alongside [[abbott-freestyle-libre-2014]].

## FDA De Novo (2018) — 'integrated continuous glucose monitoring system' (iCGM) classification (Dexcom G6) (2018-03-27)

- **id**: `fda-den170088-dexcom-icgm-2018`
- **corpus**: regulatory
- **form factor**: patch
- **creator**: U.S. Food and Drug Administration (CDRH); requester Dexcom, Inc.
- **disclosure**: U.S. FDA, De Novo classification (Dexcom, Inc., 'Dexcom G6 Continuous Glucose Monitoring System'), granted March 2018 — established the new device class 'integrated continuous glucose monitoring system' (iCGM): a CGM intended to reliably and securely transmit glucose data to digitally-connected devices (e.g. automated insulin-dosing systems), with stringent accuracy special controls; reportedly DEN170088 (verify against the FDA De Novo database).
- **ip status**: regulatory-filing
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: A public, dated FDA decision creating the 'integrated CGM' device class — a continuous glucose monitor designed to interoperate (transmit glucose data) with other devices such as automated insulin pumps, under defined accuracy and security special controls. Establishes as of 2018 the public availability of an interoperable, factory-calibrated real-time CGM intended as a component of a connected diabetes-management system. Prior art for CGM-interoperability and connected-CGM claims; regulatory anchor pairing with [[dexcom-g6-2018]] and [[shichiri-1982-wearable-needle-glucose-sensor]].

## Senseonics Eversense (2018) — first long-term implantable continuous glucose monitor (fluorescence sensor + on-skin transmitter) (2018-06)

- **id**: `eversense-implantable-cgm-2018`
- **corpus**: private
- **form factor**: implantable
- **creator**: Senseonics, Inc.
- **disclosure**: Senseonics, Inc. 'Eversense Continuous Glucose Monitoring System', FDA-approved June 2018 (CE-marked earlier) — a small fluorescence-based glucose sensor implanted subcutaneously in the upper arm for 90 days (later 180+ days), read by a removable transmitter worn on the skin over it that powers the sensor inductively, computes glucose, and streams it to a phone with on-body vibratory alerts.
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses a long-term (months) implantable glucose sensor — a fluorescence-chemistry sensor implanted subcutaneously — paired with a removable on-skin transmitter that inductively powers and reads the sensor, derives glucose, streams it wirelessly, and gives on-body vibratory alerts. Distinct from the needle/wire-type CGMs ([[shichiri-1982-wearable-needle-glucose-sensor]], [[dexcom-sts-2006]], [[abbott-freestyle-libre-2014]]): a fully implanted, wirelessly-powered, fluorescence-based long-term sensor with a separable wearable reader. Anticipates implantable-CGM claims reciting that architecture from 2018. Product-side anchor for the implantable × glucose-CGM cross-cut.

## Abbott FreeStyle Libre 2 (2018) — factory-calibrated CGM patch with real-time Bluetooth streaming and optional glucose alarms (2018-10)

- **id**: `abbott-freestyle-libre-2-2018`
- **corpus**: private
- **form factor**: patch
- **creator**: Abbott Diabetes Care
- **disclosure**: Abbott Diabetes Care. 'FreeStyle Libre 2', CE-marked October 2018 (US clearance 2020) — the FreeStyle Libre patch sensor (coin-sized adhesive, subcutaneous wire-type sensor, factory-calibrated, 14-day wear) augmented with continuous Bluetooth transmission to the reader/phone and optional real-time high/low/signal-loss glucose alarms (no scan required for alerts); FreeStyle Libre 3 (2020-2022) is smaller with continuous minute-by-minute streaming.
- **ip status**: patented
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-cgm-readout
- **prior art notes**: Discloses the small adhesive factory-calibrated CGM patch (14-day, subcutaneous wire sensor) extended with continuous Bluetooth transmission and optional real-time glucose alarms without requiring a scan — closing the gap to alarm-capable real-time CGM at a low-profile patch form factor. Anticipates patch-CGM claims reciting 'a factory-calibrated adhesive patch sensor with continuous wireless streaming and configurable real-time alarms' from 2018. Product-side anchor for the patch × glucose-CGM cross-cut.

## BioIntelliSense BioSticker (2019) — long-wear adhesive chest patch with extensive multi-parameter monitoring (2019-12)

- **id**: `biointellisense-biosticker-2019`
- **corpus**: private
- **form factor**: patch
- **creator**: BioIntelliSense, Inc.
- **disclosure**: BioIntelliSense, Inc. 'BioSticker' single-use adhesive medical-grade biosensor, FDA-cleared 2019 — a chest patch with up to 30-day wear continuously measuring skin temperature, single-lead ECG-derived heart rate at rest, respiratory rate at rest, body position, activity (steps, cadence, gait), sleep, cough, vomiting events, and falls, with wireless upload.
- **ip status**: patented
- **sensors**: sensor-ecg, sensor-accelerometer, sensor-skin-temperature, sensor-microphone-air
- **algorithms**: algo-hr, algo-respiratory-rate, algo-activity-classification, algo-posture-detection, algo-fall-detection, algo-cough-detection, algo-gait-analysis, algo-sleep-staging
- **prior art notes**: Discloses a single-use 30-day adhesive chest patch combining skin temperature, resting HR-from-ECG, resting RR, posture/activity, sleep, cough and vomiting event detection, and falls — i.e. an unusually broad multi-parameter long-wear patch with explicit event-detection (cough, vomit) classifiers. Anticipates long-wear multi-parameter patch claims from 2019, including the event-detection (cough/vomit) elements that some later patents recite. Product-side anchor for the patch × long-wear multi-parameter cross-cut.
