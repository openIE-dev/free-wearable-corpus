#!/usr/bin/env python3
"""seed_2026q3_fiction_r9.py — fictional seed batch round 9 (film & TV, 1968-2013).

Run from repo root:  python3 seeds/seed_2026q3_fiction_r9.py
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
        id="blade-runner-voight-kampff",
        canonical_name="Blade Runner — the Voight-Kampff machine (contactless multi-physiological liveness/identity test)",
        aliases=["Voight-Kampff", "VK machine", "empathy test device"],
        first_disclosure_date="1968",
        disclosure_citation="Dick, Philip K. Do Androids Dream of Electric Sheep? Doubleday, 1968 (film: Blade Runner, Warner Bros., 1982); a portable instrument that measures involuntary physiological responses — pupil dilation, 'capillary dilation of the so-called blush response', heart rate, micro-expression — under questioning, to classify a subject as human or replicant.",
        creator="Philip K. Dick",
        creator_country="US",
        form_factor="other",
        contact_surface="non-contact",
        sensors=["sensor-camera-ir", "sensor-camera-eye"],
        clinical_endpoints=["pupil-diameter", "blush-response", "heart-rate", "micro-expression"],
        algorithms=["algo-pupillometry", "algo-hr", "algo-emotion-recognition"],
        output_modalities=["visual-display"],
        notes="Form factor 'other' — a desktop instrument aimed at the face, not worn. In scope as contactless multi-physiological measurement for a classification decision.",
        prior_art_notes=(
            "Discloses a device that contactlessly measures multiple involuntary "
            "physiological signals from a person's face (pupil dilation, blush/capillary "
            "response, heart rate, micro-expression) and fuses them into a binary "
            "classification of the subject. Relevant to remote-photoplethysmography / "
            "pupillometry / 'deception or liveness detection' claims combining 'contactless "
            "facial imaging', 'extraction of two or more involuntary physiological signals', "
            "and 'a classification of the subject'. § 103 motivation as of 1968. Cf. "
            "[[psycho-pass-cymatic-scan]], [[gattaca-biometric-checkpoints]]."
        ),
        sources=[
            "Dick, Philip K. Do Androids Dream of Electric Sheep? Doubleday, 1968.",
            "Blade Runner (film). Warner Bros., 1982.",
        ],
        cpc_classifications=["A61B 5/16", "A61B 3/11", "A61B 5/024", "G06V 40/16"],
    ),
    E(
        id="escape-from-new-york-life-clock",
        canonical_name="Escape from New York — wrist countdown unit and arterial micro-charge implant",
        aliases=["EFNY life clock", "Snake Plissken countdown"],
        first_disclosure_date="1981-07-10",
        disclosure_citation="Escape from New York (AVCO Embassy Pictures), released 10 July 1981; micro-charges injected into the carotid arteries enforce a deadline, paired with a wrist-worn unit displaying the countdown and tracking the wearer.",
        creator="John Carpenter / AVCO Embassy",
        creator_country="US",
        form_factor="watch",
        form_factor_tags=["implantable"],
        contact_surface="skin",
        anatomical_target=["wrist", "carotid-artery", "neck"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses a paired system: a body-embedded enforcement implant (in the "
            "carotid arteries) and a wrist-worn unit that displays a countdown and tracks "
            "the wearer's location. Relevant to compliance/monitoring-wearable claims "
            "combining 'a wrist-worn display/tracker' and 'a co-implanted enforcement or "
            "monitoring element'. § 103 motivation as of 1981. Cf. [[logans-run-lifeclock]], "
            "[[demolition-man-tracking-implant]], [[the-running-man-tracking-collar]]."
        ),
        sources=["Escape from New York (film). AVCO Embassy Pictures, 1981."],
        cpc_classifications=["A61B 5/00", "G04G 21/04", "H04W 4/029", "A61B 5/0031"],
    ),
    E(
        id="the-running-man-tracking-collar",
        canonical_name="The Running Man — worn tracking/enforcement collar",
        aliases=["Running Man collar", "explosive collar"],
        first_disclosure_date="1982-05",
        disclosure_citation="Bachman, Richard (Stephen King). The Running Man. Signet, 1982 (film: TriStar Pictures, 1987); a neck-worn collar that continuously transmits the wearer's location and status to a control center and can be remotely triggered to enforce compliance.",
        creator="Stephen King (as Richard Bachman)",
        creator_country="US",
        form_factor="pendant",
        tier=2,
        contact_surface="skin",
        anatomical_target=["neck"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A neck-worn device that continuously reports the wearer's "
            "location/status to a remote operator and supports a remote-trigger function "
            "— a thin antecedent for worn tracking/monitoring-collar claims (cf. modern "
            "GPS offender monitors). Contributes to the pendant/collar form-factor "
            "cross-cut. Cf. [[escape-from-new-york-life-clock]], "
            "[[demolition-man-tracking-implant]]."
        ),
        sources=[
            "Bachman, Richard. The Running Man. Signet, 1982.",
            "The Running Man (film). TriStar Pictures, 1987.",
        ],
        cpc_classifications=["G08B 21/02", "H04W 4/029", "A61B 5/00"],
    ),
    E(
        id="dune-holtzman-shield-belt",
        canonical_name="Dune — Holtzman shield belt (worn personal force-field generator)",
        aliases=["shield belt", "Holtzman shield", "Dune body shield"],
        first_disclosure_date="1965-08-01",
        disclosure_citation="Herbert, Frank. Dune. Chilton Books, 1965; a worn belt that projects a body-conforming defensive force field ('shield'), with selectable settings affecting what can pass through it.",
        creator="Frank Herbert",
        creator_country="US",
        form_factor="belt",
        tier=2,
        contact_surface="skin",
        anatomical_target=["waist"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A waist-worn device that projects a configurable "
            "body-conforming protective field — a thin (non-enabling) antecedent for "
            "belt-mounted personal-protection-field claims. Contributes to the belt "
            "cross-cut alongside [[batman-utility-belt]] (storage) and "
            "[[kamen-rider-henshin-belt]] (gesture-activated controller); distinct: this "
            "belt is itself the active protective device."
        ),
        sources=["Herbert, Frank. Dune. Chilton Books, 1965."],
        cpc_classifications=["A45F 5/00", "F41H 5/007"],
    ),
    E(
        id="tron-identity-disc",
        canonical_name="Tron — the 'identity disc' (back-worn data store and tool)",
        aliases=["identity disc", "Tron disc"],
        first_disclosure_date="1982-07-09",
        disclosure_citation="Tron (Walt Disney Productions), released 9 July 1982 (and Tron: Legacy, 2010); a disc worn on the back that stores the bearer's data, memories, and functions, removable for use as a tool or weapon and re-stowed afterward.",
        creator="Steven Lisberger / Walt Disney Productions",
        creator_country="US",
        form_factor="pendant",
        tier=2,
        contact_surface="skin",
        anatomical_target=["back"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Reference-only. A back-worn removable disc functioning as the bearer's "
            "personal data/memory store and a detachable tool — a thin antecedent for "
            "body-worn detachable-storage-device claims. Contributes to the pendant/"
            "back-worn form-factor cross-cut. Cf. [[flash-costume-ring]] (ring-stored "
            "deployable article)."
        ),
        sources=[
            "Tron (film). Walt Disney Productions, 1982.",
            "Tron: Legacy (film). Walt Disney Pictures, 2010.",
        ],
        cpc_classifications=["G06F 1/163", "G11B 33/00", "G06F 3/06"],
    ),
    E(
        id="star-trek-tng-the-game-neuro-visor",
        canonical_name="Star Trek: TNG 'The Game' — head-worn neuro-reward gaming visor",
        aliases=["The Game visor", "TNG game device"],
        first_disclosure_date="1991-10-28",
        disclosure_citation="Star Trek: The Next Generation, 'The Game' (first aired 28 October 1991); a small visor worn over the eyes that projects a game into the wearer's vision and stimulates the brain's reward centers on success, producing compulsive use.",
        creator="Brannon Braga / Paramount Television",
        creator_country="US",
        form_factor="glasses",
        form_factor_tags=["goggles"],
        contact_surface="ocular",
        anatomical_target=["eyes", "temporal-lobe"],
        output_modalities=["visual-display"],
        prior_art_notes=(
            "Discloses a head-worn device that presents a game in the wearer's visual "
            "field and delivers a neural reward stimulus contingent on gameplay events. "
            "Relevant to neuro-gaming claims combining 'a near-eye display presenting a "
            "game' and 'delivery of a neuro-reward/stimulation contingent on game state'. "
            "§ 103 motivation as of 1991 — predating "
            "[[black-mirror-fifteen-million-merits-gaze-enforcement]] and "
            "[[black-mirror-playtest-implant]]."
        ),
        sources=["Star Trek: The Next Generation, 'The Game'. Paramount Television, 1991."],
        cpc_classifications=["A63F 13/212", "A61M 21/00", "G02B 27/01"],
    ),
    E(
        id="judge-dredd-helmet-and-lawgiver",
        canonical_name="Judge Dredd — Judge's helmet HUD and palmprint-authenticated 'Lawgiver'",
        aliases=["Dredd helmet", "Lawgiver", "Judge helmet"],
        first_disclosure_date="1977-03-26",
        disclosure_citation="Judge Dredd, 2000 AD prog 2 (cover date 26 March 1977), Rebellion/IPC; the Judge's helmet with an integrated heads-up display and comms, and the 'Lawgiver' sidearm whose grip reads the Judge's palmprint so the weapon fires only for its assigned bearer.",
        creator="John Wagner / Carlos Ezquerra / Pat Mills / 2000 AD",
        creator_country="GB",
        form_factor="helmet",
        contact_surface="skin",
        anatomical_target=["head", "face", "hand"],
        output_modalities=["visual-display", "audio", "data-only"],
        notes="The Lawgiver's palmprint grip is a handheld device, but it pairs with the worn helmet and is included for the grip-biometric-authentication element.",
        prior_art_notes=(
            "Discloses (a) a helmet with an integrated HUD and comms and (b) a handheld "
            "device that authenticates its user by a palmprint sensor in the grip, "
            "operating only for the recognized bearer. Relevant to head-worn-HUD claims "
            "and to grip-biometric-authentication claims combining 'a grip-surface "
            "biometric sensor', 'matching against an enrolled user', and 'enabling the "
            "device only for that user' (cf. authenticated firearms, wearer-bound tools). "
            "§ 103 motivation as of 1977. Cf. [[doc-smith-lens]] (wearer attunement), "
            "[[gattaca-biometric-checkpoints]]."
        ),
        sources=["Wagner, John; Ezquerra, Carlos. Judge Dredd, 2000 AD prog 2. IPC Magazines, 1977."],
        cpc_classifications=["A42B 3/04", "G02B 27/01", "F41A 17/06", "G06F 21/32"],
    ),
    E(
        id="lawnmower-man-vr-cybersuit",
        canonical_name="The Lawnmower Man — VR rig (gyro chair, headset, full-body cybersuit)",
        aliases=["Lawnmower Man VR suit", "cyberspace suit"],
        first_disclosure_date="1992-03-06",
        disclosure_citation="The Lawnmower Man (New Line Cinema), released 6 March 1992; a virtual-reality rig comprising a motorized gyroscopic chair, a head-mounted display, and a full-body 'cybersuit' that tracks the wearer's movements and conveys virtual sensations.",
        creator="Brett Leonard / Allied Vision / New Line Cinema",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["goggles"],
        tier=2,
        contact_surface="skin",
        anatomical_target=["whole-body"],
        sensors=["sensor-accelerometer", "sensor-gyroscope"],
        output_modalities=["haptic", "visual-display"],
        prior_art_notes=(
            "Reference-only. An early integrated VR rig — head-mounted display plus a "
            "full-body motion-capturing, sensation-conveying suit — a thin antecedent for "
            "full-body VR-suit-plus-HMD claims. Contributes to the garment cross-cut; "
            "predates [[ready-player-one-haptic-suit]] (2011) and [[sao-nervegear]] (2009)."
        ),
        sources=["The Lawnmower Man (film). New Line Cinema, 1992."],
        cpc_classifications=["G06F 3/01", "A41D 1/00", "G02B 27/01"],
    ),
    E(
        id="pacific-rim-drivesuit-and-conn-pod",
        canonical_name="Pacific Rim — Jaeger 'Drivesuit' and 'Conn-Pod' dual-pilot neural bridge",
        aliases=["Drivesuit", "Conn-Pod", "the Drift rig", "Pons system"],
        first_disclosure_date="2013-07-12",
        disclosure_citation="Pacific Rim (Warner Bros. / Legendary), released 12 July 2013; pilots wear a 'Drivesuit' (a body suit capturing motion and monitoring vitals) and a 'relay-gel'/spinal-clamp helmet that creates a shared neural bridge ('the Drift') between two co-pilots and the mecha.",
        creator="Guillermo del Toro / Legendary Pictures",
        creator_country="US",
        form_factor="garment",
        form_factor_tags=["helmet"],
        contact_surface="skin",
        anatomical_target=["whole-body", "spine", "scalp"],
        sensors=["sensor-ecg", "sensor-dry-eeg-electrode", "sensor-accelerometer"],
        clinical_endpoints=["heart-rate", "neural-sync", "motor-intent"],
        algorithms=["algo-hr"],
        output_modalities=["data-only"],
        prior_art_notes=(
            "Discloses an instrumented pilot suit (motion capture + vital-sign monitoring) "
            "combined with head/spine-worn relays that establish a shared neural bridge "
            "between two operators and a controlled machine. Relevant to multi-operator "
            "neural-interface claims and to instrumented-bodysuit claims combining 'a "
            "motion-capturing garment', 'vital-sign monitoring', and 'a head/spine neural "
            "relay linking multiple operators'. § 103 motivation as of 2013. Cf. "
            "[[nge-plug-suit-and-a10-clips]] (single-pilot), [[surrogates-neural-teleoperation-rig]]."
        ),
        sources=["Pacific Rim (film). Warner Bros. / Legendary Pictures, 2013."],
        cpc_classifications=["A61B 5/372", "A41D 1/00", "A61B 5/0205", "G06F 3/01"],
    ),
    E(
        id="repo-men-organ-transponder",
        canonical_name="Repo Men — artificial organ implant with built-in monitoring/repossession transponder",
        aliases=["Repo Men artiforg", "artiforg transponder"],
        first_disclosure_date="2009-04",
        disclosure_citation="Garcia, Eric. The Repossession Mambo, Harper, 2009 (film: Repo Men, Universal Pictures, 2010); financed artificial organs ('artiforgs') carry an integrated transponder reporting the implant's status and identity and enabling remote deactivation on non-payment.",
        creator="Eric Garcia",
        creator_country="US",
        form_factor="implantable",
        tier=2,
        contact_surface="sub-dermal",
        anatomical_target=["internal-organ"],
        clinical_endpoints=["implant-status"],
        output_modalities=["data-only"],
        connectivity="wireless transponder (fictional)",
        prior_art_notes=(
            "Reference-only. An implanted organ/device with a built-in wireless "
            "transponder that reports its identity and operating status and supports "
            "remote enable/disable — a thin antecedent for implanted-device-with-"
            "remote-management claims combining 'an implant', 'a wireless transponder "
            "reporting status', and 'remote control of the implant's operation'. Cf. "
            "[[demolition-man-tracking-implant]]; distinct in framing (financialized "
            "implant lifecycle)."
        ),
        sources=[
            "Garcia, Eric. The Repossession Mambo. Harper, 2009.",
            "Repo Men (film). Universal Pictures, 2010.",
        ],
        cpc_classifications=["A61B 5/0031", "G06K 19/07", "A61N 1/372"],
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
    print(f"  fiction round 9: added {added}, skipped {skipped} (already present)")


if __name__ == "__main__":
    main()
