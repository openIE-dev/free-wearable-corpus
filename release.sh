#!/usr/bin/env bash
# release.sh — quarterly release ceremony for the Free Wearable Corpus
#
# Produces a cryptographically timestamped, third-party-attested release
# of the corpus, wrapped in a conforming WAI1 binary container with Ed25519
# JWP receipts and Commons Scholar bundle.
#
# Usage:
#   ./release.sh <version-tag> [--dry-run]

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <version-tag> [--dry-run]"
  echo "example: $0 2026.Q3"
  exit 1
fi

VERSION="$1"
DRY_RUN=0
if [ "${2:-}" = "--dry-run" ]; then
  DRY_RUN=1
  echo "[dry-run mode: will build artifacts and compute hash, but skip TSA submissions and git tag]"
fi

if ! echo "$VERSION" | grep -Eq '^v?[0-9]{4}\.(Q[1-4]|[0-9]{2}\.[0-9]{2})$|^v[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "ERROR: version tag '$VERSION' should match YYYY.QN, YYYY.MM.DD, or vX.Y.Z"
  exit 1
fi

RELEASE_DIR="releases/${VERSION}"
TARBALL_NAME="corpus-${VERSION}.tar.gz"
TARBALL_PATH="${RELEASE_DIR}/${TARBALL_NAME}"

# ---------- preflight checks ----------

echo "=== Preflight checks ==="

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
  need_tool ots || {
    echo "ERROR: 'ots' (OpenTimestamps client) required for non-dry-run."
    echo "  install with: pip install opentimestamps-client"
    exit 1
  }
fi

if [ ! -f corpus.jsonl ]; then
  echo "ERROR: corpus.jsonl not found. Run from repo root."
  exit 1
fi

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet HEAD 2>/dev/null; then
    echo "ERROR: working tree has uncommitted changes. Commit or stash first."
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

# ---------- step 1: validate corpus ----------

echo ""
echo "=== Step 1: validate corpus ==="
python3 tools/validate.py corpus.jsonl --strict
echo "  Validation passed."

# ---------- step 2: regenerate derived artifacts ----------

echo ""
echo "=== Step 2: regenerate derived artifacts ==="
STAGE_DIR=""
cleanup_stage() {
  if [ -n "$STAGE_DIR" ] && [ -d "$STAGE_DIR" ]; then
    rm -rf "$STAGE_DIR"
  fi
}
trap cleanup_stage EXIT

if [ "$DRY_RUN" -eq 1 ]; then
  STAGE_DIR=$(mktemp -d)
  cp corpus.jsonl SCHEMA.md OBVIOUSNESS_TEMPLATE.md README.md LICENSE CONTRIBUTING.md TIMESTAMPING.md "$STAGE_DIR/"
  BUILD_ROOT="$STAGE_DIR"
else
  BUILD_ROOT="."
fi

python3 tools/index.py "$BUILD_ROOT"
python3 tools/cross_cuts.py "$BUILD_ROOT"
echo "  Index, lineage, per-corpus mirrors, and cross-cuts regenerated."

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git diff --quiet CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ 2>/dev/null; then
    echo "WARNING: regenerated artifacts differ from committed versions."
    echo "         You probably want to commit these before tagging."
    echo "         Affected files:"
    git diff --name-only CORPUS_INDEX.md lineage.json *.jsonl cross_cuts/ | sed 's/^/           /'
    echo ""
    read -p "Continue anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      exit 1
    fi
  fi
fi

# ---------- step 3: build deterministic release tarball ----------

echo ""
echo "=== Step 3: build release tarball ==="
mkdir -p "$RELEASE_DIR"

case "$VERSION" in
  *.Q1) MTIME="${VERSION%.Q1}-01-01" ;;
  *.Q2) MTIME="${VERSION%.Q2}-04-01" ;;
  *.Q3) MTIME="${VERSION%.Q3}-07-01" ;;
  *.Q4) MTIME="${VERSION%.Q4}-10-01" ;;
  *.[0-9][0-9].[0-9][0-9]) MTIME=$(echo "${VERSION#v}" | tr '.' '-') ;;
  v*) MTIME="2026-01-01" ;;
  *) MTIME="2026-01-01" ;;
