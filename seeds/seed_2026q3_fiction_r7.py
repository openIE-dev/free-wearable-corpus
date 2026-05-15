#!/usr/bin/env python3
"""seed_2026q3_fiction_r7.py — fictional seed batch round 7 (Western superhero comics tech).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r7.py
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
        id="cyclops-ruby-quartz-visor",
        canonical_name="Cyclops's ruby-quartz visor (X-Men)",
        aliases=["Cyclops visor", "ruby quartz glasses"],
        first_disclosure_date="1963-09",
        disclosure_citation="The X-Men #1 (cover date September 1963), Marvel Comics; eyewear (visor or glasses) with ruby-quartz lenses and a wearer-operated aperture control that contains and modulates an energy emission from the wearer's eyes.",
        creator="Stan Lee / Jack Kirby / Marvel Comics",
        creator_country="US",
        form_factor="glasses",
        tier=2,
        contact_surface="ocular",
        anatomical_target=["eye"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Reference-only. Eyewear with a wearer-actuated aperture/shutter that "
            "selectively passes or blocks an emission at the eye — a thin antecedent for "
            "eyewear claims with a controllable variable-transmission element. Contributes "
            "to the glasses cross-cut."
        ),
        sources=["Lee, Stan; Kirby, Jack. The X-Men #1. Marvel Comics, 1963."],
        cpc_classifications=["G02C 7/10", "G02B 27/01"],
    ),
    E(
        id="professor-x-cerebro",
        canonical_name="Cerebro (X-Men) — brain-amplifying head device for remote detection",
        aliases=["Cerebro"],
        first_disclosure_date="1964-09",
        disclosure_citation="The X-Men #7 (cover date September 1964), Marvel Comics; 'Cerebro' — a head-worn helmet/headset that amplifies the wearer's neural signals to detect and geolocate other minds at a distance, with a display readout of the detections.",
        creator="Stan Lee / Jack Kirby / Marvel Comics",
        creator_country="US",
        form_factor="helmet",
        contact_surface="scalp",
        anatomical_target=["scalp", "head"],
        sensors=["sensor-dry-eeg-electrode"],
        clinical_endpoints=["neural-activity"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a head-worn device that couples to the wearer's brain, amplifies "
            "the neural signal, uses it for a sensing task (detecting/locating other "
            "minds), and presents the results on a display. Relevant to neural-amplifier / "
            "brain-coupled-sensing claims combining 'a head-worn neural pickup', 'signal "
            "amplification', and 'a derived detection output'. § 103 motivation as of 1964. "
            "Cf. [[strange-days-squid-recorder]], [[ghost-in-the-shell-cyberbrain]]."
        ),
        sources=["Lee, Stan; Kirby, Jack. The X-Men #7. Marvel Comics, 1964."],
        cpc_classifications=["A61B 5/24", "A61B 5/372", "G06F 3/01"],
    ),
    E(
        id="magneto-helmet",
        canonical_name="Magneto's helmet (telepathy-shielding headgear)",
        aliases=["Magneto helmet"],
        first_disclosure_date="1963-09",
        disclosure_citation="The X-Men #1 (cover date September 1963), Marvel Comics; a worn helmet that shields the wearer's mind from external telepathic detection and intrusion.",
        creator="Stan Lee / Jack Kirby / Marvel Comics",
        creator_country="US",
        form_factor="helmet",
        tier=2,
        contact_surface="scalp",
        anatomical_target=["head"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A head-worn enclosure whose function is to block an external "
            "signal/field from reaching the wearer's head — a thin antecedent for "
            "shielding/Faraday-style headgear claims. Contributes to the helmet cross-cut "
            "alongside [[professor-x-cerebro]] (the complementary detection device)."
        ),
        sources=["Lee, Stan; Kirby, Jack. The X-Men #1. Marvel Comics, 1963."],
        cpc_classifications=["A42B 3/04", "H05K 9/00"],
    ),
    E(
        id="ant-man-cybernetic-helmet",
        canonical_name="Ant-Man's cybernetic helmet (head-worn interspecies signaling device)",
        aliases=["Ant-Man helmet", "Pym helmet"],
        first_disclosure_date="1962-09",
        disclosure_citation="Tales to Astonish #35 (cover date September 1962), Marvel Comics; a head-worn 'cybernetic helmet' that transmits and receives signals to communicate with and direct ants, paired with the size-changing suit.",
        creator="Stan Lee / Larry Lieber / Jack Kirby / Marvel Comics",
        creator_country="US",
        form_factor="helmet",
        tier=2,
        contact_surface="scalp",
        anatomical_target=["head"],
        actuators=["audio"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A head-worn transceiver for signaling to and from other "
            "organisms — a thin antecedent for headgear-mounted signaling/transponder "
            "claims. Contributes to the helmet cross-cut."
        ),
        sources=["Lee, Stan; Lieber, Larry; Kirby, Jack. Tales to Astonish #35. Marvel Comics, 1962."],
        cpc_classifications=["A42B 3/04", "H04B 13/00", "G06F 3/16"],
    ),
    E(
        id="iron-man-arc-reactor-chest-implant",
        canonical_name="Iron Man — arc-reactor chest implant (embedded power/life-support device with status display)",
        aliases=["arc reactor", "Stark chest reactor", "transistor-powered chest plate"],
        first_disclosure_date="1963-03",
        disclosure_citation="Tales of Suspense #39 (cover date March 1963), Marvel Comics, in which the original chest device keeps shrapnel from the wearer's heart (elaborated as the implanted 'arc reactor' in Iron Man, Marvel Studios, 2008); a chest-embedded device functioning simultaneously as a power source, a life-sustaining medical implant, and a status-indicated module.",
        creator="Stan Lee / Larry Lieber / Don Heck / Jack Kirby / Marvel Comics",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["chest", "sternum"],
        clinical_endpoints=["device-status"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a chest-embedded device that is at once a power source, a "
            "life-sustaining medical implant, and a module with an externally visible "
            "status indicator. Relevant to implantable-power-source and "
            "implant-with-status-display claims combining 'a sub-dermal device', 'an "
            "energy store powering other implanted/worn equipment', 'a therapeutic "
            "(life-sustaining) function', and 'a status indicator perceptible at the body "
            "surface'. § 103 motivation as of 1963 (status-display variant as of 2008). "
            "Cf. [[logans-run-lifeclock]], [[total-recall-2012-palm-phone]]."
        ),
        sources=[
            "Lee, Stan; Lieber, Larry; Heck, Don; Kirby, Jack. Tales of Suspense #39. Marvel Comics, 1963.",
            "Iron Man (film). Marvel Studios / Paramount Pictures, 2008.",
        ],
        cpc_classifications=["A61N 1/378", "A61B 5/00", "H02J 7/00", "A61B 5/0031"],
    ),
    E(
        id="iron-man-extremis",
        canonical_name="Iron Man — 'Extremis' (integrated body modification with wireless sensorium)",
        aliases=["Extremis", "Extremis virus"],
        first_disclosure_date="2005-01",
        disclosure_citation="Iron Man: Extremis #1-6 (Marvel Comics, 2005-2006, by Warren Ellis and Adi Granov); the 'Extremis' process rewrites the host's biology to integrate armor control into the nervous system, store equipment within the bones, accelerate healing, and provide a continuous wireless data feed to the host's senses.",
        creator="Warren Ellis / Adi Granov / Marvel Comics",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["whole-body", "nervous-system", "bones"],
        clinical_endpoints=["physiological-state"],
        output_modalities=["visual-display", "data-only"],
        connectivity="ubiquitous wireless (fictional)",
        prior_art_notes=(
            "Discloses a body modification that integrates equipment control into the "
            "nervous system, stores deployable hardware within the body, accelerates "
            "physiological repair, and streams ambient data continuously into the host's "
            "perception. Relevant to integrated body-augmentation claims combining "
            "'sub-dermal/embedded hardware', 'neural integration of device control', and "
            "'a continuous wireless sensorium'. § 103 motivation as of 2005. Cf. "
            "[[stark-iron-spider-suit]], [[neuromancer-mirrorshade-implants]]."
        ),
        sources=["Ellis, Warren; Granov, Adi. Iron Man: Extremis. Marvel Comics, 2005-2006."],
        cpc_classifications=["A61B 5/0031", "A61F 2/00", "G06F 3/01", "G06F 1/163"],
    ),
    E(
        id="batman-detective-vision-cowl",
        canonical_name="Batman — cowl with 'Detective Vision' (head-worn AR with through-obstacle vitals/skeletal overlay)",
        aliases=["Detective Vision", "Batman cowl AR", "Detective Mode"],
        first_disclosure_date="2009-08-25",
        disclosure_citation="Batman: Arkham Asylum (Rocksteady / Eidos, released 25 August 2009); the cowl's 'Detective Vision' overlays a real-time augmented view highlighting nearby people's skeletons and heartbeats through walls, evidence trails, and structural details, with integrated comms.",
        creator="Rocksteady Studios / Eidos Interactive",
        creator_country="GB",
        form_factor="helmet",
        form_factor_tags=["glasses"],
        contact_surface="skin",
        anatomical_target=["head", "face", "eyes"],
        sensors=["sensor-camera-ir"],
        output_modalities=["visual-display", "audio"],
        prior_art_notes=(
            "Discloses head-worn eyewear/cowl with an AR mode that detects nearby people "
            "(including through obstructions), renders their skeletal structure and "
            "live heart-rate indication in the wearer's view, and highlights other "
            "scene features, with comms. Relevant to AR-headgear claims combining 'a "
            "near-eye display', 'sensing of nearby persons', 'overlay of their "
            "physiological indicators (e.g. heart rate)', and 'highlighting of scene "
            "features'. § 103 motivation as of 2009. Cf. [[robocop-targeting-hud]], "
            "[[predator-bio-mask]], [[total-recall-walkthrough-body-scanner]]."
        ),
        sources=["Batman: Arkham Asylum. Rocksteady Studios / Eidos Interactive, 2009."],
        cpc_classifications=["G02B 27/01", "A42B 3/04", "A61B 5/0205", "G06V 40/10"],
    ),
    E(
        id="falcon-exo7-wing-pack-and-goggles",
        canonical_name="Falcon — 'EXO-7' wing-pack exoskeleton with HUD goggles and tethered drone",
        aliases=["EXO-7 Falcon", "Falcon wing pack", "Redwing"],
        first_disclosure_date="2014-04-04",
        disclosure_citation="Captain America: The Winter Soldier (Marvel Studios), released 4 April 2014; a back-mounted articulated wing-pack exoskeleton with HUD goggles for targeting/telemetry and a paired deployable reconnaissance drone ('Redwing') controlled from the rig.",
        creator="Marvel Studios",
        creator_country="US",
        form_factor="exoskeleton",
        form_factor_tags=["goggles"],
        contact_surface="skin",
        anatomical_target=["back", "shoulders", "eyes"],
        sensors=["sensor-camera-rgb"],
        output_modalities=["visual-display", "data-only"],
        prior_art_notes=(
            "Discloses a body-worn articulated exoskeletal rig with integrated near-eye "
            "HUD goggles and a paired, rig-controlled drone whose camera feed appears in "
            "the wearer's display. Relevant to wearable-exoskeleton claims combining 'a "
            "body-mounted articulated assembly', 'a head-worn display', and 'control of a "
            "tethered/paired drone with its feed shown to the wearer'. § 103 motivation "
            "as of 2014. Cf. [[aliens-marine-helmet-cam]] (networked body-cam), "
            "[[snow-crash-gargoyle-rig]]."
        ),
        sources=["Captain America: The Winter Soldier (film). Marvel Studios, 2014."],
        cpc_classifications=["B64C 31/00", "G02B 27/01", "B64C 39/02", "H04N 7/18"],
    ),
    E(
        id="blue-beetle-scarab",
        canonical_name="Blue Beetle 'Scarab' — spine-attached adaptive armor generator with HUD and AI",
        aliases=["the Scarab", "Khaji Da", "Blue Beetle scarab"],
        first_disclosure_date="2006-05",
        disclosure_citation="Blue Beetle (vol. 8) #1 (Marvel… DC Comics, May 2006), the Jaime Reyes incarnation; an alien biotechnological device that attaches to the host's spine and on activation extrudes a full conformal armored exo-body with weapons, flight, sensors, a heads-up display, and a symbiotic on-board artificial intelligence.",
        creator="Keith Giffen / John Rogers / Cully Hamner / DC Comics",
        creator_country="US",
        form_factor="implantable",
        form_factor_tags=["exoskeleton"],
        contact_surface="sub-dermal",
        anatomical_target=["spine", "back"],
        sensors=["sensor-camera-rgb", "sensor-camera-ir"],
        output_modalities=["visual-display", "audio", "data-only"],
        prior_art_notes=(
            "Discloses a spine-attached device that, on command, generates a conformal "
            "powered exo-body with integrated sensors, a near-eye HUD, and an on-board AI "
            "in symbiotic dialogue with the host. Relevant to implant-plus-exoskeleton "
            "claims combining 'a body-attached generator unit', 'a deployable conformal "
            "powered suit', 'integrated sensing and a HUD', and 'an onboard assistant'. "
            "§ 103 motivation as of 2006. Cf. [[stark-iron-spider-suit]], "
            "[[venom-symbiote-suit]]."
        ),
        sources=["Giffen, Keith; Rogers, John; Hamner, Cully. Blue Beetle (vol. 8) #1. DC Comics, 2006."],
        cpc_classifications=["A61B 5/0031", "B25J 9/00", "G02B 27/01", "A41D 1/00"],
    ),
    E(
        id="venom-symbiote-suit",
        canonical_name="Venom symbiote — adaptive symbiotic worn covering responsive to wearer state",
        aliases=["the symbiote", "black suit", "Venom suit"],
        first_disclosure_date="1984-05",
        disclosure_citation="The Amazing Spider-Man #252 (cover date May 1984), Marvel Comics, introducing the alien 'black costume' later revealed as a symbiote (named Venom in The Amazing Spider-Man #300, 1988); a living covering that bonds to the wearer's body, augments strength, reshapes itself on demand, generates appendages, and reacts to the host's emotional and physiological state.",
        creator="Roger Stern / Tom DeFalco / Mike Zeck / Ron Frenz / David Michelinie / Todd McFarlane / Marvel Comics",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["tattoo-electronic"],
        tier=2,
        contact_surface="skin",
        anatomical_target=["whole-body"],
        clinical_endpoints=["affective-state", "physiological-state"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. An adaptive, body-conforming worn covering that augments the "
            "wearer, reconfigures on demand, and responds to the wearer's affective and "
            "physiological state — a thin (biological, non-enabling) antecedent for "
            "shape-adaptive smart-garment and affect-responsive-wearable claims. "
            "Contributes to the garment cross-cut alongside [[bttf2-self-drying-jacket]] "
            "and [[stark-iron-spider-suit]]."
        ),
        sources=[
            "Stern, Roger; Zeck, Mike. The Amazing Spider-Man #252. Marvel Comics, 1984.",
            "Michelinie, David; McFarlane, Todd. The Amazing Spider-Man #300. Marvel Comics, 1988.",
        ],
        cpc_classifications=["A41D 1/00", "A61B 5/16", "A41D 13/00"],
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
    print(f"  fiction round 7: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
