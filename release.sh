#!/usr/bin/env bash
# release.sh — quarterly release ceremony for the Free Wearable Corpus
#
# Produces a cryptographically timestamped, third-party-attested release.
# After this script runs successfully, every entry in the tarball is
# functionally citeable as 102 prior art with verifiable pre-existence
# proof.
#
# Usage:
#   ./release.sh <version-tag> [--dry-run]
#
# Requirements:
#   - python3 (3.8+)
#   - openssl (for RFC 3161)
#   - curl
#   - GNU tar (brew install gnu-tar on macOS for `gtar`)
#   - sha256sum
#   - git
#   - ots (OpenTimestamps client): pip install opentimestamps-client

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <version-tag> [--dry-run]"
  exit 1
fi

VERSION="$1"
DRY_RUN=0
if [ "${2:-}" = "--dry-run" ]; then
  DRY_RUN=1
  echo "[dry-run mode]"
fi

if ! echo "$VERSION" | grep -Eq '^v?[0-9]{4}\.(Q[1-4]|[0-9]{2}\.[0-9]{2})$|^v[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "ERROR: version tag '$VERSION' should match YYYY.QN, YYYY.MM.DD, or vX.Y.Z"
  exit 1
fi

RELEASE_DIR="releases/${VERSION}"
TARBALL_NAME="corpus-${VERSION}.tar.gz"
TARBALL_PATH="${RELEASE_DIR}/${TARBALL_NAME}"

# --- preflight ---

echo "=== Preflight ==="
need_tool() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "ERROR: required tool '$1' not found in PATH"
    exit 1
  fi
}
need_tool python3
need_tool openssl
need_tool curl
need_tool sha256sum
need_tool git

if command -v gtar >/dev/null 2>&1; then
  TAR=gtar
elif tar --version 2>/dev/null | grep -q "GNU tar"; then
  TAR=tar
else
  echo "ERROR: GNU tar required (bsdtar lacks --sort)."
  echo "  install with: brew install gnu-tar"
  exit 1
fi
if [ "$DRY_RUN" -eq 0 ]; then
  if ! command -v ots >/dev/null 2>&1; then
    echo "ERROR: 'ots' (OpenTimestamps client) required for non-dry-run."
    echo "  install with: pip install opentimestamps-client"
    exit 1
  fi
fi

if [ ! -f corpus.jsonl ]; then
  echo "ERROR: corpus.jsonl not found. Run from repo root."
  exit 1
fi

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet HEAD 2>/dev/null; then
    echo "ERROR: working tree has uncommitted changes."
    git status --short
    exit 1
  fi
  if git rev-parse "$VERSION" >/dev/null 2>&1; then
    echo "ERROR: tag '$VERSION' already exists."
    exit 1
  fi
fi

if [ -d "$RELEASE_DIR" ] && [ "$DRY_RUN" -eq 0 ]; then
  echo "ERROR: $RELEASE_DIR already exists."
  exit 1
fi

echo "  Preflight OK."

# --- validate ---
echo ""
echo "=== Validate corpus ==="
python3 tools/validate.py corpus.jsonl --strict

# --- regenerate derived artifacts ---
echo ""
echo "=== Regenerate derived artifacts ==="
python3 tools/index.py .
python3 tools/cross_cuts.py

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ 2>/dev/null; then
    echo "WARNING: regenerated artifacts differ from committed versions."
    git diff --name-only CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ | sed 's/^/  /'
    read -p "Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then exit 1; fi
  fi
fi

# --- build deterministic tarball ---
echo ""
echo "=== Build release tarball ==="
mkdir -p "$RELEASE_DIR"

case "$VERSION" in
  *.Q1) MTIME="${VERSION%.Q1}-01-01" ;;
  *.Q2) MTIME="${VERSION%.Q2}-04-01" ;;
  *.Q3) MTIME="${VERSION%.Q3}-07-01" ;;
  *.Q4) MTIME="${VERSION%.Q4}-10-01" ;;
  *.[0-9][0-9].[0-9][0-9]) MTIME=$(echo "$VERSION" | tr '.' '-') ;;
  v*) MTIME=$(date -u +"%Y-%m-%d") ;;
  *) MTIME=$(date -u +"%Y-%m-%d") ;;
esac

$TAR --use-compress-program='gzip -n' -cf "$TARBALL_PATH" \
  --sort=name \
  --owner=0 --group=0 --numeric-owner \
  --mtime="${MTIME}T00:00:00Z" \
  --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
  corpus.jsonl \
  SCHEMA.md \
  OBVIOUSNESS_TEMPLATE.md \
  CORPUS_INDEX.md \
  lineage.json \
  private.jsonl open.jsonl fictional.jsonl academic.jsonl regulatory.jsonl standards.jsonl \
  cross_cuts/ \
  README.md \
  LICENSE \
  CONTRIBUTING.md \
  TIMESTAMPING.md