esac

$TAR -C "$BUILD_ROOT" --use-compress-program='gzip -n' -cf "$TARBALL_PATH" \
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
echo "  (deterministic: same content + same version tag = same hash)"

ENTRIES=$(wc -l < corpus.jsonl | tr -d ' ')
echo "  Contains: ${ENTRIES} corpus entries"

# ---------- step 3b: emit WAI1 envelope, canonical OpenIE JSONL & Commons bundle ----------

echo ""
echo "=== Step 3b: emit WAI1 envelope & Commons Scholar bundle ==="
WAI_NAME="corpus-${VERSION}.wai"
WAI_PATH="${RELEASE_DIR}/${WAI_NAME}"
EMIT_FLAGS=(
  --version "$VERSION"
  --release-dir "$RELEASE_DIR"
  --tarball "$TARBALL_PATH"
  --corpus "${BUILD_ROOT}/corpus.jsonl"
  --lineage "${BUILD_ROOT}/lineage.json"
  --timestamp "${MTIME}T00:00:00Z"
)
if [ "$DRY_RUN" -eq 1 ]; then
  EMIT_FLAGS+=(--dry-run)
fi
python3 tools/emit_wai_commons.py "${EMIT_FLAGS[@]}"

TARBALL_B3=$(grep "  ${TARBALL_NAME}\$" "${RELEASE_DIR}/BLAKE3SUMS" | cut -d' ' -f1)
WAI_SHA=$(grep "  ${WAI_NAME}\$" "${RELEASE_DIR}/SHA256SUMS" | cut -d' ' -f1)
WAI_B3=$(grep "  ${WAI_NAME}\$" "${RELEASE_DIR}/BLAKE3SUMS" | cut -d' ' -f1)
RECEIPT_SHA=$(grep "  WAI_RECEIPT.json\$" "${RELEASE_DIR}/SHA256SUMS" | cut -d' ' -f1)
RECEIPT_B3=$(grep "  WAI_RECEIPT.json\$" "${RELEASE_DIR}/BLAKE3SUMS" | cut -d' ' -f1)
CANON_SHA=$(grep "  artifacts.canonical.jsonl\$" "${RELEASE_DIR}/SHA256SUMS" | cut -d' ' -f1)
CANON_B3=$(grep "  artifacts.canonical.jsonl\$" "${RELEASE_DIR}/BLAKE3SUMS" | cut -d' ' -f1)
COMMONS_SHA=$(grep "  commons_ingest_bundle.json\$" "${RELEASE_DIR}/SHA256SUMS" | cut -d' ' -f1)
COMMONS_B3=$(grep "  commons_ingest_bundle.json\$" "${RELEASE_DIR}/BLAKE3SUMS" | cut -d' ' -f1)

