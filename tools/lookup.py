#!/usr/bin/env python3
"""lookup.py — wearable patent-claim prior-art analyzer.

Given a claim phrase or free-form description, returns ranked corpus
entries that disclose the matching components (form factor / sensor /
algorithm), in chronological order. Earliest disclosure with a tag match
is the strongest 102 prior art candidate; combined matches are inputs to
the OBVIOUSNESS_TEMPLATE.

Usage:
    python3 tools/lookup.py "wristworn device with photoplethysmography sensor and atrial fibrillation detection"
    python3 tools/lookup.py "EEG glasses for seizure detection" --before 2020 --limit 5
    python3 tools/lookup.py --tag sensor-ppg --tag watch
    python3 tools/lookup.py "smart ring HRV" --commons-only

Ranking: tag matches (high weight) > prior_art_notes / details (medium)
> name / aliases (low). Ties broken by earlier disclosure date wins.
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
CORPUS = ROOT / "corpus.jsonl"

# Phrase → tag mapping. Extend freely; longer phrases match first.
TAG_KEYWORDS = {
    # form factor
    "wristworn": "watch",
    "wrist-worn": "watch",
    "wrist worn": "watch",
    "smartwatch": "watch",
    "smart watch": "watch",
    "wristwatch": "watch",
    "wristband": "bracelet",
    "wrist band": "bracelet",
    "fitness band": "bracelet",
    "smart ring": "ring",
    "finger ring": "ring",
    "smart glasses": "glasses",
    "ar glasses": "glasses",
    "smartglasses": "glasses",
    "eyeglasses": "glasses",
    "eye glasses": "glasses",
    "hmd": "goggles",
    "head-mounted display": "goggles",
    "head mounted display": "goggles",
    "vr headset": "goggles",
    "ar headset": "goggles",
    "contact lens": "contact-lens",
    "earbud": "earbud",
    "in-ear": "earbud",
    "in ear": "earbud",
    "hearing aid": "hearing-aid",
    "headphone": "over-ear-headphone",
    "headband": "headband",
    "skin patch": "patch",
    "adhesive patch": "patch",
    "wearable patch": "patch",
    "smart shirt": "garment",
    "smart fabric": "garment",
    "smart garment": "garment",
    "e-textile": "garment",
    "compression sleeve": "garment",
    "sports bra": "garment",
    "smart sock": "sock",
    "smart insole": "insole",
    "smart shoe": "shoe",
    "body camera": "body-camera",
    "bodycam": "body-camera",
    "exoskeleton": "exoskeleton",
    "implantable": "implantable",
    "ingestible": "ingestible",
    "smart pill": "ingestible",
    "mouthguard": "dental",
    "intraoral": "dental",
    "epidermal electronic": "tattoo-electronic",
    "electronic tattoo": "tattoo-electronic",

    # sensors — optical
    "photoplethysmography": "sensor-ppg",
    "ppg sensor": "sensor-ppg",
    "ppg": "sensor-ppg",
    "pulse oximetry": "sensor-spo2",
    "spo2": "sensor-spo2",
    "oxygen saturation": "sensor-spo2",
    "fnirs": "sensor-fnirs",
    "near-infrared spectroscopy": "sensor-fnirs",
    "raman spectroscopy": "sensor-raman",
    "thermal imager": "sensor-camera-thermal",
    "eye-tracking camera": "sensor-camera-eye",
    "eye tracking": "sensor-camera-eye",
    "ir camera": "sensor-camera-ir",
    "infrared camera": "sensor-camera-ir",

    # sensors — electrophysiological
    "electrocardiography": "sensor-ecg",
    "ecg sensor": "sensor-ecg",
    "ekg": "sensor-ecg",
    "electroencephalography": "sensor-eeg",
    "eeg sensor": "sensor-eeg",
    "eeg electrode": "sensor-eeg",
    "electromyography": "sensor-emg",
    "emg sensor": "sensor-emg",
    "electrooculography": "sensor-eog",
    "galvanic skin response": "sensor-gsr",
    "electrodermal": "sensor-gsr",
    "eda sensor": "sensor-gsr",
    "bioimpedance": "sensor-bioimpedance",
    "impedance pneumography": "sensor-respiration-impedance",

    # sensors — mechanical
    "accelerometer": "sensor-accelerometer",
    "gyroscope": "sensor-gyroscope",
    "magnetometer": "sensor-magnetometer",
    "barometric pressure": "sensor-barometer",
    "piezoelectric sensor": "sensor-piezoelectric",
    "strain gauge": "sensor-strain-gauge",

    # sensors — acoustic
    "bone conduction microphone": "sensor-microphone-bone",
    "digital stethoscope": "sensor-stethoscope-digital",

    # sensors — biochemical
    "continuous glucose monitor": "sensor-glucose-cgm",
    "cgm sensor": "sensor-glucose-cgm",
    "sweat lactate": "sensor-lactate",
    "sweat cortisol": "sensor-cortisol",
    "transdermal alcohol": "sensor-alcohol-transdermal",
    "ketone sensor": "sensor-ketone",

    # sensors — thermal
    "skin temperature": "sensor-skin-temperature",
    "core temperature": "sensor-core-temperature",
    "heat flux sensor": "sensor-heat-flux",

    # sensors — hemodynamic
    "pulse transit time": "sensor-cuffless-bp-ptt",
    "cuffless blood pressure": "sensor-cuffless-bp-ptt",
    "applanation tonometry": "sensor-cuffless-bp-tonometry",
    "volume clamp": "sensor-cuffless-bp-volume-clamp",

    # sensors — neural
    "dry electrode": "sensor-dry-eeg-electrode",
    "microneedle electrode": "sensor-microneedle-eeg",

    # sensors — other
    "mmwave radar": "sensor-radar-mmwave",
    "wearable ultrasound": "sensor-ultrasound-wearable",
    "uv exposure": "sensor-uv",
    "uv sensor": "sensor-uv",

    # algorithms
    "heart rate variability": "algo-hrv",
    "hrv": "algo-hrv",
    "atrial fibrillation": "algo-afib-detection",
    "afib": "algo-afib-detection",
    "arrhythmia detection": "algo-arrhythmia-classification",
    "blood pressure estimation": "algo-pwv-bp-estimation",
    "stress index": "algo-stress-index",
    "sleep staging": "algo-sleep-staging",
    "sleep stage": "algo-sleep-staging",
    "sleep apnea": "algo-sleep-apnea-detection",
    "snore detection": "algo-snore-detection",
    "step count": "algo-step-count",
    "fall detection": "algo-fall-detection",
    "gait analysis": "algo-gait-analysis",
    "activity classification": "algo-activity-classification",
    "calorie estimation": "algo-calorie-estimation",
    "tremor detection": "algo-tremor-detection",
    "bradykinesia": "algo-bradykinesia-detection",
    "seizure detection": "algo-seizure-detection",
    "cognitive workload": "algo-cognitive-workload",
    "drowsiness detection": "algo-drowsiness-detection",
    "attention state": "algo-attention-state",
    "ssvep": "algo-bci-ssvep",
    "motor imagery": "algo-bci-motor-imagery",
    "p300": "algo-bci-p300",
    "non-invasive glucose": "algo-glucose-noninvasive",
    "noninvasive glucose": "algo-glucose-noninvasive",
    "hand gesture": "algo-hand-gesture-emg",
    "gaze tracking": "algo-eye-gaze-tracking",
    "pupillometry": "algo-pupillometry",
    "emotion recognition": "algo-emotion-recognition",
    "respiratory rate": "algo-respiratory-rate",
    "cough detection": "algo-cough-detection",
}


def load_corpus():
    if not CORPUS.exists() or CORPUS.stat().st_size == 0:
        return []
    return [json.loads(l) for l in CORPUS.read_text().splitlines() if l.strip()]


def tags_from_claim(claim: str) -> dict:
    """Return {tag: hits}. Longer phrases match before shorter."""
    text = " " + claim.lower() + " "
    text = re.sub(r"[\(\)\.,;:/]", " ", text)
    hits = defaultdict(int)
    matched_spans = []
    phrases = sorted(TAG_KEYWORDS.keys(), key=len, reverse=True)
    for phrase in phrases:
        idx = 0
        while True:
            needle = " " + phrase + " " if " " in phrase else phrase
            i = text.find(needle, idx)
            if i == -1:
                break
            if any(s <= i < e or s < i + len(phrase) <= e for s, e in matched_spans):
                idx = i + 1
                continue
            hits[TAG_KEYWORDS[phrase]] += 1
            matched_spans.append((i, i + len(phrase)))
            idx = i + len(phrase)
    return dict(hits)


def entry_tags(entry):
    """All tags an entry carries across all three axes."""
    tags = set()
    if entry.get("form_factor"):
        tags.add(entry["form_factor"])
    for t in entry.get("form_factor_tags") or []:
        tags.add(t)
    for t in entry.get("sensors") or []:
        tags.add(t)
    for t in entry.get("algorithms") or []:
        tags.add(t)
    return tags


def score_entry(entry, tag_hits, claim_lower):
    score = 0
    matched = set()
    for t in entry_tags(entry):
        if t in tag_hits:
            score += 10 * tag_hits[t]
            matched.add(t)
    fields = [
        entry.get("prior_art_notes"),
        entry.get("sensor_details"),
        entry.get("notes"),
        entry.get("compute"),
    ]
    for f in fields:
        if not f:
            continue
        f_lower = f.lower()
        for term in claim_lower.split():
            if len(term) >= 4 and term in f_lower:
                score += 1
    name_lower = (entry.get("canonical_name") or "").lower()
    aliases = " ".join(entry.get("aliases") or []).lower()
    for term in claim_lower.split():
        if len(term) >= 4 and (term in name_lower or term in aliases):
            score += 1
    year_str = (entry.get("first_disclosure_date") or "")[:4]
    try:
        year = int(year_str)
    except ValueError:
        year = 9999
    return score, -year, matched


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("claim", nargs="*", help="claim phrase or free-form description")
    p.add_argument("--tag", action="append", default=[], help="explicit tag(s); repeatable")
    p.add_argument("--before", type=int, help="only entries disclosed before this year")
    p.add_argument("--after", type=int, help="only entries disclosed after this year")
    p.add_argument("--commons-only", action="store_true", help="exclude draft entries")
    p.add_argument("--tier-1-only", action="store_true", help="exclude Tier 2 reference-only entries")
    p.add_argument("--limit", type=int, default=15, help="max results to print (default 15)")
    p.add_argument("--json", action="store_true", help="output JSON")
    args = p.parse_args()

    if not args.claim and not args.tag:
        p.error("provide a claim phrase or --tag <tag>")

    claim = " ".join(args.claim)
    tag_hits = tags_from_claim(claim) if claim else {}
    for t in args.tag:
        tag_hits[t] = tag_hits.get(t, 0) + 1

    entries = load_corpus()
    scored = []
    for e in entries:
        if args.commons_only and e.get("draft"):
            continue
        if args.tier_1_only and e.get("tier") == 2:
            continue
        year_str = (e.get("first_disclosure_date") or "")[:4]
        try:
            year = int(year_str)
        except ValueError:
            year = None
        if args.before is not None and (year is None or year >= args.before):
            continue
        if args.after is not None and (year is None or year <= args.after):
            continue
        s, neg_year, matched = score_entry(e, tag_hits, claim.lower())
        if s > 0:
            scored.append((s, neg_year, matched, e))
    scored.sort(key=lambda x: (-x[0], x[1]))

    if args.json:
        print(json.dumps([
            {
                "id": e["id"],
                "canonical_name": e["canonical_name"],
                "year": (e.get("first_disclosure_date") or "")[:4],
                "corpus": e["corpus"],
                "form_factor": e.get("form_factor"),
                "ip_status": e.get("ip_status"),
                "draft": bool(e.get("draft")),
                "tier": e.get("tier", 1),
                "score": s,
                "matched_tags": sorted(mt),
                "disclosure_citation": e.get("disclosure_citation"),
                "prior_art_notes": e.get("prior_art_notes"),
            }
            for s, _, mt, e in scored[:args.limit]
        ], indent=2, ensure_ascii=False))
        return

    if claim:
        print(f"Claim: {claim}")
    if tag_hits:
        print("Mapped tags:")
        for t, n in sorted(tag_hits.items(), key=lambda x: -x[1]):
            print(f"  {t} ×{n}")
    else:
        print("(no tag mapped from claim — extend TAG_KEYWORDS in lookup.py)")
    print()
    if not scored:
        print("No matching entries.")
        return
    print(f"Top {min(args.limit, len(scored))} of {len(scored)} matches "
          f"(chronological tiebreak: earlier wins):")
    print("-" * 72)
    for s, _, mt, e in scored[:args.limit]:
        year = (e.get("first_disclosure_date") or "?")[:4]
        draft = " (draft)" if e.get("draft") else ""
        tier = f" tier={e['tier']}" if e.get("tier") == 2 else ""
        print(f"  {year}  {e['canonical_name']:<45.45} score={s} "
              f"{e.get('ip_status', '?'):<14} {e['id']}{draft}{tier}")
        if mt:
            print(f"        tags: {', '.join(sorted(mt))}")
        if e.get("disclosure_citation"):
            cite = e["disclosure_citation"]
            if len(cite) > 200:
                cite = cite[:200] + "…"
            print(f"        cite: {cite}")
        print()


if __name__ == "__main__":
    main()
