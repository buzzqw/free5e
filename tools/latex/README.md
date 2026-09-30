# Conversione Markdown -> D&D LaTeX

`markdown_to_dnd_latex.py` usa solo Python 3 e la libreria standard. Non traduce
il testo e non usa Pandoc: converte la struttura Markdown nei comandi del
template `dndbook` vendorizzato in `tools/latex/dnd`.

Supporta titoli, front matter YAML semplice, paragrafi, corsivo, grassetto,
codice inline, link, immagini, citazioni, liste, tabelle e blocchi di codice.
Con `--follow-links` include anche i link locali a file Markdown.

Esempio per il Vanguard:

```sh
python3 tools/latex/markdown_to_dnd_latex.py \
  it-IT/Characters_Codex/03_Creating_a_Character/Classes/Vanguard/Vanguard.md \
  --include it-IT/Characters_Codex/06_Spellcasting/Spell_Lists/Vanguard_Spells.md \
  --follow-links \
  --title Vanguard \
  --author Free5e \
  --output /tmp/vanguard.tex
```

Per compilare il risultato con il template locale:

```sh
TEXINPUTS=tools/latex/dnd//: lualatex -output-directory=/tmp /tmp/vanguard.tex
```