HASH=$(sha256sum "$TARBALL_PATH" | cut -d' ' -f1)
echo "${HASH}  ${TARBALL_NAME}" > "${RELEASE_DIR}/SHA256SUMS"
echo "  Tarball: ${TARBALL_PATH}"
echo "  SHA-256: ${HASH}"

ENTRIES=$(wc -l < corpus.jsonl)
echo "  Contains: ${ENTRIES} corpus entries"

if [ "$DRY_RUN" -eq 1 ]; then
  echo ""
  echo "=== Dry-run complete ==="
  exit 0
fi

# --- RFC 3161 timestamping ---
echo ""
echo "=== RFC 3161 timestamping ==="
openssl ts -query -data "$TARBALL_PATH" -sha256 -cert -no_nonce \
  -out "${RELEASE_DIR}/request.tsq"

echo "  Submitting to FreeTSA..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    https://freetsa.org/tsr \
    -o "${RELEASE_DIR}/freetsa.tsr"; then
  echo "    OK ($(wc -c < "${RELEASE_DIR}/freetsa.tsr") bytes)"
else
  echo "    WARNING: FreeTSA submission failed."
  rm -f "${RELEASE_DIR}/freetsa.tsr"
fi

echo "  Submitting to DigiCert..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    http://timestamp.digicert.com \
    -o "${RELEASE_DIR}/digicert.tsr"; then
  echo "    OK ($(wc -c < "${RELEASE_DIR}/digicert.tsr") bytes)"
else
  echo "    WARNING: DigiCert submission failed."
  rm -f "${RELEASE_DIR}/digicert.tsr"
fi

if [ ! -f "${RELEASE_DIR}/freetsa.tsr" ] && [ ! -f "${RELEASE_DIR}/digicert.tsr" ]; then
  echo "ERROR: both RFC 3161 submissions failed. Aborting."
  exit 1
fi

# --- OpenTimestamps ---
echo ""
echo "=== OpenTimestamps anchoring ==="
ots stamp "$TARBALL_PATH"
mv "${TARBALL_PATH}.ots" "${RELEASE_DIR}/${TARBALL_NAME}.ots"
echo "  OpenTimestamps proof recorded (initially unconfirmed)."

# --- manifest ---
echo ""
echo "=== Write manifest ==="
cat > "${RELEASE_DIR}/MANIFEST.md" <<EOF
# Release ${VERSION}

| | |
|---|---|
| Date (UTC) | $(date -u +"%Y-%m-%dT%H:%M:%SZ") |
| Tarball | \`${TARBALL_NAME}\` |
| SHA-256 | \`${HASH}\` |
| Entries | ${ENTRIES} |

## Timestamping artifacts

| Layer | File | Status |
|---|---|---|
| RFC 3161 (FreeTSA) | \`freetsa.tsr\` | $([ -f "${RELEASE_DIR}/freetsa.tsr" ] && echo "OK" || echo "skipped") |
| RFC 3161 (DigiCert) | \`digicert.tsr\` | $([ -f "${RELEASE_DIR}/digicert.tsr" ] && echo "OK" || echo "skipped") |
| OpenTimestamps | \`${TARBALL_NAME}.ots\` | OK (initially unconfirmed) |

## What this release attests

The exact byte sequence of \`${TARBALL_NAME}\` (SHA-256 \`${HASH}\`)
existed at or before the timestamps recorded in the .tsr and .ots files.
The contents of that tarball — including \`corpus.jsonl\` with its
${ENTRIES} entries — are therefore public disclosures as of those
timestamps, citable as 102 prior art against any patent with a later
effective filing date.
EOF
echo "  ${RELEASE_DIR}/MANIFEST.md"

# --- git tag ---
echo ""
echo "=== Git tag ==="
git add "$RELEASE_DIR"
git commit -m "release: ${VERSION}

${ENTRIES} corpus entries.
SHA-256: ${HASH}"

git tag -a "$VERSION" -m "Free Wearable Corpus release ${VERSION}

SHA-256: ${HASH}
Entries: ${ENTRIES}"

echo "  Tagged ${VERSION}."

echo ""
echo "=========================================="
echo "  Release ${VERSION} complete."
echo "=========================================="
echo "Next steps:"
echo "  1. Push: git push origin main && git push origin ${VERSION}"
echo "  2. In ~6 hours: ots upgrade ${RELEASE_DIR}/${TARBALL_NAME}.ots"
echo "     then commit the upgraded proof."
echo "  3. Discoverability submissions (see RELEASE_RUNBOOK.md)."