write_manifest() {
  local manifest_date="$1"
  local commons_status="$2"
  cat > "${RELEASE_DIR}/MANIFEST.md" <<EOF
# Release ${VERSION}

| | |
|---|---|
| Date (UTC) | ${manifest_date} |
| Tarball | \`${TARBALL_NAME}\` |
| Tarball SHA-256 | \`${HASH}\` |
| Tarball BLAKE3 | \`${TARBALL_B3}\` |
| WAI1 Envelope | \`${WAI_NAME}\` |
| WAI1 SHA-256 | \`${WAI_SHA}\` |
| WAI1 BLAKE3 | \`${WAI_B3}\` |
| Entries | ${ENTRIES} |
| Commons Sync | ${commons_status} |

## Release artifacts & digests (\`CC0-1.0\`)

| Artifact | SHA-256 | BLAKE3 |
|---|---|---|
| \`${TARBALL_NAME}\` | \`${HASH}\` | \`${TARBALL_B3}\` |
| \`artifacts.canonical.jsonl\` | \`${CANON_SHA}\` | \`${CANON_B3}\` |
| \`${WAI_NAME}\` | \`${WAI_SHA}\` | \`${WAI_B3}\` |
| \`WAI_RECEIPT.json\` | \`${RECEIPT_SHA}\` | \`${RECEIPT_B3}\` |
| \`commons_ingest_bundle.json\` | \`${COMMONS_SHA}\` | \`${COMMONS_B3}\` |

## Timestamping & cryptographic attestation layers

| Layer | File | Status |
|---|---|---|
| WAI1 + Ed25519 JWP Receipt | \`WAI_RECEIPT.json\` | ✓ |
| RFC 3161 (FreeTSA — tarball) | \`freetsa.tsr\` | $([ -f "${RELEASE_DIR}/freetsa.tsr" ] && echo "✓" || echo "✗ skipped") |
| RFC 3161 (DigiCert — tarball) | \`digicert.tsr\` | $([ -f "${RELEASE_DIR}/digicert.tsr" ] && echo "✓" || echo "✗ skipped") |
| RFC 3161 (FreeTSA — WAI receipt) | \`wai_receipt.freetsa.tsr\` | $([ -f "${RELEASE_DIR}/wai_receipt.freetsa.tsr" ] && echo "✓" || echo "✗ skipped") |
| RFC 3161 (DigiCert — WAI receipt) | \`wai_receipt.digicert.tsr\` | $([ -f "${RELEASE_DIR}/wai_receipt.digicert.tsr" ] && echo "✓" || echo "✗ skipped") |
| OpenTimestamps (tarball) | \`${TARBALL_NAME}.ots\` | $([ -f "${RELEASE_DIR}/${TARBALL_NAME}.ots" ] && echo "✓ (initially unconfirmed)" || echo "✗ skipped") |
| OpenTimestamps (WAI receipt) | \`WAI_RECEIPT.json.ots\` | $([ -f "${RELEASE_DIR}/WAI_RECEIPT.json.ots" ] && echo "✓ (initially unconfirmed)" || echo "✗ skipped") |

## Verification

See \`tools/verify_release.sh\` for the standard verification procedure,
or run individually:

\`\`\`bash
# Verify all SHA-256 digests
sha256sum -c SHA256SUMS

# Offline verify WAI1 header, SPEC §2 limits, BLAKE3 digests, and Ed25519 signatures
python3 ../../tools/emit_wai_commons.py --verify .
\`\`\`

## What this release attests

The exact byte sequences of \`${TARBALL_NAME}\` (SHA-256 \`${HASH}\`, BLAKE3 \`${TARBALL_B3}\`)
and \`${WAI_NAME}\` (SHA-256 \`${WAI_SHA}\`, BLAKE3 \`${WAI_B3}\`) existed at or before the
timestamps recorded in the \`.tsr\` and \`.ots\` files and are bound under the Ed25519
signature in \`WAI_RECEIPT.json\`. The ${ENTRIES} entries in \`corpus.jsonl\` and
\`artifacts.canonical.jsonl\` are public disclosures under \`CC0-1.0\`, citable as
35 U.S.C. 102/103 prior art against any patent with a later effective filing date.
EOF
}

if [ "$DRY_RUN" -eq 1 ]; then
  write_manifest "${MTIME}T00:00:00Z" "dry-run (bundle emitted + non-blocking health ping)"
  echo ""
  echo "=== Dry-run complete ==="
  echo "Tarball built at:      ${TARBALL_PATH}"
  echo "WAI1 envelope at:      ${WAI_PATH}"
  echo "Canonical OpenIE at:   ${RELEASE_DIR}/artifacts.canonical.jsonl"
  echo "Commons bundle at:     ${RELEASE_DIR}/commons_ingest_bundle.json"
  echo "Hashes recorded at:    ${RELEASE_DIR}/SHA256SUMS & ${RELEASE_DIR}/BLAKE3SUMS"
  echo "Manifest recorded at:  ${RELEASE_DIR}/MANIFEST.md"
  echo "Skipped: TSA submissions, OpenTimestamps anchoring, live Commons write, git tag."
  exit 0
fi

# ---------- step 4: RFC 3161 timestamping ----------

echo ""
echo "=== Step 4: RFC 3161 timestamping ==="

openssl ts -query -data "$TARBALL_PATH" -sha256 -cert -no_nonce \
  -out "${RELEASE_DIR}/request.tsq"
openssl ts -query -data "${RELEASE_DIR}/WAI_RECEIPT.json" -sha256 -cert -no_nonce \
  -out "${RELEASE_DIR}/wai_receipt.tsq"

echo "  Submitting tarball & WAI receipt to FreeTSA..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    https://freetsa.org/tsr \
    -o "${RELEASE_DIR}/freetsa.tsr"; then
  echo "    Tarball OK ($(wc -c < "${RELEASE_DIR}/freetsa.tsr") bytes)"
else
  echo "    WARNING: FreeTSA tarball submission failed; continuing with other layers."
  rm -f "${RELEASE_DIR}/freetsa.tsr"
fi

if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/wai_receipt.tsq" \
    https://freetsa.org/tsr \
    -o "${RELEASE_DIR}/wai_receipt.freetsa.tsr"; then
  echo "    WAI receipt OK ($(wc -c < "${RELEASE_DIR}/wai_receipt.freetsa.tsr") bytes)"
else
  rm -f "${RELEASE_DIR}/wai_receipt.freetsa.tsr"
fi

echo "  Submitting tarball & WAI receipt to DigiCert..."
if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/request.tsq" \
    http://timestamp.digicert.com \
    -o "${RELEASE_DIR}/digicert.tsr"; then
  echo "    Tarball OK ($(wc -c < "${RELEASE_DIR}/digicert.tsr") bytes)"
else
  echo "    WARNING: DigiCert tarball submission failed; continuing with other layers."
  rm -f "${RELEASE_DIR}/digicert.tsr"
fi

if curl -sS --max-time 30 --fail \
    -H "Content-Type: application/timestamp-query" \
    --data-binary @"${RELEASE_DIR}/wai_receipt.tsq" \
    http://timestamp.digicert.com \
    -o "${RELEASE_DIR}/wai_receipt.digicert.tsr"; then
  echo "    WAI receipt OK ($(wc -c < "${RELEASE_DIR}/wai_receipt.digicert.tsr") bytes)"
else
  rm -f "${RELEASE_DIR}/wai_receipt.digicert.tsr"
fi

if [ ! -f "${RELEASE_DIR}/freetsa.tsr" ] && [ ! -f "${RELEASE_DIR}/digicert.tsr" ]; then
  echo "ERROR: both RFC 3161 submissions failed. Aborting."
  exit 1
fi

# ---------- step 5: OpenTimestamps Bitcoin anchoring ----------

echo ""
echo "=== Step 5: OpenTimestamps anchoring ==="
ots stamp "$TARBALL_PATH"
if [ "${TARBALL_PATH}.ots" != "${RELEASE_DIR}/${TARBALL_NAME}.ots" ]; then
  mv "${TARBALL_PATH}.ots" "${RELEASE_DIR}/${TARBALL_NAME}.ots"
fi
ots stamp "${RELEASE_DIR}/WAI_RECEIPT.json"
echo "  OpenTimestamps proofs recorded for ${TARBALL_NAME} and WAI_RECEIPT.json (initially unconfirmed)."

# ---------- step 5b: Commons Scholar notification / sync ----------

echo ""
echo "=== Step 5b: Commons Scholar (scholar.askdavidc.ai) sync ==="
python3 tools/emit_wai_commons.py \
  --push-commons-only \
  --version "$VERSION" \
  --release-dir "$RELEASE_DIR"

# ---------- step 6: write release manifest ----------

echo ""
echo "=== Step 6: write manifest ==="
write_manifest "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" "synced / bundle emitted (\`commons_ingest_bundle.json\`)"
echo "  ${RELEASE_DIR}/MANIFEST.md"

# ---------- step 7: git tag ----------

echo ""
echo "=== Step 7: git tag ==="
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
