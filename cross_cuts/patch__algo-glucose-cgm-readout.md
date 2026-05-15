---
title: patch ∩ algo-glucose-cgm-readout
parent: Cross-cuts
layout: default
---

# Intersection cross-cut: `patch` ∩ `algo-glucose-cgm-readout`

Axes: **form_factor × algorithms**

**8 corpus entries disclose both tags.**

Earliest disclosure: 1982-11-20

These entries are the direct inputs to [OBVIOUSNESS_TEMPLATE.md](../OBVIOUSNESS_TEMPLATE.html). Any patent claim combining these two elements is anticipated or rendered obvious by the chain below.

---

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
