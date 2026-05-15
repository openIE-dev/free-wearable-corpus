#!/usr/bin/env python3
"""seed_2026q3_fiction_r6.py — fictional seed batch round 6 (anime, manga & tabletop SF).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r6.py
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
        id="dragon-ball-z-scouter",
        canonical_name="Dragon Ball 'Scouter' (monocular scanning eyewear)",
        aliases=["Scouter", "DBZ scouter"],
        first_disclosure_date="1989-04",
        disclosure_citation="Toriyama, Akira. Dragon Ball (manga), the Saiyan arc introducing the 'Scouter' c. April 1989, Shueisha (Dragon Ball Z anime, 1989); a monocular eyewear device that scans a target and displays a quantified strength metric ('power level'), with two-way voice communication and a head-up readout.",
        creator="Akira Toriyama",
        creator_country="JP",
        form_factor="glasses",
        contact_surface="ocular",
        anatomical_target=["ear", "eye"],
        sensors=["sensor-camera-rgb"],
        actuators=["audio"],
        output_modalities=["visual-display", "audio"],
        connectivity="radio link (fictional)",
        prior_art_notes=(
            "Discloses monocular head-worn eyewear that scans a person/object in view, "
            "computes and displays a quantified metric about the target, and provides "
            "two-way voice comms — all in a single ear-hooked unit with a flip-down "
            "display. Relevant to AR-eyewear claims combining 'a monocular near-eye "
            "display', 'an outward sensor', 'on-view target measurement/identification', "
            "and 'integrated voice comms'. § 103 motivation that the scan-and-display-a-"
            "metric monocular headset was an articulated objective by 1989. Cf. "
            "[[black-mirror-nosedive-rating-overlay]]."
        ),
        sources=["Toriyama, Akira. Dragon Ball. Shueisha (Weekly Shōnen Jump), 1984-1995."],
        cpc_classifications=["G02B 27/01", "G06V 20/20", "H04M 1/05"],
    ),
    E(
        id="gundam-psycommu-interface",
        canonical_name="Mobile Suit Gundam — 'psycommu' head-worn neural interface for remote weapon control",
        aliases=["psycommu", "psycho-frame", "Newtype interface"],
        first_disclosure_date="1979-04-07",
        disclosure_citation="Mobile Suit Gundam (Nippon Sunrise television series, premiered 7 April 1979); the 'psycommu' system — a head-worn interface that reads the pilot's brainwaves to direct remote weapon units ('funnels'/'bits') and control the mobile suit without manual input.",
        creator="Yoshiyuki Tomino / Nippon Sunrise",
        creator_country="JP",
        form_factor="helmet",
        form_factor_tags=["headband"],
        contact_surface="scalp",
        anatomical_target=["scalp", "head"],
        sensors=["sensor-dry-eeg-electrode"],
        clinical_endpoints=["motor-intent", "neural-activity"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a head-worn neural sensor that decodes the wearer's intent from "
            "brain activity and uses it to command remote machines/weapons and a piloted "
            "vehicle hands-free. Relevant to wearable-BCI claims combining 'a head-worn "
            "neural sensor array', 'decoding of operator intent', and 'transmission of "
            "commands to remote devices'. § 103 motivation that the wearable "
            "neural-control interface for remote devices was an articulated objective by "
            "1979 — predating [[surrogates-neural-teleoperation-rig]]."
        ),
        sources=["Mobile Suit Gundam (television series). Nippon Sunrise, 1979."],
        cpc_classifications=["A61B 5/372", "G06F 3/01", "B25J 13/00"],
    ),
    E(
        id="nge-plug-suit-and-a10-clips",
        canonical_name="Neon Genesis Evangelion — 'plug suit' and 'A10 nerve clips' (bio-monitoring suit + head-worn neural sync interface)",
        aliases=["plug suit", "A10 clips", "Eva interface clips"],
        first_disclosure_date="1995-10-04",
        disclosure_citation="Neon Genesis Evangelion (Gainax television series, premiered 4 October 1995); pilots wear a skin-tight pressurized 'plug suit' with continuous bio-monitoring and a measured 'synchronization ratio' with the mecha, plus 'A10 nerve clips' worn on the head that interface the pilot's nervous system to the machine.",
        creator="Hideaki Anno / Gainax",
        creator_country="JP",
        form_factor="garment",
        form_factor_tags=["headband"],
        contact_surface="skin",
        anatomical_target=["torso", "limbs", "scalp"],
        sensors=["sensor-ecg", "sensor-dry-eeg-electrode", "sensor-respiration-impedance"],
        clinical_endpoints=["heart-rate", "respiration", "neural-sync"],
        algorithms=["algo-hr", "algo-respiratory-rate"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses (a) a form-fitting body garment with continuous vital-sign "
            "monitoring and a derived operator-machine synchronization metric, and (b) "
            "head-worn clips coupling the wearer's nervous system to an external system. "
            "Relevant to instrumented-bodysuit claims combining 'a close-fitting garment "
            "with distributed physiological sensors' and 'a derived synchronization/"
            "engagement metric', and to head-worn neural-interface claims. § 103 "
            "motivation as of 1995. Cf. [[pacific-rim-drivesuit-and-conn-pod]] (a later "
            "dual-pilot variant)."
        ),
        sources=["Neon Genesis Evangelion (television series). Gainax, 1995-1996."],
        cpc_classifications=["A61B 5/0205", "A41D 13/00", "A61B 5/372", "A61B 5/318"],
    ),
    E(
        id="cyberpunk-2020-cyberoptics-and-interface-plugs",
        canonical_name="Cyberpunk 2020 — 'cyberoptics' and 'Interface plugs' (implanted sensor eyes + neural ports)",
        aliases=["cyberoptics", "Interface plugs", "Cyberpunk 2020 cyberware", "Cyberpunk 2013"],
        first_disclosure_date="1988",
        disclosure_citation="Pondsmith, Mike. Cyberpunk (a.k.a. 'Cyberpunk 2013'), R. Talsorian Games, 1988 (expanded as 'Cyberpunk 2020', 1990; video game 'Cyberpunk 2077', 2020); 'cyberoptics' — prosthetic eyes with selectable modes (low-light, infrared, telescopic, image enhancement), camera/recording options, and a HUD overlay — and 'Interface plugs' / neural processors for direct device control.",
        creator="Mike Pondsmith / R. Talsorian Games",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["eye", "skull", "wrist"],
        sensors=["sensor-camera-ir", "sensor-camera-rgb"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses prosthetic ocular implants with user-selectable imaging modes "
            "(low-light, IR, telescopic, enhancement), optional integrated camera and "
            "recording, and a HUD overlay, plus implanted neural ports for direct machine "
            "control. Relevant to implantable-vision-system and implanted-neural-interface "
            "claims; part of the chronological chain through "
            "[[caidin-cyborg-bionics]] (1972), [[neuromancer-mirrorshade-implants]] (1984), "
            "[[shadowrun-cyberware]] (1989), [[ghost-in-the-shell-cyberbrain]] (1989). § 103 "
            "motivation as of 1988."
        ),
        sources=[
            "Pondsmith, Mike. Cyberpunk. R. Talsorian Games, 1988.",
            "Pondsmith, Mike. Cyberpunk 2020. R. Talsorian Games, 1990.",
        ],
        cpc_classifications=["A61F 2/14", "A61F 9/08", "A61B 5/0031", "G06F 3/01"],
    ),
    E(
        id="shadowrun-cyberware",
        canonical_name="Shadowrun — 'cyberware' (cybereyes, cyberears, datajack, smartlink)",
        aliases=["cyberware", "cybereyes", "datajack", "smartlink", "Shadowrun cyberware"],
        first_disclosure_date="1989",
        disclosure_citation="Shadowrun, 1st edition, FASA Corporation, 1989; implanted 'cybereyes' (low-light/thermal/magnification/recording, HUD overlay), 'cyberears' (amplification, spatial recognition, recording), a head-mounted 'datajack' (neural data port), and a 'smartlink' wiring a weapon's targeting reticle into the eye.",
        creator="Bob Charrette / Paul Hume / Tom Dowd / FASA",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["eye", "ear", "skull"],
        sensors=["sensor-camera-ir", "sensor-camera-thermal", "sensor-microphone-air"],
        output_modalities=["visual-display", "audio", "data-only"],
        prior_art_notes=(
            "Discloses implanted vision and hearing prostheses with selectable enhancement "
            "modes and recording, a cranial neural data port, and a HUD targeting overlay "
            "wired to the eye. Relevant to implantable-sensory-prosthesis and "
            "implanted-data-port claims; an independent 1989 disclosure parallel to "
            "[[cyberpunk-2020-cyberoptics-and-interface-plugs]] and "
            "[[ghost-in-the-shell-cyberbrain]]. § 103 motivation as of 1989."
        ),
        sources=["Shadowrun (1st edition). FASA Corporation, 1989."],
        cpc_classifications=["A61F 2/14", "A61F 2/18", "A61B 5/0031", "G06F 3/01"],
    ),
    E(
        id="sao-nervegear",
        canonical_name="Sword Art Online — 'NerveGear' full-immersion VR headset",
        aliases=["NerveGear", "AmuSphere", "Augma", "SAO headset"],
        first_disclosure_date="2009-04-10",
        disclosure_citation="Kawahara, Reki. Sword Art Online (light novel), ASCII Media Works, first volume 10 April 2009; the 'NerveGear' — a head-worn helmet that intercepts sensory signals and motor commands at the brainstem level for total-immersion virtual reality (later 'AmuSphere' with safety limits; 'Augma' as a non-immersive AR wearable).",
        creator="Reki Kawahara",
        creator_country="JP",
        form_factor="helmet",
        contact_surface="scalp",
        anatomical_target=["scalp", "head", "brainstem"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a head-worn, non-implanted device that delivers full sensory "
            "immersion and reads motor intent by interfacing at the brainstem, plus a "
            "later lighter AR variant. Relevant to non-invasive full-sensory VR-headset "
            "claims combining 'a head-worn transducer array', 'suppression/substitution "
            "of native sensory input', and 'capture of motor intent'. § 103 motivation as "
            "of 2009. Cf. [[ready-player-one-haptic-suit]], [[lawnmower-man-vr-cybersuit]], "
            "[[black-mirror-striking-vipers-temple-disc]]."
        ),
        sources=["Kawahara, Reki. Sword Art Online, vol. 1. ASCII Media Works, 2009."],
        cpc_classifications=["G06F 3/01", "A61B 5/372", "G02B 27/01"],
    ),
    E(
        id="gantz-suit",
        canonical_name="Gantz — interface bodysuit (strength augmentation + player tracking)",
        aliases=["Gantz suit", "Gantz bodysuit"],
        first_disclosure_date="2000-07",
        disclosure_citation="Oku, Hiroya. Gantz (manga), Shueisha, serialization began July 2000; a skin-tight bodysuit issued to participants that greatly augments the wearer's strength and agility, interfaces with the wearer's body, and is tracked (with the wearer's status/score) by a central system.",
        creator="Hiroya Oku",
        creator_country="JP",
        form_factor="garment",
        contact_surface="skin",
        anatomical_target=["torso", "limbs"],
        clinical_endpoints=["wearer-status"],
        output_modalities=["data-only"],
        connectivity="central tracking link (fictional)",
        prior_art_notes=(
            "Discloses a close-fitting powered bodysuit that augments the wearer's "
            "strength/agility, interfaces with the body, and reports the wearer's status "
            "to a remote system. Relevant to powered-garment / soft-exosuit claims "
            "combining 'a form-fitting garment', 'force/agility augmentation', and "
            "'wearer-state telemetry'. § 103 motivation as of 2000. Cf. "
            "[[nge-plug-suit-and-a10-clips]], [[crysis-nanosuit]]."
        ),
        sources=["Oku, Hiroya. Gantz. Shueisha (Weekly Young Jump), 2000-2013."],
        cpc_classifications=["A41D 1/00", "A61H 3/00", "B25J 9/00"],
    ),
    E(
        id="sailor-moon-communicator-watch",
        canonical_name="Sailor Moon — Sailor Guardians' video communicator wristwatch",
        aliases=["Sailor communicator", "Sailor Moon wrist communicator"],
        first_disclosure_date="1991-12-28",
        disclosure_citation="Takeuchi, Naoko. Sailor Moon (Pretty Soldier Sailor Moon) (manga), Kodansha, serialization began December 1991 (anime 1992); wrist-worn 'communicator' devices used by the Sailor Guardians for two-way video and voice communication.",
        creator="Naoko Takeuchi",
        creator_country="JP",
        form_factor="watch",
        tier=2,
        sensors=["sensor-camera-rgb"],
        actuators=["audio"],
        output_modalities=["visual-display", "audio"],
        prior_art_notes=(
            "Reference-only. A wrist-worn device for two-way video and voice "
            "communication; one more entry in the long chain of wristworn-videophone "
            "fiction from [[dick-tracy-2way-wrist-tv]] (1964) and [[jetsons-wrist-communicator]] "
            "(1962) onward, here in a 1991 manga aimed at a mass audience."
        ),
        sources=["Takeuchi, Naoko. Pretty Soldier Sailor Moon. Kodansha (Nakayoshi), 1991-1997."],
        cpc_classifications=["G04G 21/04", "H04N 7/14"],
    ),
    E(
        id="pokemon-poketch",
        canonical_name="Pokémon — 'Pokétch' wrist device with an app ecosystem",
        aliases=["Poketch", "Pokémon Watch"],
        first_disclosure_date="2006-09-28",
        disclosure_citation="Pokémon Diamond and Pearl (Nintendo / Game Freak, 2006); the 'Pokétch' — a wrist-worn touchscreen device hosting an extensible set of small applications (clock, calculator, step counter, map, friendship checker, etc.).",
        creator="Game Freak / Nintendo",
        creator_country="JP",
        form_factor="watch",
        tier=2,
        sensors=["sensor-accelerometer"],
        algorithms=["algo-step-count"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Reference-only. A wrist-worn touchscreen device with an extensible app "
            "ecosystem including step counting and other utilities — a 2006 depiction of "
            "the app-platform smartwatch concept. Contributes to the wristworn-multifunction "
            "computer chain alongside [[inspector-gadget-wrist-computer]] (1983)."
        ),
        sources=["Pokémon Diamond and Pearl. Nintendo / Game Freak, 2006."],
        cpc_classifications=["G04G 21/04", "G06F 1/163", "A61B 5/11"],
    ),
    E(
        id="doraemon-take-copter",
        canonical_name="Doraemon — 'Take-copter' (head-worn thought-controlled flight device)",
        aliases=["Take-copter", "Bamboo Copter", "Hopter"],
        first_disclosure_date="1969-12",
        disclosure_citation="Fujiko F. Fujio. Doraemon (manga), Shogakukan, serialization began December 1969; the 'Take-copter' — a small propeller unit affixed to the head (or other body part) that lifts and flies the wearer, steered by the wearer's intent.",
        creator="Fujiko F. Fujio",
        creator_country="JP",
        form_factor="cap",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A head-worn personal-flight device steered by the wearer's "
            "intent — contributes the 'headgear as a personal locomotion appliance' "
            "concept circa 1969 to the headgear cross-cut, alongside "
            "[[inspector-gadget-gadget-hat]] (1983)."
        ),
        sources=["Fujiko F. Fujio. Doraemon. Shogakukan, 1969-1996."],
        cpc_classifications=["A42B 1/00", "B64C 27/00", "G06F 3/01"],
    ),
    E(
        id="kamen-rider-henshin-belt",
        canonical_name="Kamen Rider — 'Henshin Belt' (gesture-and-command transformation belt)",
        aliases=["Henshin Belt", "Typhoon belt", "Kamen Rider belt"],
        first_disclosure_date="1971-04-03",
        disclosure_citation="Kamen Rider (Toei television series, premiered 3 April 1971); a worn waist belt ('Typhoon' and its successors) that, on a gesture plus a spoken command from the wearer, triggers a transformation of the wearer's state/equipment.",
        creator="Shotaro Ishinomori / Toei",
        creator_country="JP",
        form_factor="belt",
        tier=2,
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A waist-worn device activated by a wearer gesture combined "
            "with a spoken command to invoke a function — contributes the 'belt-mounted "
            "gesture+voice-activated wearable controller' concept circa 1971 to the belt "
            "cross-cut, alongside [[batman-utility-belt]] (1939, the storage-platform "
            "variant)."
        ),
        sources=["Kamen Rider (television series). Toei Company, 1971-1973."],
        cpc_classifications=["A45F 5/00", "G06F 3/01", "G06F 1/163"],
    ),
    E(
        id="digimon-digivice",
        canonical_name="Digimon — 'Digivice' (worn companion-monitoring device)",
        aliases=["Digivice", "Digimon device"],
        first_disclosure_date="1999-03-07",
        disclosure_citation="Digimon Adventure (Toei animated series, premiered 7 March 1999; derived from the 1997 Tamagotchi-style 'Digital Monster' virtual-pet device); a small worn/clipped device with a display that monitors and tracks the status of a partner creature and the wearer's location relative to it.",
        creator="Akiyoshi Hongo / Toei / Bandai",
        creator_country="JP",
        form_factor="pendant",
        tier=2,
        sensors=["sensor-accelerometer"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Reference-only. A small worn device with a display that continuously monitors "
            "the status of a paired entity and relative location — a thin antecedent to "
            "wearable pet/companion-monitoring devices. Contributes to the pendant/clip-worn "
            "form-factor cross-cut."
        ),
        sources=[
            "Digimon Adventure (television series). Toei Animation / Bandai, 1999.",
            "Digital Monster (virtual-pet device). Bandai, 1997.",
        ],
        cpc_classifications=["G06F 1/163", "A01K 29/00", "H04W 4/029"],
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
    print(f"  fiction round 6: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
