# Studio del repository

## Struttura

Free5e usa Markdown GitHub-flavored come sorgente. I link locali ai Markdown
sono trasformati in inclusioni durante la conversione, quindi ogni traduzione
deve conservare link, ancore e struttura dei capitoli finché il relativo
percorso italiano non viene approvato.

La conversione automatica passa da Markdown ad AsciiDoc e poi genera HTML, PDF,
EPUB, DocBook, DOCX, ODT e LaTeX. Il workflow riutilizzabile si trova in
`.github/workflows/convert-files.yml`.

## Perimetro rilevato

La sorgente inglese contiene 979 file Markdown nei quattro documenti previsti:

| Documento | File Markdown |
| --- | ---: |
| Character's Codex | 604 |
| Conductor's Companion | 362 |
| Monstrous Manuscript | 12 |
| 5e to Free5e Migration Guide | 1 |

Il `Character's Codex` è il nucleo più grande e contiene classi, ascendenze,
background, incantesimi, equipaggiamento, piani di esistenza e appendici. Il
`Conductor's Companion` è materiale per la conduzione delle partite. Il
`Monstrous Manuscript` contiene mostri, PNG e strumenti per la gestione degli
incontri. La `Migration Guide` è un documento autonomo.

## Localizzazione prevista

Il repository usa directory regionali con codice `lingua-PAESE`; per l'italiano
è appropriato `it-IT`. Le traduzioni esistenti localizzano anche nomi di
directory e file, ma il kit iniziale usa percorsi speculari a `en-US` per
rendere la mappatura automatica e il lavoro incrementale meno rischiosi.

Ogni libro finito deve avere un solo Markdown principale, i capitoli nelle
relative sottodirectory, `Legal.md`, i crediti e un tema PDF nella directory
del libro. Il tema `it-IT/pdf-theme.yml` è un modello da copiare e adattare a
ciascun libro.

## Terminologia e fonti

Il PDF locale `IT_SRD_CC_v5.2.1.pdf` è una fonte terminologica ufficiale per i
concetti che Free5e condivide con l'SRD 5.2.1. Non è sufficiente per i contenuti
originali di Free5e o per il materiale tratto da A5ESRD, Lazy GM's Resource
Document, Kibbles' Compendium of Legends and Legacies e BFRD. Questi casi sono
da verificare contro il testo sorgente e le attribuzioni legali del libro.

Free5e modifica inoltre alcuni nomi di classe e concetti per motivi di
inclusività. `Dreadnought`, `Wodewose`, `Adept` e `Vanguard` non vanno sostituiti
automaticamente con i nomi delle classi SRD: sono decisioni editoriali
specifiche di Free5e e sono marcate nel glossario.

## Controlli tecnici

- cspell usa `it-IT/cspell.config.yaml` e il dizionario locale.
- markdownlint continua a controllare tutti i Markdown del repository.
- Il workflow italiano di conversione salta i libri finché il loro Markdown
  principale non esiste.
- Le attribuzioni vanno completate libro per libro prima della pubblicazione.
