#!/usr/bin/env python3
"""seed_2026q3_fiction_r8.py — fictional seed batch round 8 (older SF literature & pulp; deep pedigree).

Forster (1909), Gernsback (1911), Huxley (1932), 'Doc' Smith (1937),
Heinlein (1942, 1959), Delany (1968), Niven (1966), Gibson (1984).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r8.py
Idempotent — skips ids already present.

Doctrinal note: fictional disclosures are generally non-enabling; their
prior-art value is § 103 motivation-to-combine. The early-20th-century
entries here establish very long pedigree for several wearable concepts.
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
        id="forster-the-machine-stops-personal-apparatus",
        canonical_name="'The Machine Stops' — pervasive personal mediated-communication apparatus",
        aliases=["The Machine Stops apparatus", "Forster speaking-apparatus"],
        first_disclosure_date="1909-11",
        disclosure_citation="Forster, E.M. 'The Machine Stops', The Oxford and Cambridge Review, November 1909; each person interacts with the world almost entirely through a personal communication apparatus (visual 'plates', a speaking apparatus, an 'isolation knob'), giving and receiving lectures, calls, and information remotely.",
        creator="E.M. Forster",
        creator_country="GB",
        form_factor="other",
        contact_surface="non-contact",
        tier=2,
        output_modalities=["visual-display", "audio", "data-only"],
        notes="Form factor 'other' — a personal but room-fixed apparatus rather than a worn device. In scope as a very-long-pedigree antecedent of the ubiquitous-personal-mediated-communication concept.",
        prior_art_notes=(
            "Reference-only. Documents, in 1909, a society in which each individual "
            "conducts essentially all communication and information access through a "
            "personal mediated interface (audio, video, an isolation control). Thin and "
            "non-enabling, but establishes that the ubiquitous-personal-communication-"
            "device concept is over a century old — context for any patent claiming the "
            "bare idea of a pervasive personal communication terminal."
        ),
        sources=["Forster, E.M. 'The Machine Stops'. The Oxford and Cambridge Review, 1909."],
        cpc_classifications=["H04M 1/00", "G06F 1/16"],
    ),
    E(
        id="gernsback-hypnobioscope",
        canonical_name="Ralph 124C 41+ — the 'Hypnobioscope' (head-worn sleep-state learning device)",
        aliases=["Hypnobioscope", "Ralph 124C 41+ sleep-teacher"],
        first_disclosure_date="1911-04",
        disclosure_citation="Gernsback, Hugo. Ralph 124C 41+, serialized in Modern Electrics beginning April 1911 (book edition 1925); the 'Hypnobioscope' — a head-worn device that transmits printed/spoken information into the brain of a sleeping wearer for learning during sleep.",
        creator="Hugo Gernsback",
        creator_country="US",
        form_factor="headband",
        form_factor_tags=["cap"],
        contact_surface="scalp",
        anatomical_target=["scalp", "head"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a head-worn device used during sleep that delivers information into "
            "the wearer's brain — i.e. a wearable sleep-state learning/stimulation device. "
            "Relevant to sleep-stimulation and sleep-learning wearable claims combining "
            "'a head-worn transducer', 'operation during the wearer's sleep', and "
            "'delivery of a stimulus/content keyed to sleep state'. § 103 motivation that "
            "the wearable sleep-learning device was an articulated objective by 1911 — the "
            "deep antecedent for the modern sleep-headband patent space. Cf. "
            "[[strange-days-squid-recorder]]."
        ),
        sources=["Gernsback, Hugo. Ralph 124C 41+. Modern Electrics, 1911 / Stratford Co., 1925."],
        cpc_classifications=["A61M 21/00", "A61B 5/4806", "G09B 5/00"],
    ),
    E(
        id="huxley-brave-new-world-feelies",
        canonical_name="Brave New World — the 'feelies' (multisensory immersive media with tactile feedback) and hypnopaedia",
        aliases=["the feelies", "hypnopaedia", "Brave New World scent organ"],
        first_disclosure_date="1932",
        disclosure_citation="Huxley, Aldous. Brave New World. Chatto & Windus, 1932; the 'feelies' — cinema augmented with synchronized tactile sensations delivered through metal knobs the viewer holds — together with 'scent organs' and 'hypnopaedia' (sleep-teaching delivered via under-pillow speakers).",
        creator="Aldous Huxley",
        creator_country="GB",
        form_factor="other",
        contact_surface="skin",
        tier=2,
        output_modalities=["haptic", "thermal", "data-only"],
        notes="Form factor 'other' — held/seat-mounted transducers rather than a worn device. In scope as a deep antecedent of multisensory immersive media with tactile feedback, and of sleep-teaching apparatus.",
        prior_art_notes=(
            "Reference-only. Documents, in 1932, (a) immersive entertainment that adds "
            "synchronized tactile (and olfactory) sensations to audiovisual content via "
            "hand-contacted transducers, and (b) sleep-teaching apparatus. Thin and "
            "non-enabling, but long-pedigree context for haptic-immersive-media and "
            "sleep-learning claims. Cf. [[gernsback-hypnobioscope]], "
            "[[ready-player-one-haptic-suit]]."
        ),
        sources=["Huxley, Aldous. Brave New World. Chatto & Windus, 1932."],
        cpc_classifications=["G06F 3/01", "A63J 25/00", "A61M 21/00"],
    ),
    E(
        id="doc-smith-lens",
        canonical_name="The Lens (Lensman series) — wrist-worn device with single-wearer biometric attunement",
        aliases=["the Lens", "Arisian Lens", "Lensman Lens"],
        first_disclosure_date="1937-09",
        disclosure_citation="Smith, E.E. 'Doc'. Galactic Patrol, serialized in Astounding Stories beginning September 1937 (book edition 1950); 'the Lens' — a crystalline device worn at the wrist that is attuned to exactly one bearer, confers telepathic communication and translation, cannot be used by anyone else, and is harmful to an unauthorized wearer.",
        creator="E.E. 'Doc' Smith",
        creator_country="US",
        form_factor="bracelet",
        contact_surface="skin",
        anatomical_target=["wrist"],
        clinical_endpoints=["wearer-identity"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses a wrist-worn device that is biometrically attuned to a single "
            "authorized wearer, refuses to function for (and harms) any other wearer, and "
            "provides communication/translation services. Relevant to wearable-security "
            "claims combining 'a wrist-worn device', 'binding to a single enrolled wearer "
            "by a biometric or physiological signature', and 'disabling/refusal on an "
            "unrecognized wearer' (the now-common 'wrist-off detection' / 'continuous "
            "wearer authentication' feature). § 103 motivation that wrist-worn "
            "single-wearer attunement was an articulated objective by 1937. Cf. "
            "[[batman-utility-belt]] (a storage belt) — distinct: this is a "
            "wearer-attuned device."
        ),
        sources=["Smith, E.E. Galactic Patrol. Astounding Stories, 1937 / Fantasy Press, 1950."],
        cpc_classifications=["G06F 21/32", "A61B 5/00", "G06F 1/163", "H04W 12/06"],
    ),
    E(
        id="heinlein-waldo-master-gloves",
        canonical_name="'Waldo' — wearable master gloves for teleoperated manipulation",
        aliases=["waldoes", "Waldo gloves", "Heinlein waldo"],
        first_disclosure_date="1942-08",
        disclosure_citation="Heinlein, Robert A. (as Anson MacDonald). 'Waldo', Astounding Science-Fiction, August 1942; the operator wears master gloves whose movements are mirrored by remote manipulator hands ('waldoes') of any scale, with force/position feedback to the operator.",
        creator="Robert A. Heinlein",
        creator_country="US",
        form_factor="garment",
        contact_surface="skin",
        anatomical_target=["hands", "fingers"],
        sensors=["sensor-strain-gauge"],
        clinical_endpoints=["hand-pose", "finger-force"],
        output_modalities=["haptic", "data-only"],
        prior_art_notes=(
            "Discloses wearable instrumented gloves that capture the operator's hand and "
            "finger motion and forces, drive a remote manipulator that mirrors them, and "
            "return force/position feedback to the wearer — the foundational data-glove / "
            "telemanipulation-glove concept (the engineering term 'waldo' derives from "
            "this story). Relevant to data-glove claims combining 'a glove instrumented "
            "for hand/finger pose and force', 'transmission to a remote manipulator', and "
            "'haptic feedback to the wearer'. § 103 motivation as of 1942. Cf. "
            "[[ready-player-one-haptic-suit]], [[surrogates-neural-teleoperation-rig]]."
        ),
        sources=["Heinlein, Robert A. 'Waldo'. Astounding Science-Fiction, 1942."],
        cpc_classifications=["G06F 3/01", "B25J 3/04", "A41D 19/00", "G06F 3/014"],
    ),
    E(
        id="heinlein-starship-troopers-powered-armor",
        canonical_name="Starship Troopers — Mobile Infantry powered armor (powered exoskeleton with HUD, multi-sensor suite, comms, biomonitoring)",
        aliases=["powered armor", "Mobile Infantry suit", "MI powered suit"],
        first_disclosure_date="1959-10",
        disclosure_citation="Heinlein, Robert A. Starship Troopers, serialized as 'Starship Soldier' in The Magazine of Fantasy & Science Fiction, October-November 1959 (book edition 1959); the Mobile Infantry powered armor — a fully enclosing powered exoskeleton augmenting strength and mobility, with a HUD/'snoopers', integrated radar/IR/audio sensors, encrypted comms, climate control, medical/biometric monitoring, and assistive control ('the suit does part of your thinking for you').",
        creator="Robert A. Heinlein",
        creator_country="US",
        form_factor="exoskeleton",
        contact_surface="skin",
        anatomical_target=["whole-body"],
        sensors=["sensor-camera-ir", "sensor-microphone-air", "sensor-accelerometer"],
        clinical_endpoints=["multi-parameter-vitals"],
        output_modalities=["visual-display", "audio", "data-only"],
        prior_art_notes=(
            "Discloses a fully enclosing powered exoskeleton integrating strength/mobility "
            "augmentation, a head-up display, a multi-modal sensor suite (radar, IR, "
            "audio), encrypted comms, environmental control, wearer biometric monitoring, "
            "and assistive autonomy. The foundational powered-armor-with-integrated-"
            "sensorium text. Relevant to powered-exoskeleton claims combining 'a powered "
            "body-worn frame', 'a HUD', 'multiple environmental sensors', 'comms', and "
            "'monitoring of the wearer's vital signs'. § 103 motivation as of 1959. Cf. "
            "[[halo-mjolnir-armor]], [[crysis-nanosuit]], [[metroid-power-suit]], "
            "[[stark-iron-spider-suit]], [[darth-vader-life-support-suit]]."
        ),
        sources=["Heinlein, Robert A. Starship Troopers. The Magazine of Fantasy & Science Fiction, 1959 / G.P. Putnam's Sons, 1959."],
        cpc_classifications=["A61H 3/00", "B25J 9/00", "G02B 27/01", "A61B 5/00"],
    ),
    E(
        id="delany-nova-cyborg-sockets",
        canonical_name="Nova — 'plug' sockets at wrist and spine for direct machine operation",
        aliases=["Nova plugs", "cyborg studs", "Delany sockets"],
        first_disclosure_date="1968-08",
        disclosure_citation="Delany, Samuel R. Nova, Doubleday, 1968; people are born with sockets at the wrists and the small of the back ('plugs') used to connect directly to and operate machinery, ships, and tools as natural extensions of the body.",
        creator="Samuel R. Delany",
        creator_country="US",
        form_factor="implantable",
        contact_surface="sub-dermal",
        anatomical_target=["wrist", "spine"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses standardized body-mounted sockets (at the wrist and spine) for "
            "direct, plug-in operation of external machines. Relevant to implanted/"
            "percutaneous neural- or sensorimotor-interface-port claims combining 'a "
            "body-mounted connector', 'a standardized interface to external devices', and "
            "'direct sensorimotor control of those devices'. § 103 motivation as of 1968 — "
            "predating [[the-matrix-headjack]], [[existenz-bioport-and-game-pod]], and the "
            "cyberpunk 'datajack' lineage. Non-enabling."
        ),
        sources=["Delany, Samuel R. Nova. Doubleday, 1968."],
        cpc_classifications=["A61B 5/0031", "A61M 39/02", "G06F 3/01"],
    ),
    E(
        id="niven-autodoc",
        canonical_name="The 'autodoc' (Larry Niven, Known Space) — automated diagnostic-and-treatment booth",
        aliases=["autodoc", "auto-doc", "Niven autodoc"],
        first_disclosure_date="1966",
        disclosure_citation="Niven, Larry. Known Space stories (the 'autodoc' recurring from the mid-1960s, e.g. 'The Adults' / 'World of Ptavvs', 1966, and prominently in Ringworld, 1970); an automated booth/bed that scans an occupant, diagnoses injury and illness, and administers treatment without a human physician.",
        creator="Larry Niven",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        clinical_endpoints=["whole-body-diagnostics", "physiological-state"],
        output_modalities=["visual-display", "drug-delivery"],
        notes="Form factor 'other' — a fixed booth/bed, not worn. In scope as automated whole-body diagnosis and treatment; the term 'autodoc' is widely reused in later fiction.",
        prior_art_notes=(
            "Discloses an automated booth/bed that scans an occupant, derives a diagnosis "
            "across multiple body systems, and delivers treatment, all without a clinician "
            "— an early, much-reused articulation of the closed-loop diagnose-and-treat "
            "machine. Relevant to automated-diagnostic-and-treatment-station claims; part "
            "of the chain with [[star-trek-biobed]] (1966), [[elysium-medbay-scanner]] "
            "(2013). § 103 motivation as of 1966."
        ),
        sources=[
            "Niven, Larry. 'World of Ptavvs'. Worlds of Tomorrow, 1965 / Ballantine, 1966.",
            "Niven, Larry. Ringworld. Ballantine Books, 1970.",
        ],
        cpc_classifications=["A61B 5/00", "G16H 50/20", "A61G 7/05", "A61B 5/0205"],
    ),
    E(
        id="neuromancer-cyberspace-deck-trodes-and-simstim",
        canonical_name="Neuromancer — 'trodes' (head-worn cyberspace interface) and 'simstim' (worn sensory-broadcast rig)",
        aliases=["trodes", "simstim", "cyberspace deck", "Gibson trodes"],
        first_disclosure_date="1982-07",
        disclosure_citation="Gibson, William. 'Burning Chrome', Omni, July 1982 (and Neuromancer, Ace Books, 1984); 'simstim' — a worn rig that records and broadcasts one person's complete sensory experience for another to inhabit — and the head-worn electrode set ('trodes') by which a 'console cowboy' jacks into the 'matrix'/cyberspace.",
        creator="William Gibson",
        creator_country="CA",
        form_factor="headband",
        form_factor_tags=["cap"],
        contact_surface="scalp",
        anatomical_target=["scalp", "head"],
        sensors=["sensor-dry-eeg-electrode"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses (a) a head-worn, non-implanted electrode set providing bidirectional "
            "neural interface to a virtual/data environment, and (b) a worn rig that "
            "captures one wearer's full multisensory stream and broadcasts it for another "
            "to experience. Relevant to wearable-BCI and wearable-sensory-broadcast claims. "
            "§ 103 motivation as of 1982 — predating [[strange-days-squid-recorder]] (1995) "
            "for sensory broadcast, and a head-worn (non-implanted) alternative to "
            "[[the-matrix-headjack]]. Non-enabling."
        ),
        sources=[
            "Gibson, William. 'Burning Chrome'. Omni, 1982.",
            "Gibson, William. Neuromancer. Ace Books, 1984. ISBN 0-441-56956-0.",
        ],
        cpc_classifications=["A61B 5/372", "G06F 3/01", "A61B 5/24"],
    ),
    E(
        id="neuromancer-mirrorshade-ocular-implants",
        canonical_name="Neuromancer — Molly's mirrored ocular implants with embedded data readout",
        aliases=["mirrorshades", "Molly's lenses", "Gibson mirrorshade implants"],
        first_disclosure_date="1984",
        disclosure_citation="Gibson, William. Neuromancer, Ace Books, 1984; surgically inset mirrored lenses sealing the eye sockets, with a time display and other readouts projected into the wearer's field of view.",
        creator="William Gibson",
        creator_country="CA",
        form_factor="implantable",
        form_factor_tags=["contact-lens", "glasses"],
        contact_surface="ocular",
        anatomical_target=["eye"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses surgically implanted ocular lenses that present a head-up data "
            "readout (clock and other status) in the wearer's visual field — an early "
            "implanted-AR-display concept. Relevant to ocular-implant / AR-contact-lens "
            "claims combining 'an implanted or contact-lens optical element' and 'an "
            "overlaid data readout in the visual field'. § 103 motivation as of 1984 — "
            "predating [[cyberpunk-2020-cyberoptics-and-interface-plugs]] (1988) and "
            "[[rainbows-end-ar-contact-lens]] (2006). Non-enabling."
        ),
        sources=["Gibson, William. Neuromancer. Ace Books, 1984. ISBN 0-441-56956-0."],
        cpc_classifications=["G02C 7/04", "A61F 2/14", "G02B 27/01"],
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
    print(f"  fiction round 8: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
