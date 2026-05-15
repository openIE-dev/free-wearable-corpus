#!/usr/bin/env python3
"""seed_2026q3_real_r6_academic.py — more academic foundations.

Ballistocardiography / seismocardiography; tattoo-electronic and contact-
lens glucose biosensors; the WEALTHY knitted-textile smart shirt; the
Heikenfeld broad wearable-sensors review.

Run from repo root:  python3 seeds/seed_2026q3_real_r6_academic.py
Idempotent — skips ids already present.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("corpus", "academic")
    kw.setdefault("ip_status", "public-domain")
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    E(
        id="inan-2015-bcg-scg-review",
        canonical_name="Inan et al. (2015) — ballistocardiography and seismocardiography review",
        aliases=["BCG SCG review", "Inan ballistocardiography"],
        first_disclosure_date="2015-07",
        disclosure_citation="Inan OT, Migeotte P-F, Park K-S, Etemadi M, Tavakolian K, Casanella R, Zanetti J, Tank J, Funtova I, Prisk GK, Di Rienzo M. 'Ballistocardiography and seismocardiography: a review of recent advances.' IEEE Journal of Biomedical and Health Informatics 2015;19(4):1414-1427.",
        creator="Omer T. Inan et al.",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["patch", "garment", "watch"],
        contact_surface="skin",
        sensors=["sensor-accelerometer", "sensor-piezoelectric"],
        algorithms=["algo-hr", "algo-hrv", "algo-pwv-bp-estimation"],
        clinical_endpoints=["heart-rate", "stroke-volume", "cardiac-mechanics"],
        prior_art_notes=(
            "Reviews ballistocardiography (whole-body reaction force from cardiac "
            "ejection, measured at the seat/scale/bed) and seismocardiography (local "
            "chest vibration from cardiac motion, measured by accelerometers on the "
            "sternum) and their integration into bathroom scales, weighing chairs, beds, "
            "and chest patches — i.e. the mechanical-cardiac-signal route to heart rate, "
            "HRV, and cardiac-timing-interval / stroke-volume estimation. Prior art for "
            "claims reciting 'measuring cardiac activity from a body-worn or "
            "support-mounted accelerometer/force sensor', as both the BCG and SCG "
            "approaches and their wearable instantiations were collected and reviewed by "
            "2015. Anchor for the BCG/SCG cross-cut."
        ),
        sources=["Inan OT, et al. IEEE J Biomed Health Inform 2015;19(4):1414-1427."],
        cpc_classifications=["A61B 5/11", "A61B 5/02", "A61B 5/1102", "A61B 7/04"],
    ),
    E(
        id="bandodkar-2015-tattoo-glucose-sensor",
        canonical_name="Bandodkar et al. (2015) — tattoo-based noninvasive glucose monitoring",
        aliases=["tattoo glucose sensor", "iontophoretic tattoo glucose"],
        first_disclosure_date="2015-01-06",
        disclosure_citation="Bandodkar AJ, Jia W, Yardımcı C, Wang X, Ramirez J, Wang J. 'Tattoo-based noninvasive glucose monitoring: a proof-of-concept study.' Analytical Chemistry 2015;87(1):394-398.",
        creator="Amay J. Bandodkar / Joseph Wang group (UC San Diego)",
        creator_country="US",
        form_factor="tattoo-electronic",
        contact_surface="skin",
        anatomical_target=["skin"],
        sensors=["sensor-glucose-cgm"],
        algorithms=["algo-glucose-noninvasive"],
        clinical_endpoints=["interstitial-glucose"],
        prior_art_notes=(
            "Discloses a temporary-tattoo-format epidermal device that uses reverse "
            "iontophoresis to extract interstitial fluid through the skin and amperometric "
            "enzyme electrodes to measure glucose in it, demonstrating noninvasive "
            "transdermal glucose monitoring without a needle. Anticipates "
            "noninvasive-CGM claims combining 'a skin-mounted tattoo/epidermal patch', "
            "'iontophoretic extraction of interstitial fluid', and 'electrochemical "
            "glucose measurement at the skin surface' from 2015. Anchor for the "
            "tattoo-electronic × glucose-CGM cross-cut on the real side; relevant to "
            "[[koh-rogers-2016-soft-microfluidic-sweat-device]] and the broader "
            "[[bandodkar-wang-2014-wearable-electrochemical-sensors-review]]."
        ),
        sources=["Bandodkar AJ, et al. Anal Chem 2015;87(1):394-398."],
        cpc_classifications=["A61B 5/14532", "A61B 5/14517", "A61B 5/14507", "A61N 1/0428"],
    ),
    E(
        id="yao-parviz-2011-contact-lens-glucose-sensor",
        canonical_name="Yao et al. (Parviz group) (2011) — contact lens with embedded electrochemical sensor for tear glucose",
        aliases=["contact lens glucose sensor", "Parviz contact lens", "tear glucose lens"],
        first_disclosure_date="2011-03-15",
        disclosure_citation="Yao H, Shum AJ, Cowan M, Lähdesmäki I, Parviz BA. 'A contact lens with embedded sensor for monitoring tear glucose level.' Biosensors and Bioelectronics 2011;26(7):3290-3296.",
        creator="Hung Yao / Babak A. Parviz et al. (University of Washington)",
        creator_country="US",
        form_factor="contact-lens",
        contact_surface="ocular",
        anatomical_target=["cornea", "tear-film"],
        sensors=["sensor-glucose-cgm", "sensor-optical-glucose"],
        algorithms=["algo-glucose-noninvasive"],
        clinical_endpoints=["tear-glucose"],
        prior_art_notes=(
            "Discloses a soft contact lens with an embedded amperometric "
            "glucose-oxidase electrochemical sensor and integrated interconnects to "
            "measure glucose in the tear film — a corneal-contact noninvasive glucose "
            "monitor. Anticipates contact-lens biosensor claims combining 'a soft "
            "ophthalmic contact lens', 'an embedded electrochemical sensor at the lens "
            "surface', and 'detection of an analyte in the tear film (glucose)' from "
            "2011. Anchor for the contact-lens × biosensor cross-cut on the real side; "
            "relevant to [[rainbows-end-ar-contact-lens]] (the fictional AR-lens "
            "antecedent) and to the Google/Verily 'smart contact lens' patent estate."
        ),
        sources=["Yao H, et al. Biosens Bioelectron 2011;26(7):3290-3296."],
        cpc_classifications=["A61B 5/14532", "G02C 7/04", "A61B 5/1455", "G01N 33/487"],
    ),
    E(
        id="heikenfeld-2018-wearable-sensors-lab-on-chip-review",
        canonical_name="Heikenfeld et al. (2018) — 'Wearable sensors: modalities, challenges, and prospects'",
        aliases=["Heikenfeld wearable sensors review", "wearable sensors Lab on a Chip 2018"],
        first_disclosure_date="2018-01-21",
        disclosure_citation="Heikenfeld J, Jajack A, Rogers J, Gutruf P, Tian L, Pan T, Li R, Khine M, Kim J, Wang J, Kim J. 'Wearable sensors: modalities, challenges, and prospects.' Lab on a Chip 2018;18(2):217-248.",
        creator="Jason Heikenfeld et al.",
        creator_country="US",
        form_factor="other",
        form_factor_tags=["patch", "watch", "tattoo-electronic", "contact-lens", "garment", "ring"],
        contact_surface="skin",
        sensors=["sensor-ppg", "sensor-ecg", "sensor-eeg", "sensor-glucose-cgm", "sensor-lactate", "sensor-cortisol", "sensor-skin-temperature", "sensor-bioimpedance"],
        clinical_endpoints=["multi-analyte"],
        prior_art_notes=(
            "Authoritative 2018 review collecting wearable sensing across modalities — "
            "physical (motion, BCG/SCG, mechanoacoustic), electrophysiological (ECG/EMG/"
            "EEG), optical (PPG/SpO2, near-IR), thermal, electrochemical (sweat, saliva, "
            "tears, interstitial), and stimulation-coupled — across form factors (patch, "
            "watch, tattoo, contact lens, garment) and the challenges of body-fluid "
            "sampling, calibration, motion-artifact handling, and skin-electronics "
            "interfacing. Prior art establishing that the modality/form-factor "
            "combinations enumerated here were collected and surveyed by 2018; useful "
            "against later claims to those combinations. General anchor."
        ),
        sources=["Heikenfeld J, et al. Lab Chip 2018;18(2):217-248."],
        cpc_classifications=["A61B 5/00", "A61B 5/0006", "A61B 5/1486", "A61B 5/02416"],
    ),
    E(
        id="paradiso-2005-wealthy-knitted-smart-shirt",
        canonical_name="Paradiso et al. (2005) — 'A wearable health care system based on knitted integrated sensors' (WEALTHY)",
        aliases=["WEALTHY smart shirt", "knitted ECG shirt", "Paradiso textile electrodes"],
        first_disclosure_date="2005-09",
        disclosure_citation="Paradiso R, Loriga G, Taccini N. 'A wearable health care system based on knitted integrated sensors.' IEEE Transactions on Information Technology in Biomedicine 2005;9(3):337-344. (Output of the EU FP5 'WEALTHY' project, 2002-2005.)",
        creator="Rita Paradiso / Giannicola Loriga / Nicola Taccini (Smartex / CNR, Italy; EU WEALTHY consortium)",
        creator_country="IT",
        form_factor="garment",
        contact_surface="skin",
        anatomical_target=["chest", "torso"],
        sensors=["sensor-ecg", "sensor-respiration-impedance", "sensor-piezoelectric", "sensor-accelerometer", "sensor-skin-temperature"],
        algorithms=["algo-hr", "algo-respiratory-rate", "algo-activity-classification"],
        clinical_endpoints=["electrocardiogram", "respiration", "skin-temperature", "activity"],
        prior_art_notes=(
            "Discloses a smart shirt with electrodes and sensors knitted directly into "
            "the textile (conductive yarns forming dry ECG electrodes; piezoresistive "
            "yarns forming respiration sensors via thoracic/abdominal expansion; "
            "accelerometer; temperature) plus an on-garment electronic interface and "
            "wireless link, deriving ECG, heart rate, respiration, posture/activity, and "
            "temperature — i.e. a fully integrated textile-electrode wearable. Any claim "
            "reciting 'an item of clothing with electrodes/sensors integrated into the "
            "fabric structure for physiological monitoring' reads on Paradiso 2005. "
            "Anchor for the garment × textile-electrode cross-cut; the foundational EU "
            "project for the smart-shirt patent space (Hexoskin, Cityzen, etc. all "
            "build on this lineage)."
        ),
        sources=["Paradiso R, Loriga G, Taccini N. IEEE Trans Inf Technol Biomed 2005;9(3):337-344."],
        cpc_classifications=["A61B 5/0205", "A61B 5/259", "A41D 1/00", "A61B 5/02438"],
    ),
]


def main():
    existing = set()
    if CORPUS.exists() and CORPUS.stat().st_size:
        for line in CORPUS.read_text().splitlines():
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])
    added = skipped = 0
    with CORPUS.open("a") as f:
        for e in ENTRIES:
            if e["id"] in existing:
                skipped += 1
                continue
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
            added += 1
    print(f"  real academic r6: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
