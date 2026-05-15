---
title: sensor-glucose-cgm
parent: Cross-cuts
layout: default
---

# Cross-cut: `sensor-glucose-cgm`

Axis: **sensors**

**18 corpus entries disclose this tag.**

Earliest disclosure: 1962

Listed in chronological order. Each entry's `prior_art_notes` and
`disclosure_citation` constitute the citeable prior art material.

---

## Clark & Lyons (1962) — the enzyme electrode (basis of the amperometric glucose biosensor) (1962)

- **id**: `clark-lyons-1962-enzyme-electrode`
- **corpus**: academic
- **form factor**: other
- **creator**: Leland C. Clark Jr. / Champ Lyons
- **disclosure**: Clark LC Jr, Lyons C. 'Electrode systems for continuous monitoring in cardiovascular surgery.' Annals of the New York Academy of Sciences 1962;102(1):29-45.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm
- **prior art notes**: Proposes coupling an enzyme (glucose oxidase) to an oxygen electrode so that the electrode current reports glucose concentration — the founding concept of the amperometric enzyme biosensor and hence of every electrochemical continuous glucose monitor. Any CGM claim reciting 'an enzyme electrode configured to generate a current dependent on glucose concentration' rests on a concept public since 1962. § 102 prior art for the electrochemical-glucose-sensing principle.

## Updike & Hicks (1967) — the practical glucose enzyme electrode (1967-06-03)

- **id**: `updike-hicks-1967-enzyme-electrode`
- **corpus**: academic
- **form factor**: other
- **creator**: Stuart J. Updike / George P. Hicks
- **disclosure**: Updike SJ, Hicks GP. 'The enzyme electrode.' Nature 1967;214(5092):986-988.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm
- **prior art notes**: Reduces Clark & Lyons's concept to a working device — an immobilized-enzyme membrane on an electrode giving a glucose-dependent signal — the practical ancestor of the implantable/subcutaneous glucose sensor. Prior art for CGM claims reciting 'a membrane-immobilized glucose oxidase layer on an electrode'. Combined with [[shichiri-1982-wearable-needle-glucose-sensor]] it establishes both the chemistry and the wearable form.

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

## Yao et al. (Parviz group) (2011) — contact lens with embedded electrochemical sensor for tear glucose (2011-03-15)

- **id**: `yao-parviz-2011-contact-lens-glucose-sensor`
- **corpus**: academic
- **form factor**: contact-lens
- **creator**: Hung Yao / Babak A. Parviz et al. (University of Washington)
- **disclosure**: Yao H, Shum AJ, Cowan M, Lähdesmäki I, Parviz BA. 'A contact lens with embedded sensor for monitoring tear glucose level.' Biosensors and Bioelectronics 2011;26(7):3290-3296.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm, sensor-optical-glucose
- **algorithms**: algo-glucose-noninvasive
- **prior art notes**: Discloses a soft contact lens with an embedded amperometric glucose-oxidase electrochemical sensor and integrated interconnects to measure glucose in the tear film — a corneal-contact noninvasive glucose monitor. Anticipates contact-lens biosensor claims combining 'a soft ophthalmic contact lens', 'an embedded electrochemical sensor at the lens surface', and 'detection of an analyte in the tear film (glucose)' from 2011. Anchor for the contact-lens × biosensor cross-cut on the real side; relevant to [[rainbows-end-ar-contact-lens]] (the fictional AR-lens antecedent) and to the Google/Verily 'smart contact lens' patent estate.

## Google[X] / Verily smart contact lens (2014) — tear-glucose-sensing contact lens project (2014-01-16)

- **id**: `verily-google-smart-contact-lens-2014`
- **corpus**: private
- **form factor**: contact-lens
- **creator**: Google[X] / Verily Life Sciences (Brian Otis, Babak Parviz, et al.)
- **disclosure**: Google[X] (Brian Otis, Babak Parviz). 'Smart contact lens' project, publicly disclosed 16 January 2014 — a soft contact lens with an embedded miniature glucose sensor, antenna, and wireless interface to a phone, intended to continuously measure tear glucose. Later transferred to Verily (Alphabet's life-sciences arm) and licensed to Novartis/Alcon; the program was reported wound down c. 2018 without a shipping product, but the underlying patent estate (Otis et al., Parviz et al.; e.g. US 8,608,310; US 9,184,698 and continuations) is extensive.
- **ip status**: patented
- **sensors**: sensor-glucose-cgm, sensor-optical-glucose
- **algorithms**: algo-glucose-noninvasive
- **prior art notes**: Discloses a soft contact lens with an embedded miniature electrochemical glucose sensor, antenna, and wireless interface for continuous tear-glucose monitoring — a major industrial follow-on to [[yao-parviz-2011-contact-lens-glucose-sensor]]. Anticipates smart-contact-lens claims combining 'a soft ophthalmic lens', 'an embedded biosensor', and 'wireless transmission of the sensed analyte' from 2014; the extensive associated patent family is itself prior art on most subsequent contact-lens-biosensor and embedded-lens-electronics claims. Product-side anchor for the contact-lens × biosensor cross-cut.

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

## Bandodkar et al. (2015) — tattoo-based noninvasive glucose monitoring (2014-12-12)

- **id**: `bandodkar-2015-tattoo-glucose-sensor`
- **corpus**: academic
- **form factor**: tattoo-electronic
- **creator**: Amay J. Bandodkar / Joseph Wang group (UC San Diego)
- **disclosure**: Bandodkar AJ, Jia W, Yardımcı C, Wang X, Ramirez J, Wang J. 'Tattoo-based noninvasive glucose monitoring: a proof-of-concept study.' Analytical Chemistry 2015;87(1):394-398.
- **ip status**: public-domain
- **sensors**: sensor-glucose-cgm
- **algorithms**: algo-glucose-noninvasive
- **prior art notes**: Discloses a temporary-tattoo-format epidermal device that uses reverse iontophoresis to extract interstitial fluid through the skin and amperometric enzyme electrodes to measure glucose in it, demonstrating noninvasive transdermal glucose monitoring without a needle. Anticipates noninvasive-CGM claims combining 'a skin-mounted tattoo/epidermal patch', 'iontophoretic extraction of interstitial fluid', and 'electrochemical glucose measurement at the skin surface' from 2015. Anchor for the tattoo-electronic × glucose-CGM cross-cut on the real side; relevant to [[koh-rogers-2016-soft-microfluidic-sweat-device]] and the broader [[bandodkar-wang-2014-wearable-electrochemical-sensors-review]].

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
