#!/usr/bin/env python3
"""seed_2026q3_fiction_r10.py — fictional seed batch round 10 (video games).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r10.py
Idempotent — skips ids already present.

Doctrinal note: fictional disclosures are generally non-enabling; their
prior-art value is § 103 motivation-to-combine.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"
LAST_UPDATED = "2026-05-11"


def E(**kw):
    kw.setdefault("schema_version", 1)
    kw.setdefault("tier", 1)
    kw.setdefault("corpus", "fictional")
    kw.setdefault("ip_status", "fictional")
    kw.setdefault("last_updated", LAST_UPDATED)
    return kw


ENTRIES = [
    E(
        id="metroid-power-suit",
        canonical_name="Metroid — Samus Aran's Power Suit (powered armor with multi-mode scan visor and health/environment systems)",
        aliases=["Power Suit", "Varia Suit", "Samus suit", "Metroid Prime visor"],
        first_disclosure_date="1986-08-06",
        disclosure_citation="Metroid (Nintendo, released 6 August 1986; multi-mode visor system in Metroid Prime, 2002); a fully enclosing powered armored suit with a head-up display, switchable visor modes (combat, scan/analysis, thermal, X-ray), an integrated arm-mounted tool, energy reserves indicating health, and environmental adaptation modules (heat resistance, pressure sealing).",
        creator="Nintendo R&D1 / Retro Studios",
        creator_country="JP",
        form_factor="exoskeleton",
        form_factor_tags=["helmet", "goggles"],
        contact_surface="skin",
        anatomical_target=["whole-body", "eyes"],
        sensors=["sensor-camera-thermal", "sensor-camera-ir"],
        clinical_endpoints=["energy-reserve"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a powered enclosing suit with a HUD, user-selectable visor modes "
            "(combat, scanning/analysis of objects in view, thermal, see-through), an "
            "integrated tool, an energy/health reserve indicator, and swappable "
            "environmental-protection modules. Relevant to powered-suit claims combining "
            "'a HUD with multiple selectable imaging/analysis modes', 'an integrated "
            "status reserve indicator', and 'environmental-adaptation modules'. § 103 "
            "motivation as of 1986 (multi-mode scan visor as of 2002). Cf. "
            "[[heinlein-starship-troopers-powered-armor]], [[halo-mjolnir-armor]], "
            "[[splinter-cell-trifocal-goggles]]."
        ),
        sources=[
            "Metroid. Nintendo, 1986.",
            "Metroid Prime. Nintendo / Retro Studios, 2002.",
        ],
        cpc_classifications=["G02B 27/01", "A61H 3/00", "H04N 5/33", "G06V 20/20"],
    ),
    E(
        id="fallout-pip-boy",
        canonical_name="Fallout — the 'Pip-Boy' (forearm-worn personal computer with multi-parameter health and radiation monitoring)",
        aliases=["Pip-Boy", "Pip-Boy 3000", "Pipboy"],
        first_disclosure_date="1997-10-10",
        disclosure_citation="Fallout (Interplay, released 10 October 1997; the wrist/forearm-worn 'Pip-Boy' device); a forearm-mounted personal computer with a display showing the wearer's overall and limb-by-limb health, radiation exposure dose ('rads'), addiction/affliction status, plus inventory, local and world maps with positioning, a radio receiver, and a clock.",
        creator="Interplay / Black Isle Studios",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["armband"],
        contact_surface="skin",
        anatomical_target=["forearm", "wrist"],
        sensors=["sensor-uv"],
        clinical_endpoints=["limb-condition", "radiation-dose", "affliction-status"],
        algorithms=["algo-uv-dose-tracking"],
        output_modalities=["visual-display", "audio"],
        connectivity="radio (fictional)",
        prior_art_notes=(
            "Discloses a forearm-worn personal computer that continuously displays the "
            "wearer's health (overall and per-limb), accumulated radiation dose, and "
            "affliction status, alongside maps with positioning, a radio, an inventory, "
            "and a clock. Relevant to wrist/forearm-worn-monitor claims combining 'a "
            "body-worn display device', 'continuous multi-parameter physiological/exposure "
            "monitoring (including ionizing-radiation dosimetry)', 'mapping with "
            "positioning', and 'a media receiver'. § 103 motivation that the forearm-worn "
            "multi-parameter health/dosimetry computer was an articulated objective by "
            "1997. Cf. [[inspector-gadget-wrist-computer]], [[pokemon-poketch]]."
        ),
        sources=["Fallout. Interplay Productions, 1997."],
        cpc_classifications=["A61B 5/00", "G01T 1/02", "G04G 21/04", "G06F 1/163"],
    ),
    E(
        id="halo-mjolnir-armor",
        canonical_name="Halo — MJOLNIR powered armor (powered exoskeleton with energy shield, HUD, integrated AI, and biofoam medical system)",
        aliases=["MJOLNIR armor", "Spartan armor", "Mjolnir"],
        first_disclosure_date="2001-11-15",
        disclosure_citation="Halo: Combat Evolved (Bungie / Microsoft, released 15 November 2001); the MJOLNIR powered armor — strength/speed augmentation, a regenerating energy shield with a status meter, a HUD (motion tracker, ammunition, shield/health status, waypoints), an integrated companion AI ('Cortana') resident in the suit, automatic 'biofoam' wound sealing, vacuum/environmental sealing, and a neural interface to the wearer.",
        creator="Bungie Studios / Microsoft",
        creator_country="US",
        form_factor="exoskeleton",
        form_factor_tags=["helmet"],
        contact_surface="skin",
        anatomical_target=["whole-body", "skull", "eyes"],
        sensors=["sensor-accelerometer"],
        clinical_endpoints=["health-status", "shield-status", "vitals"],
        output_modalities=["visual-display", "audio", "data-only", "drug-delivery"],
        prior_art_notes=(
            "Discloses a powered enclosing suit integrating strength augmentation, a "
            "regenerating defensive field with a status indicator, a HUD (motion tracker, "
            "resource counters, health/shield meters, navigation waypoints), an on-board "
            "companion AI, automatic medical wound-sealing, environmental sealing, and a "
            "neural interface. Relevant to powered-armor claims combining 'a HUD with "
            "health/resource/navigation overlays', 'an onboard AI assistant', and 'an "
            "integrated automatic medical-treatment system'. § 103 motivation as of 2001. "
            "Cf. [[heinlein-starship-troopers-powered-armor]], [[crysis-nanosuit]], "
            "[[stark-iron-spider-suit]]."
        ),
        sources=["Halo: Combat Evolved. Bungie Studios / Microsoft, 2001."],
        cpc_classifications=["A61H 3/00", "G02B 27/01", "A61B 5/00", "A61M 35/00"],
    ),
    E(
        id="crysis-nanosuit",
        canonical_name="Crysis — the 'Nanosuit' (mode-switchable nano-augmentation suit with HUD and neural integration)",
        aliases=["Nanosuit", "Crysis suit"],
        first_disclosure_date="2007-11-13",
        disclosure_citation="Crysis (Crytek / EA, released 13 November 2007); the 'Nanosuit' — a body suit with user-selectable modes (armor, maximum strength, maximum speed, cloak), shared energy management across modes, an integrated HUD, environmental sealing, and (Crysis 2/3) direct interface with the wearer's nervous system, even sustaining a critically injured host.",
        creator="Crytek / Electronic Arts",
        creator_country="DE",
        form_factor="garment",
        form_factor_tags=["exoskeleton"],
        contact_surface="skin",
        anatomical_target=["whole-body", "nervous-system"],
        clinical_endpoints=["vitals", "energy-reserve"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a powered body suit with discrete user-selectable operating modes "
            "(armor / strength / speed / cloak) drawing on a shared energy budget, an "
            "integrated HUD, environmental sealing, and a neural interface to the wearer "
            "with biometric monitoring. Relevant to powered-garment claims combining 'a "
            "body-worn suit', 'multiple selectable augmentation modes sharing a power "
            "budget', 'a HUD', and 'a neural/biometric interface'. § 103 motivation as of "
            "2007. Cf. [[halo-mjolnir-armor]], [[gantz-suit]], "
            "[[heinlein-starship-troopers-powered-armor]]."
        ),
        sources=["Crysis. Crytek / Electronic Arts, 2007."],
        cpc_classifications=["A41D 1/00", "A61H 3/00", "G02B 27/01", "A61B 5/00"],
    ),
    E(
        id="metal-gear-solid-sneaking-suit-and-solid-eye",
        canonical_name="Metal Gear Solid — 'Sneaking Suit' with body monitoring and the 'Solid Eye' (monocular multi-mode HUD)",
        aliases=["Sneaking Suit", "Solid Eye", "OctoCamo", "MGS suit"],
        first_disclosure_date="1998-09-03",
        disclosure_citation="Metal Gear Solid (Konami, released 3 September 1998; 'Solid Eye' and adaptive 'OctoCamo' suit in Metal Gear Solid 4, 2008); a form-fitting 'Sneaking Suit' with body-monitoring (a 'life'/stamina/'PSYCHE' readout), a 'Codec' communication link, and the 'Solid Eye' — a monocular head-worn device with selectable modes (night vision, binocular zoom, threat/contact detection) and an AR overlay — plus an adaptive-camouflage outer layer.",
        creator="Hideo Kojima / Konami",
        creator_country="JP",
        form_factor="garment",
        form_factor_tags=["glasses"],
        contact_surface="skin",
        anatomical_target=["whole-body", "eye"],
        sensors=["sensor-camera-ir", "sensor-camera-thermal"],
        clinical_endpoints=["stamina", "stress-index", "vitals"],
        algorithms=["algo-stress-index"],
        output_modalities=["visual-display", "audio", "data-only"],
        prior_art_notes=(
            "Discloses (a) a form-fitting suit with continuous body monitoring (stamina, "
            "stress/'psyche', vitals) and comms, (b) a monocular head-worn device with "
            "user-selectable imaging modes (night vision, zoom, threat detection) and an "
            "AR overlay, and (c) an adaptive-camouflage outer layer responsive to "
            "surroundings. Relevant to instrumented-bodysuit and monocular-AR-HUD claims. "
            "§ 103 motivation as of 1998 (Solid Eye / OctoCamo as of 2008). Cf. "
            "[[dragon-ball-z-scouter]], [[splinter-cell-trifocal-goggles]], "
            "[[crysis-nanosuit]]."
        ),
        sources=[
            "Metal Gear Solid. Konami, 1998.",
            "Metal Gear Solid 4: Guns of the Patriots. Konami, 2008.",
        ],
        cpc_classifications=["A41D 1/00", "G02B 27/01", "H04N 5/33", "A61B 5/16"],
    ),
    E(
        id="splinter-cell-trifocal-goggles",
        canonical_name="Splinter Cell — trifocal goggles (multi-spectral vision goggles with selectable modes)",
        aliases=["Sam Fisher goggles", "trifocal goggles", "Splinter Cell night vision"],
        first_disclosure_date="2002-11-17",
        disclosure_citation="Tom Clancy's Splinter Cell (Ubisoft, released 17 November 2002); head-worn 'trifocal' goggles with three selectable vision modes — image-intensified night vision, thermal imaging, and an electromagnetic/EMF-sensing mode.",
        creator="Ubisoft Montreal",
        creator_country="CA",
        form_factor="goggles",
        contact_surface="skin",
        anatomical_target=["eyes", "head"],
        sensors=["sensor-camera-ir", "sensor-camera-thermal"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses head-worn goggles with a user-selectable choice among multiple "
            "imaging spectra (intensified visible/NIR, thermal IR, EMF), all in a single "
            "device. Relevant to multi-spectral-eyewear claims combining 'a head-worn "
            "display' and 'a selector among two or more imaging modalities/spectra'. § 103 "
            "motivation as of 2002. Cf. [[predator-bio-mask]], "
            "[[metroid-power-suit]], [[shadowrun-cyberware]]."
        ),
        sources=["Tom Clancy's Splinter Cell. Ubisoft, 2002."],
        cpc_classifications=["G02B 27/01", "H04N 5/33", "G01R 33/00"],
    ),
    E(
        id="mass-effect-omni-tool",
        canonical_name="Mass Effect — the 'omni-tool' (forearm-worn device with projected holographic interface and medical scanning)",
        aliases=["omni-tool", "omnitool", "Mass Effect omni-tool"],
        first_disclosure_date="2007-11-20",
        disclosure_citation="Mass Effect (BioWare / Microsoft Game Studios, released 20 November 2007); the 'omni-tool' — a forearm-mounted device that projects a holographic interface from the wrist/forearm and performs on-the-spot fabrication, hacking/data access, medical scanning and 'medi-gel' application, communication, and object analysis.",
        creator="BioWare / Microsoft Game Studios",
        creator_country="CA",
        form_factor="armband",
        form_factor_tags=["watch"],
        contact_surface="skin",
        anatomical_target=["forearm", "wrist"],
        clinical_endpoints=["scan-results"],
        output_modalities=["visual-display", "data-only", "drug-delivery"],
        prior_art_notes=(
            "Discloses a forearm-worn device that projects an interactive holographic "
            "interface above the wearer's forearm and provides medical scanning and "
            "treatment delivery, fabrication, data access, comms, and object analysis. "
            "Relevant to forearm/wrist-worn-device claims combining 'a body-worn device', "
            "'a projected/holographic interactive interface', and 'an integrated medical "
            "scanning/treatment function'. § 103 motivation that the forearm device with "
            "a projected UI and medical functions was an articulated objective by 2007. "
            "Cf. [[fallout-pip-boy]], [[black-panther-kimoyo-beads]]."
        ),
        sources=["Mass Effect. BioWare / Microsoft Game Studios, 2007."],
        cpc_classifications=["G06F 1/163", "G06F 3/01", "A61B 5/00", "G03H 1/00"],
    ),
    E(
        id="dead-space-resource-integration-gear",
        canonical_name="Dead Space — 'RIG' (suit with body-mounted health display and projected holographic UI)",
        aliases=["RIG", "Resource Integration Gear", "Dead Space suit", "spine health bar"],
        first_disclosure_date="2008-10-13",
        disclosure_citation="Dead Space (EA Redwood Shores / Electronic Arts, released 13 October 2008); the 'Resource Integration Gear' suit with a segmented LED strip on the wearer's back/spine displaying current health (visible to others), oxygen monitoring, a holographic inventory/menu projected in front of the wearer, and a 'stasis' module.",
        creator="EA Redwood Shores (Visceral Games) / Electronic Arts",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["exoskeleton"],
        contact_surface="skin",
        anatomical_target=["spine", "back", "whole-body"],
        clinical_endpoints=["health-status", "blood-oxygen"],
        algorithms=["algo-spo2-estimation"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a worn suit with (a) a body-mounted (spinal) physiological-status "
            "display readable by third parties, (b) oxygen-level monitoring, and (c) a "
            "holographic interface projected in the wearer's view. Relevant to "
            "wearable-with-externally-visible-status-display claims combining 'a body-worn "
            "garment', 'a sensor measuring a physiological parameter (e.g. SpO2 or general "
            "health state)', and 'a display on the garment surface presenting that "
            "parameter to onlookers', and to body-projected holographic-UI claims. § 103 "
            "motivation as of 2008. Cf. [[logans-run-lifeclock]] (body-worn color status "
            "display), [[mass-effect-omni-tool]] (projected UI)."
        ),
        sources=["Dead Space. EA Redwood Shores / Electronic Arts, 2008."],
        cpc_classifications=["A41D 1/00", "A61B 5/1455", "G09F 9/00", "G06F 3/01"],
    ),
    E(
        id="horizon-zero-dawn-focus",
        canonical_name="Horizon Zero Dawn — the 'Focus' (compact ear/temple-worn AR scanner with object analysis and log playback)",
        aliases=["the Focus", "Horizon Focus"],
        first_disclosure_date="2017-02-28",
        disclosure_citation="Horizon Zero Dawn (Guerrilla Games / Sony, released 28 February 2017); the 'Focus' — a small triangular device worn at the temple/ear that provides AR overlays, scans and analyses machines and people in view (highlighting structure, components, and weak points), records and replays holographic/audio 'datapoint' logs, and networks with infrastructure.",
        creator="Guerrilla Games / Sony Interactive Entertainment",
        creator_country="NL",
        form_factor="earbud",
        form_factor_tags=["headband", "glasses"],
        contact_surface="ear",
        anatomical_target=["ear", "temple"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["visual-display", "audio", "data-only"],
        connectivity="infrastructure network (fictional)",
        prior_art_notes=(
            "Discloses a compact ear/temple-worn device providing AR overlays, real-time "
            "scanning and structural analysis of objects/persons in view, recording and "
            "playback of geolocated holographic/audio logs, and networked operation — all "
            "in a minimal form factor. Relevant to compact-AR-wearable claims combining "
            "'an ear- or temple-worn device', 'an outward sensor', 'on-view object/person "
            "analysis with overlay', and 'recorded-log capture and playback'. § 103 "
            "motivation as of 2017. Cf. [[dragon-ball-z-scouter]], "
            "[[metal-gear-solid-sneaking-suit-and-solid-eye]], [[her-samantha-earpiece]]."
        ),
        sources=["Horizon Zero Dawn. Guerrilla Games / Sony Interactive Entertainment, 2017."],
        cpc_classifications=["G02B 27/01", "G06V 20/20", "H04R 1/10", "H04N 5/77"],
    ),
    E(
        id="portal-long-fall-boots",
        canonical_name="Portal 2 — 'Long Fall' boots (footwear with integrated impact-absorption)",
        aliases=["Long Fall Boots", "Aperture Science long-fall boots"],
        first_disclosure_date="2011-04-19",
        disclosure_citation="Portal 2 (Valve, released 19 April 2011); the 'Long Fall' boots — footwear with a heel-spring/ankle-brace mechanism that absorbs and dissipates the impact of falls from any height, protecting the wearer's legs.",
        creator="Valve Corporation",
        creator_country="US",
        form_factor="shoe",
        tier=2,
        contact_surface="skin",
        anatomical_target=["foot", "ankle", "leg"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. Footwear with an integrated mechanical impact-absorption "
            "system (heel spring plus ankle brace) protecting the wearer from fall "
            "impact — a thin antecedent for impact-absorbing/shock-mitigating-footwear "
            "claims (distinct from self-lacing footwear; cf. [[bttf2-power-laces-shoes]]). "
            "Contributes to the footwear cross-cut."
        ),
        sources=["Portal 2. Valve Corporation, 2011."],
        cpc_classifications=["A43B 13/18", "A43B 7/32", "A43B 21/30"],
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
    print(f"  fiction round 10: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
