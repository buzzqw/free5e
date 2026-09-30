#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPOSITORY_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"

export INPUT_LANGUAGE="it-IT"
export INPUT_DATE_FORMAT="%d/%m/%Y"
export INPUT_BOOK_DIRECTORY="it-IT/Characters_Codex"
export INPUT_BOOK_MAIN_FILE="Characters_Codex"
export INPUT_GENERATED_FILES_TARGET_DIRECTORY="generated"
export INPUT_ARTIFACTS_TARGET_DIR="generated"
export GIT_CONFIG_GLOBAL="${TMPDIR:-/tmp}/free5e-conversion-gitconfig"

if command -v ruby >/dev/null 2>&1; then
  RUBY_GEM_BIN="$(ruby -e 'puts Gem.user_dir')/bin"
  if [ -d "${RUBY_GEM_BIN}" ]; then
    export PATH="${RUBY_GEM_BIN}:${PATH}"
  fi
fi

if ! command -v kramdoc >/dev/null 2>&1; then
  printf '%s\n' "Errore: kramdoc non e disponibile nel PATH." >&2
  printf '%s\n' "Installa la gem Ruby kramdown-asciidoc e riprova." >&2
  exit 1
fi

if ! command -v asciidoctor-pdf >/dev/null 2>&1; then
  printf '%s\n' "Errore: asciidoctor-pdf non e disponibile nel PATH." >&2
  printf '%s\n' "Installa la gem Ruby asciidoctor-pdf e riprova." >&2
  exit 1
fi

cd "${REPOSITORY_ROOT}"

"${REPOSITORY_ROOT}/.github/convert-files/conversion-scripts/markdown-to-asciidoc.sh"
"${REPOSITORY_ROOT}/.github/convert-files/conversion-scripts/asciidoc-to-pdf.sh"

PDF_PATH="${REPOSITORY_ROOT}/generated/Characters_Codex/pdf/Characters_Codex.pdf"
if [ ! -s "${PDF_PATH}" ]; then
  printf '%s\n' "Errore: il PDF non e stato creato o e vuoto." >&2
  exit 1
fi

printf '\nPDF creato: %s\n' \
  "${PDF_PATH}"
