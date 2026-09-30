# Criteri di traduzione

## Priorità delle fonti

1. Usare la terminologia del `System Reference Document 5.2.1` italiano quando
   il concetto è presente nel PDF.
2. Mantenere la stessa resa italiana in tutto il repository, aggiornando prima
   `glossary.csv` quando emerge una variante.
3. Segnalare come `da approvare` i nomi e i concetti specifici di Free5e o delle
   altre fonti, senza presentarli come terminologia ufficiale SRD.

## Stile

- Usare un italiano naturale e inclusivo senza schwa o grafie sperimentali.
- Preferire forme neutre, plurali e perifrasi quando evitano un genere non
  necessario.
- Conservare dadi, numeri, unità, marcatori Markdown, tabelle, link e ancore.
- Non tradurre gli identificatori tecnici dei link finché la struttura italiana
  non viene approvata; il file `translation_status.csv` usa percorsi speculari.
- Tradurre i nomi propri descrittivi solo dopo aver verificato che non siano
  nomi propri dell'ambientazione o riferimenti a una fonte esterna.

## Procedura consigliata

1. Approvare le righe `da approvare` in `glossary.csv`.
2. Aprire una conversazione separata per ogni capitolo. Non accumulare più
   capitoli nella stessa conversazione, per evitare di saturare il contesto.
3. All'inizio di ogni conversazione leggere `translation_status.csv`, il
   glossario e il capitolo sorgente completo prima di tradurre.
4. Tradurre un capitolo alla volta, partendo dal `Character's Codex`.
5. Aggiornare `translation_status.csv` dopo ogni file completato.
6. Aggiungere in `dictionary.txt` solo nomi propri o termini fantastici, non
   termini che dovrebbero invece stare nel glossario.
7. Eseguire cspell e markdownlint prima di ogni merge.

Ogni capitolo deve essere consegnato con una breve nota sui termini nuovi,
sulle decisioni editoriali e sugli eventuali riferimenti da verificare nel
capitolo successivo. La continuità tra conversazioni deve dipendere dai file
del repository, non dalla cronologia della chat.

Il materiale sotto `it-IT` è una base di lavoro e non costituisce una versione
pubblicabile finché i testi non sono stati tradotti e revisionati.

## Bardo

- La terminologia di classe e dei collegi segue le voci già approvate nel glossario: `bardo`, `collegio bardico`, `Collegio del Sapere` e `Collegio dei Folli`.
- I nomi dei privilegi specifici di Free5e sono stati resi in italiano per questa prima versione; richiedono una revisione editoriale insieme alle altre classi.
- `Vicious Mockery` è stato mantenuto come `Beffa crudele`, in coerenza con la traduzione già usata in `How_to_Play.md`.
- La classe contiene riferimenti alla futura traduzione della lista degli incantesimi, delle descrizioni degli incantesimi e della tabella degli slot da incantatore completo.

## Chierico

- La terminologia della classe segue il glossario approvato: `chierico`, `dominio divino`, `Incanalare divinità`, `incantesimi da chierico`, `Dominio del martirio` e `mandato sacro`.
- I nomi degli incantesimi sono stati tradotti usando la terminologia italiana disponibile; gli anchor tecnici sono stati mantenuti invariati.
- I privilegi specifici di Free5e e i nomi dei Mandati sacri richiedono una revisione editoriale insieme alle altre classi.
- I riferimenti alla lista degli incantesimi, alle descrizioni degli incantesimi e alla tabella degli slot da incantatore completo restano in attesa delle rispettive traduzioni.

## Classi

- La tabella mantiene i nomi Free5e già approvati per Adepto, Dreadnought, Vanguard e Wodewose; le altre classi seguono la terminologia italiana del glossario.
- I link alle classi e sezioni non ancora tradotte mantengono i percorsi e gli identificatori dei file inglesi, in attesa della creazione delle rispettive destinazioni italiane.
- La distinzione tra `Metà` e `Completo` nella colonna del lancio degli incantesimi segue rispettivamente i mezzi incantatori e gli incantatori completi.

## Tabella degli slot per incantatore completo

- Gli ordinali dei livelli e l'intestazione della tabella sono stati adattati alla notazione italiana già usata nelle tabelle delle classi; i valori numerici e i trattini sono invariati.
- Il file non contiene riferimenti o collegamenti ancora da tradurre.

## Tabella degli slot per mezzo incantatore

- Sono state mantenute la notazione italiana degli ordinali, la struttura della tabella e i valori degli slot del sorgente; il file non contiene riferimenti o collegamenti da tradurre.

## Vanguard: Giuramento di devozione

- La terminologia segue le voci approvate `Vanguard`, `Giuramento di devozione`, `Incanalare divinità` e `incantesimi da Vanguard`; i privilegi specifici sono stati tradotti come `Arma sacra`, `Scacciare i profani`, `Aura di devozione`, `Purezza dello spirito` e `Nimbo sacro`, in attesa di revisione editoriale.
- I nomi visibili dei cinque incantesimi e del riferimento a Protezione dal bene e dal male sono stati tradotti, mantenendo invariati link e anchor tecnici; le rispettive descrizioni degli incantesimi non sono ancora tradotte.

## Vanguard: Giuramento dell'esemplare

- La terminologia di classe usa `Vanguard` e `Giuramento dell'esemplare`; i principi e i privilegi specifici sono stati tradotti come `Principi dell'esemplarismo`, `Manto del silenzio`, `Santuario del sacrosanto`, `Aura di serenità`, `Rimprovero` e `Mondo ordinato`, in attesa di revisione editoriale.
- `Nullify Sense` è stato reso come `Sopprimere un senso`; i nomi visibili degli incantesimi e il collegamento a `Aura di serenità` mantengono invariati gli anchor tecnici. Le descrizioni degli incantesimi e la sezione Allineamento sono ancora riferimenti futuri.

## Dreadnought

- Sono stati mantenuti i nomi Free5e `Dreadnought` e i termini approvati `Cammino del berserker` e `Cammino del drago`.
- I termini delle condizioni e dei tipi di danno conservano i relativi anchor tecnici e i marcatori HTML del renderer.
- Il sorgente contiene alcuni riferimenti a terminologia e contenuti ancora da verificare nel capitolo degli incantesimi e nelle classi successive.

## Guerriero

- La classe e gli archetipi usano la terminologia approvata `guerriero`, `picchiatore`, `campione`, `stile di combattimento`, `Attacco extra` e `archetipi marziali`.
- I nomi degli stili di combattimento sono stati tradotti nei testi visibili, mantenendo invariati i percorsi dei file sorgente ancora da tradurre.
- I marcatori HTML per goblin e condizioni, gli anchor tecnici e i riferimenti alle sezioni future sono stati conservati.

## Ranger

- La terminologia segue il glossario approvato per `ranger`, `cacciatore`, `cacciatore di taglie`, `Attacco extra`, `stile di combattimento` e `archetipi del ranger`.
- I nomi degli incantesimi e delle capacità sono stati tradotti nei testi visibili, mentre percorsi e anchor tecnici restano invariati.
- Sono stati mantenuti i marcatori HTML per mostri, condizioni e incantesimi; i riferimenti a liste degli incantesimi e classi future richiedono revisione quando saranno tradotti.

## Ladro

- La terminologia segue il glossario approvato per `ladro`, `assassino`, `maestria` ed `Elusione`; i nomi dei privilegi sono stati tradotti nei testi visibili.
- I percorsi e gli anchor tecnici dei riferimenti ad attrezzi, condizioni, mostri, incantesimi e sezioni future sono stati mantenuti invariati.
- I riferimenti a strumenti e alle sezioni di esplorazione e combattimento dipendono dalla futura traduzione dei capitoli corrispondenti.
- Nel titolo del privilegio Aumento dei punteggi di caratteristica è stato reinserito il 19° livello, presente nella tabella e nel testo del sorgente ma omesso accidentalmente dal titolo inglese.

## Stregone

- Sono stati tradotti tutti gli 11 file della classe, delle origini e della Metamagia; i nomi dei file `Enpowered_Spell.md` e `Hightened_Spell.md` mantengono volutamente gli errori ortografici presenti nei percorsi sorgente.
- La terminologia usa `stregone`, `origine stregonesca`, `fonte della magia` e `Metamagia` come indicato nel glossario.
- I nomi degli incantesimi, le condizioni, i marcatori HTML, i link e gli anchor tecnici sono stati conservati o tradotti solo nel testo visibile.
- `parasense` è stato reso come `parasenso`; il termine è specifico di Free5e e va verificato durante la revisione del capitolo dei sensi e dell'esplorazione.

## Vanguard

- La terminologia usa `Vanguard`, `Giuramento del dovere`, `Incanalare divinità`, `incantesimi da Vanguard`, `mezzo incantatore` e i privilegi tradotti `Senso divino`, `Imposizione delle mani`, `Punizione divina` e `Tocco purificatore`.
- I nomi degli stili di combattimento, degli incantesimi e dei privilegi sono stati tradotti nei testi visibili, mantenendo invariati percorsi e anchor tecnici; la lista degli incantesimi da Vanguard e le descrizioni degli incantesimi restano riferimenti futuri.
- L'espressione danneggiata del sorgente `1d8? radiant damage` è stata resa come `1d8` danni radiosi per mantenere una marcatura Markdown valida senza alterare il valore numerico.

## Warlock: Deflagrazione agonizzante

- L'invocazione `Agonizing Blast` è stata resa come `Deflagrazione agonizzante`; `Eldritch Blast` è stato tradotto come `Deflagrazione occulta`, mantenendo invariato l'anchor tecnico.
- La descrizione collegata di `Eldritch Blast` non è ancora tradotta e resta un riferimento futuro.

## Warlock: Armatura delle ombre

- L'invocazione `Armor of Shadows` è stata resa come `Armatura delle ombre`; `Mage Armor` è stata resa come `Armatura magica` nel testo visibile, mantenendo invariato l'anchor tecnico.
- La descrizione collegata di `Mage Armor` non è ancora tradotta e resta un riferimento futuro.

## Warlock: Passo ascendente

- L'invocazione `Ascendant Step` è stata resa come `Passo ascendente`; `Levitate` è stata resa come `Levitazione` nel testo visibile, mantenendo invariato l'anchor tecnico.
- La descrizione collegata di `Levitate` non è ancora tradotta e resta un riferimento futuro.

## Warlock: Influenza ammaliante

- `Beguiling Influence` è stata resa come `Influenza ammaliante`; le abilità `Deception` e `Persuasion` seguono i termini approvati `Inganno` e `Persuasione`.
- Il file non contiene link, anchor o riferimenti ancora da tradurre.

## Warlock: Accordo bestiale

- `Bestial Accord` è stata resa come `Accordo bestiale`; `Converse with Animals` è stata resa come `Parlare con gli animali` nel testo visibile, mantenendo invariato l'anchor tecnico.
- La descrizione dell'incantesimo `Converse with Animals` non è ancora tradotta e resta un riferimento futuro.

## Warlock: Sussurri ammalianti

- `Bewitching Whispers` è stata resa come `Sussurri ammalianti`; il prerequisito e la formulazione sul recupero dopo un riposo lungo seguono lo stile delle invocazioni precedenti.
- `Compulsion` è stata resa come `Costrizione` nel testo visibile, mantenendo invariato l'anchor tecnico; la descrizione dell'incantesimo non è ancora tradotta e resta un riferimento futuro.

## Warlock: Legame del maestro della catena

- `Bond of the Chain Master` è stato reso come `Legame del maestro della catena`; `Pact of the Chain` è stato reso come `Patto della Catena` nel testo visibile, mantenendo invariato l'anchor tecnico.
- Sono stati mantenuti i termini approvati `famiglio`, `telepatia`, `piano di esistenza` e `linguaggio dei segni`; la descrizione del Patto della Catena è ora disponibile nel relativo file italiano.

## Warlock: invocazioni successive

- I titoli sono stati resi come `Libro degli antichi segreti`, `Catene di Carceri`, `Vista del diavolo`, `Parola terribile`, `Vista mistica`, `Lancia mistica`, `Occhi del custode delle rune`, `Vigore immondo`, `Sguardo di due menti` e `Bevitore di vita`.
- La terminologia segue il glossario per `rituale`, `incantesimo da warlock`, `gittata`, `danni necrotici`, `Carisma`, `sensi`, `piano di esistenza` e la condizione `soppresso`; i termini visibili `Patto del Tomo`, `Patto della Catena` e `Patto della Lama` mantengono invariati i rispettivi anchor tecnici.
- Le descrizioni degli incantesimi `Hold Monster`, `Confusion`, `Detect Magic` e `False Life`, la classe Warlock completa e la sezione dei piani di esistenza non sono ancora tradotte e restano riferimenti futuri.

## Warlock: invocazioni, patti e Immondo

- Sono stati tradotti i 20 file successivi, dalle invocazioni `Mask of Many Faces` a `Witch Sight`, dall'indice delle suppliche, dai tre Patti e dal patrono `The Fiend`; i nomi dei file restano invariati.
- La terminologia segue il glossario per `suppliche occulte`, `incantesimi da warlock`, `slot incantesimo`, `patrono`, `immondo`, condizioni, danni e piani di esistenza. I titoli visibili dei collegamenti sono stati uniformati ai titoli dei file italiani.
- Percorsi relativi, anchor tecnici e marcatori HTML sono invariati. Le descrizioni degli incantesimi collegati, la classe Warlock completa e altri riferimenti non ancora tradotti restano da completare e revisionare.

## Warlock, Wizard, Wodewose, culture ed equipaggiamento

- Sono stati tradotti i 50 file successivi, dalle sezioni `The Overseer` e `Warlock` fino a `Mounts and Vehicles`, comprendendo Wizard, Wodewose, stili di combattimento, creazione del personaggio, culture, determinazione dei punteggi, disabilità ed equipaggiamento.
- La terminologia usa le voci approvate `Warlock`, `Mago`, `Arcanista`, `Teurgo`, `Wodewose`, `circoli del Wodewose`, `stile di combattimento`, `culture`, `equipaggiamento da avventura`, `armatura` e `oggetti assistivi`. Il titolo esterno `Limitless Heroics - Including Characters with Disabilities, Mental Illness, and Neurodivergence in Fifth Edition` è mantenuto in originale come riferimento bibliografico.
- Sono stati mantenuti valori numerici, unità, tabelle, percorsi relativi, anchor tecnici, marcatori HTML e codice inline; le formule nei blocchi di codice sono state tradotte quando contenevano testo descrittivo.
- Restano riferimenti futuri le liste e descrizioni degli incantesimi, le sezioni di esplorazione e combattimento, le sezioni di equipaggiamento non incluse in questo gruppo e gli altri contenuti ancora `non iniziato`.

## Equipaggiamento e talenti: prima tranche

- Sono stati tradotti i 50 file successivi, da `Selling Treasure` a `Stealth Expert`, includendo equipaggiamento, tabelle delle armi e i primi talenti.
- La terminologia delle armi e delle proprietà segue il glossario e la resa italiana SRD: `falcione`, `mazza chiodata`, `portata`, `lancio`, `a due mani` e `accurata`; i valori, le unità e la struttura delle tabelle sono invariati.
- I nomi dei talenti sono stati tradotti nei testi visibili, mentre percorsi relativi, anchor tecnici, marcatori HTML e riferimenti a sezioni future restano invariati. I riferimenti alle descrizioni degli incantesimi e alle sezioni di combattimento/esplorazione non ancora tradotte richiedono verifica successiva.

## Talenti, caratteristiche, avventura, piani e incantesimi A

- Sono stati tradotti i 50 file successivi, da `Street_Fighter` a `Alter_Self`, includendo i talenti conclusivi, ispirazione e fortuna, lingue, avanzamento di livello, uso dei punteggi di caratteristica, avventura, combattimento, esplorazione, piani di esistenza e i primi cinque incantesimi della sezione A.
- La terminologia segue il glossario per `talento`, `prova di caratteristica`, `vantaggio`, `svantaggio`, `bonus di competenza`, `tiro salvezza`, `combattimento`, `esplorazione`, `piani di esistenza`, `incantesimo` e i tipi di danno. I nomi specifici dei talenti e degli incantesimi sono stati tradotti nel testo visibile, mantenendo invariati nomi file, percorsi e anchor tecnici.
- Sono stati conservati struttura Markdown, tabelle, valori numerici, codice inline, marcatori HTML, anchor tecnici e metadati degli incantesimi. Restano riferimenti futuri alle condizioni, alle descrizioni e alle liste degli incantesimi e ad alcune sezioni di classe; i valori tecnici inglesi dei metadati e i nomi da verificare `cloaker`, `bugbear`, `Feywild` e `Shadowfell` restano da controllare durante la revisione.

## Tranche A-E completata

- Le 100 traduzioni iniziali dalla sezione `Animal Friendship` a `Emma's Irresistible Dance` sono state completate e marcate come `tradotto`; restano da revisionare.

## Incantesimi E-F: prima tranche

- Sono stati tradotti `Enhance Ability`, `Enlarge/Reduce`, `Entangle`, `Enthrall`, `Etherealness`, `Expeditious Retreat`, `Eyebite`, l'indice E, `Fabricate` e `Faerie Fire`.
- La terminologia segue il glossario per `punteggio di caratteristica`, `vantaggio`, `svantaggio`, `tiro salvezza`, `terreno difficile`, `trattenuto`, `Piano Etereo`, `Scatto`, `danni da forza`, `strumenti da artigiano` e `impercettibile (vista)`. I nomi dei privilegi degli incantesimi sono stati tradotti nel testo visibile, mentre percorsi, anchor, classi HTML e metadati tecnici restano invariati.
- I valori tecnici dei metadati e gli identificatori English-only, inclusi `spell_name`, le scuole magiche, i valori booleani e gli anchor dei collegamenti, restano inevitabilmente in inglese. `cspell` e `markdownlint` non sono disponibili nell'ambiente, quindi non è stato possibile eseguire quei controlli automatici.

## Incantesimi F: seconda tranche

- Sono stati tradotti `False Life`, `Fear`, `Feather Fall`, `Find Familiar`, `Find Steed`, `Find Traps`, `Find the Path`, `Finger of Death`, `Fiona's Freezing Sphere` e `Fire Bolt`; la terminologia segue il glossario per condizioni, danni, prove, taglie, tipi di creatura, evocazione e lancio degli incantesimi.
- I riferimenti ancora inglesi nei metadati, inclusi nomi incantesimo, scuole, unità, valori booleani, formule e identificatori, sono tecnici e inevitabili; è stato mantenuto anche il commento storico `previously "Freezing Sphere"`. I nomi file, i percorsi, gli anchor e i marcatori HTML restano invariati.
- `cspell` e `markdownlint` non sono installati nell'ambiente, quindi non è stato possibile eseguire quei controlli automatici.

## Incantesimi F-G: terza tranche

- Sono stati resi `Fire Shield` come `Scudo di fuoco`, `Flame Strike` come `Colonna di fuoco` e `Forbiddance` come `Interdizione`; le altre denominazioni seguono lo stesso criterio descrittivo e la terminologia SRD già adottata.
- Sono stati mantenuti invariati metadati tecnici, nomi file, percorsi, anchor e marcatori HTML; i termini specialistici nuovi restano da revisionare.

## Incantesimi G-H: quarta tranche

- Sono stati tradotti i 20 file da `Glibness` a `Heat Metal`, inclusi gli indici `G`; i nomi file, i percorsi, gli anchor, i marcatori HTML e i metadati tecnici restano invariati.
- Le rese terminologiche principali sono `Loquacità`, `Globo di invulnerabilità`, `Glifo di interdizione`, `Bacche benefiche`, `Unto`, `Impercettibilità superiore`, `Ristorare superiore`, `Guardiano della fede`, `Guardie e interdizioni`, `Guida`, `Dardo tracciante`, `Folata di vento`, `Santificare`, `Terreno illusorio`, `Nuocere`, `Velocità`, `Cura`, `Parola guaritrice` e `Scaldare metallo`; seguono lo stile SRD e richiedono revisione editoriale.

## Incantesimi H-I: quinta tranche

- Sono stati tradotti i 20 file da `Hellish Rebuke` a `Iz’zart's Swarm Limb`, inclusi gli indici `H` e `I`; le rese specifiche `Maledizione`, `Blocca mostri`, `Blocca persone`, `Prigionia` e `Arto dello sciame di Iz’zart` restano da revisionare editorialmente.
- Metadati, nomi file, percorsi, anchor tecnici, marcatori HTML e valori sono invariati; le label visibili dei collegamenti sono state tradotte secondo il glossario e lo stile delle tranche precedenti.

## Incantesimi J-M: sesta tranche

- Sono stati tradotti i 20 file da `Jess's Private Sanctum` a `Magic Jar`, inclusi gli indici `J`, `K` e `L`.
- Le rese principali sono `Santuario privato di Jess`, `Scassinare`, `Conoscenza delle leggende`, `Ristorare inferiore`, `Individuare creatura`, `Passo lungo`, `Armatura magica`, `Mano magica`, `Cerchio magico` e `Giara magica`; i nomi specifici restano da revisionare editorialmente.
- Metadati tecnici, nomi file, percorsi, anchor, marcatori HTML e valori sono invariati; le label visibili dei collegamenti seguono la terminologia già adottata.

## Incantesimi M: settima tranche

- Sono stati tradotti i 20 file da `Magic Missile` a `Misty Step`; le rese principali includono `Dardo incantato`, `Bocca magica`, `Arma magica`, `Guarigione di massa`, `Pioggia di meteore`, `Mente vuota` e `Passo velato`.
- Le label visibili di condizioni, scuole, sensi e incantesimi collegati seguono il glossario (`soppresso`, `impercettibile (vista)`, `visione del vero`); nomi file, percorsi, anchor, HTML, metadati e valori tecnici restano invariati.

## Incantesimi M-N-P: ottava tranche

- Sono stati tradotti i 20 file da `Modify Memory` a `Plane Shift`, inclusi gli indici `M` e `N`.
- Le rese terminologiche principali sono `Modificare la memoria`, `Raggio di luna`, `Mano di Morscheck`, `Evocazione istantanea di Natalex`, `Arte della natura`, `Sopprimere un senso`, `Passare senza tracce`, `Passaparete`, `Percepire l'impercettibile`, `Alleato planare`, `Legame planare` e `Spostamento planare`; i termini specifici restano da revisionare editorialmente.
- Metadati tecnici, nomi file, percorsi, anchor, marcatori HTML e valori sono invariati; le label visibili dei collegamenti sono state tradotte secondo il glossario e lo stile delle tranche precedenti.

## Incantesimi P-R: nona tranche

- Sono stati tradotti i 20 file da `Plant Growth` a `Raise Dead`, inclusi gli indici `P` e `Q`.
- Le rese principali sono `Crescita vegetale`, `Metamorfosi`, `Parola del potere: uccidere`, `Muro prismatico`, `Protezione dal bene e dal male`, `Interrogare i morti` e `Rianimare morti`; seguono il glossario e richiedono revisione editoriale.
- Metadati tecnici, nomi file, percorsi, anchor, marcatori HTML e valori sono invariati; le label visibili dei collegamenti sono state tradotte.

## Incantesimi R-S: decima tranche

- Sono stati tradotti i 20 file da `Rantock's Telepathic Bond` a `Sequester`, inclusi gli indici `R` e le descrizioni degli incantesimi R-S.
- Le rese principali sono `Legame telepatico di Rantock`, `Raggio debilitante`, `Raggio di gelo`, `Rianimare`, `Scrutare`, `Apparenza`, `Inviare` e `Sequestrare`; la terminologia specifica resta da revisionare editorialmente.
- Metadati, nomi file, percorsi, anchor, marcatori HTML, tabelle e valori sono invariati; le label visibili dei collegamenti sono state tradotte.

## Incantesimi S: undicesima tranche

- Sono stati tradotti i 20 file da `Shapechange` a `Stoneskin`; i metadati tecnici, i nomi file, i percorsi e gli anchor restano invariati.
- Le rese principali sono `Cambiamento di forma`, `Frantumare`, `Scudo della fede`, `Randello incantato`, `Stretta folgorante`, `Tempesta di nevischio`, `Guardiani spirituali` e `Pelle di pietra`; seguono il glossario e lo stile delle tranche precedenti e restano da revisionare editorialmente.

## Incantesimi S-T: dodicesima tranche

- Sono stati tradotti i 20 file da `Storm of Vengeance` a `True Strike`, inclusi gli indici `S` e `T`; nomi file, percorsi, anchor, marcatori HTML, metadati e valori tecnici restano invariati.
- Le rese terminologiche principali sono `Tempesta di vendetta`, `Suggestione`, `Raggio di sole`, `Esplosione solare`, `Simbolo`, `Telecinesi`, `Teletrasporto`, `Cerchio di teletrasporto`, `Onda tonante`, `Passo arboreo`, `Metamorfosi vera`, `Resurrezione vera`, `Visione del vero` e `Colpo accurato`; i termini specifici restano da revisionare editorialmente.

## Incantesimi U-W: tredicesima tranche

- Sono stati tradotti i 20 file da `Unseen Servant` a `Word of Recall`, inclusi gli indici `U`, `V` e `W`.
- Le rese principali sono `Servitore invisibile`, `Tocco vampirico`, `Beffa crudele`, `Muro di fuoco`, `Muro di forza`, `Muro di ghiaccio`, `Muro di pietra`, `Muro di spine`, `Legame protettivo`, `Respirare sott'acqua`, `Camminare sull'acqua`, `Ragnatela`, `Bizzarro`, `Camminare nel vento`, `Muro di vento`, `Desiderio` e `Parola del richiamo`; i termini specifici restano da revisionare editorialmente.
- Metadati, nomi file, percorsi, anchor tecnici, marcatori HTML, tabelle e valori sono invariati; le label visibili dei collegamenti sono state tradotte secondo glossario e stile delle tranche precedenti.

## Incantesimi, condizioni e conversioni tra sistemi

- Sono stati tradotti i 20 file assegnati dalle righe 582-601, completando la sezione Z degli incantesimi, le liste degli incantesimi, il capitolo sul lancio degli incantesimi, le condizioni, le conversioni tra sistemi, l'appendice e i materiali introduttivi del Codice del personaggio.
- Le rese principali seguono il glossario e i campioni esistenti: `Zona di verità`, `lancio degli incantesimi`, `condizione`, `indebolimento`, `impercettibile`, `soppresso`, `incantesimi da Bardo/Chierico/Ranger/Stregone/Vanguard/Warlock/Mago/Wodewose` e i termini delle fonti A5E, ToV e D&D 2024.
- Sono stati mantenuti invariati nomi file, percorsi, anchor tecnici, marcatori HTML, metadati tecnici, valori, tabelle e commenti tecnici. I nomi specifici di Free5e e delle fonti esterne, come `Wyrd`, `Wodewose`, nomi propri degli incantesimi e terminologia di conversione, richiedono revisione editoriale.

## Codice del personaggio e Compendio del Conduttore: prima tranche

- Sono stati tradotti i 20 file assegnati dalle righe 602-621, comprendendo crediti, fonti, note legali, introduzione, creazione del gruppo di gioco di ruolo da tavolo e prime sezioni sulla costruzione della campagna.
- Le rese principali adottano `Conduttore`, `persone giocanti`, `gioco di ruolo da tavolo`, `campagna a spirale`, `fronti della campagna` e `background`; i titoli visibili dei link sono stati tradotti, mentre percorsi, anchor, nomi propri, URL, commenti tecnici, HTML e valori della tabella restano invariati.
- Restano intenzionalmente in inglese i nomi propri, i titoli delle fonti esterne, le licenze, i riferimenti bibliografici e gli identificatori tecnici; `TODO`, `TTRPG`, `LFG` e `VTT` sono stati conservati o spiegati nel testo per continuità e riconoscibilità. `cspell` e `markdownlint` non risultano installati nell'ambiente, quindi non è stato possibile eseguire quei controlli automatici.

## Compendio del Conduttore: preparazione della campagna e Sessione zero

- Sono stati tradotti i 20 file assegnati dalle righe 622-641, comprendendo i pitch e le tabelle della campagna a spirale, il processo e il kit di preparazione del gioco di ruolo e le sezioni della Sessione zero su personaggi, patroni, avventure brevi e strumenti di sicurezza.
- Le rese terminologiche principali sono `pitch della campagna`, `campagna a spirale`, `luogo di partenza`, `patrono del gruppo`, `persone giocanti`, `Sessione zero`, `strumenti di sicurezza`, `limiti invalicabili` e `contenuti fuori scena`; i nomi propri e i termini tecnici Free5e restano da revisionare.
- Sono stati mantenuti percorsi relativi, nomi file, anchor tecnici, commenti di controllo, URL, HTML, tabelle e valori. Restano in inglese i nomi delle risorse esterne e i relativi identificatori; `cspell` e `markdownlint` non risultano installati nell'ambiente.

## Compendio del Conduttore: costruzione degli incontri

- Sono stati tradotti i 20 file assegnati dalle righe 642-661, comprendendo l'avvio della campagna, il generatore di spunti, la costruzione degli incontri di combattimento, gli elementi ambientali, la gestione delle orde e le tabelle di combinazione dei mostri.
- Le rese principali adottano `GS`, `incontro`, `potenziale letalità`, `persone giocanti`, `elementi dell'incontro`, `manopole della difficoltà`, `boss`, `gregari` e `Conduttore`; i nomi specifici dei mostri e i termini Free5e restano da revisionare.
- Sono stati mantenuti percorsi relativi, nomi file, anchor tecnici, classi HTML, commenti di controllo, valori, formule, tabelle e marcatori Markdown. `cspell` e `markdownlint` non risultano installati nell'ambiente.

## Compendio del Conduttore: incontri avanzati, preparazione e oggetti magici

- Sono stati tradotti i 20 file delle righe 662-681, dalle combinazioni di mostri per sei personaggi fino alla creazione degli oggetti magici senzienti.
- Le rese principali adottano `PNG`, `fasce di gioco`, `modelli di missione`, `segreti e indizi`, `luoghi fantastici`, `ricompense`, `tesoro` e `oggetti magici senzienti`; i termini specifici restano da revisionare.
- Sono stati mantenuti percorsi, nomi file, anchor, HTML, tabelle, valori e commenti tecnici. `cspell` e `markdownlint` non risultano installati nell'ambiente, quindi non è stato possibile eseguire quei controlli automatici.

## Compendio del Conduttore: incontri e teatro della mente

- Sono stati tradotti i 20 file delle righe 682-701, dagli oggetti magici senzienti alle linee guida per il teatro della mente, inclusi gli incontri di combattimento e i trucchi rapidi.
- Le rese principali adottano `danni continuativi`, `vantaggio cinematografico`, `persone giocanti`, `teatro della mente`, `attacchi di opportunità`, `copertura` e `gittata`; i termini specifici restano da revisionare.
- Sono stati mantenuti percorsi relativi, nomi file, valori, tabelle, marcatori Markdown e il commento tecnico `spell-checker:words aphantasia`.

## Compendio del Conduttore: esplorazione, sotterranei e piani interni

- Sono stati tradotti i 20 file delle righe 702-721, includendo l'esplorazione di sotterranei, i dettagli ambientali, i viaggi tra i piani e il Piano Materiale.
- Le rese principali adottano `sotterraneo`, `piani Interni`, `Piani Elementali`, `Caos Elementale`, `Piano Vitale`, `Piano del Vuoto` e i nomi degli incantesimi già presenti nel glossario e nei file italiani.
- Sono stati mantenuti invariati percorsi relativi, nomi file, anchor, classi HTML, valori e il commento tecnico `TODO`; i termini specifici dei piani restano da revisionare.
- I quattro collegamenti dall'indice dell'esplorazione verso sezioni future restano riferimenti non ancora disponibili, coerentemente con i sorgenti e con le righe successive dello stato.

## Compendio del Conduttore: piani esterni, Sottosuolo, città e terre selvagge

- Sono stati tradotti i 20 file delle righe 722-741, comprendendo i piani esterni e transitivi, le sensazioni planari, le spedizioni nel Sottosuolo, le avventure urbane, il viaggio nelle terre selvagge e la richiesta di prove.
- Le rese principali adottano `Piani Esterni`, `Piani transitivi`, `Feywild`, `Shadowfell`, `Sottosuolo`, `fasce`, `dintorni danneggiabili` e `persone giocanti`; i termini specifici dei piani e delle sezioni future restano da revisionare.
- Sono stati mantenuti invariati percorsi relativi, nomi file, anchor, HTML, commenti tecnici, valori, tabelle e marcatori Markdown. Le sezioni ancora non trasferite dal documento Google conservano l'avviso tradotto.

## Compendio del Conduttore: gestione della partita, incontri sociali, improvvisazione e oggetti magici

- Sono stati tradotti i 20 file delle righe 742-761, comprendendo la gestione della partita, gli incontri sociali, gli strumenti per l'improvvisazione e l'attivazione e la sintonia degli oggetti magici.
- Le rese principali adottano `Sventura`, `CD`, `GS`, `danni statici`, `dispositivi assistivi` e `sintonia`; i termini specifici e le scelte inclusive restano da revisionare.
- Sono stati mantenuti percorsi relativi, nomi file, anchor tecnici, commenti, HTML, tabelle, formule e valori. Gli avvisi sul trasferimento dal documento Google restano presenti nei file interessati.

## Compendio del Conduttore: uso degli oggetti magici e oggetti A-B

- Sono stati tradotti i 20 file delle righe 762-781, comprendendo le regole per usare, indossare e impugnare oggetti magici, gli oggetti magici da `Adamantine Armor` a `Arrow-Catching Shield` e gli avvisi di trasferimento per i quattro sacchetti.
- Le rese principali adottano `sintonia`, `Classe Armatura`, `munizioni`, `armatura`, `oggetto meraviglioso`, `Conduttore`, `danni contundenti`, `danni perforanti` e `danni taglienti`; metadati, percorsi, identificatori, anchor e nomi file restano invariati.

## Compendio del Conduttore: oggetti magici B-C

- Sono stati tradotti i 20 file delle righe 782-801, dagli oggetti `Bead of Force` a `Cape of the Mountebank`, inclusi l'indice B e i due oggetti con descrizione completa.
- Le rese principali adottano `Perla della forza`, `Cintura dei nani`, `stivali elfici`, `sintonia`, `elementali dell'acqua` e `elementali del fuoco`; i nomi specifici restano da revisionare.
- Sono stati mantenuti metadati, commenti tecnici, percorsi relativi, nomi file, anchor, valori e struttura Markdown. Gli avvisi di trasferimento dal documento Google restano presenti nei file interessati.

## Compendio del Conduttore: oggetti magici C-D

- Sono stati tradotti i 20 file delle righe 802-821, dagli oggetti `Carpet of Flying` a `Deck of Many Things`, inclusi l'indice C e gli avvisi di trasferimento dal documento Google.
- Le rese principali adottano `Tappeto volante`, `Mantello della protezione`, `Sfera di cristallo`, `Cubo della forza`, `Pugnale del veleno` e `Mazzo delle molte cose`; i nomi specifici restano da revisionare.
- Sono stati mantenuti commenti, percorsi relativi, nomi file, anchor, valori e struttura Markdown.

## Compendio del Conduttore: oggetti magici D-F

- Sono stati tradotti i 20 file delle righe 822-841, dagli oggetti `Defender` a `Figurine of Wondrous Power`, inclusi gli indici D ed E.
- I titoli visibili e gli avvisi di trasferimento sono stati resi in italiano; percorsi, nomi file e commenti tecnici sono invariati. I nomi specifici degli oggetti restano da revisionare.

## Compendio del Conduttore: oggetti magici F-H

- Sono stati tradotti i 20 file delle righe 842-861, dagli oggetti `Flame Tongue` a `Helm of Comprehending Languages`, inclusi gli indici F e G.
- I titoli visibili e gli avvisi di trasferimento sono stati resi in italiano; `Flamewell` è stato mantenuto nel commento tecnico e i percorsi, i nomi file e le intestazioni alfabetiche sono invariati.
- Le rese specifiche degli oggetti, tra cui `Lingua di fiamma`, `Ammazzagiganti`, `Cuoio borchiato ammaliato` e `Elmo della comprensione dei linguaggi`, restano da revisionare editorialmente.

## Compendio del Conduttore: oggetti magici H-L

- Sono stati tradotti i 20 file delle righe 862-881, dagli oggetti `Helm of Telepathy` a `Luck Blade`, inclusi gli indici H, I, J e K.
- I titoli visibili e gli avvisi di trasferimento sono stati resi in italiano; percorsi, nomi file, commenti tecnici e identificatori restano invariati. Le rese specifiche degli oggetti restano da revisionare editorialmente.

## Compendio del Conduttore: oggetti magici L-N

- Sono stati tradotti i 20 file delle righe 882-901, dagli indici L e M agli oggetti magici M-N, inclusi gli avvisi di trasferimento e l'indice generale degli oggetti magici.
- I titoli visibili e gli avvisi sono stati resi in italiano; commenti tecnici, nomi file, percorsi e struttura Markdown restano invariati. `Necklace_of_Fireballs.md` è vuoto anche nel sorgente.
- Le rese specifiche degli oggetti restano da revisionare editorialmente.

## Compendio del Conduttore: oggetti magici O-Y e generatori di stanze

- Sono stati tradotti i 20 file delle righe 902-921, includendo gli indici alfabetici degli oggetti magici, `Ring of Protection`, gli avvisi di trasferimento, le stanze casuali e le tabelle dei generatori di idee per le stanze, le condizioni e le scoperte nei sotterranei.
- Le rese principali adottano `Anello della protezione`, `Stivali alati`, `stanze`, `condizione`, `sotterraneo`, `PNG`, `sanguinante`, `nanico`, `dragonide` e `orchesco`; i nomi specifici degli oggetti e le descrizioni dei generatori restano da revisionare editorialmente.
- Sono stati mantenuti commenti tecnici, metadati, nomi file, percorsi, valori `d20` e struttura Markdown; le label visibili dei collegamenti e gli avvisi sono stati tradotti.

## Generatori, Whitesparrow e Boiling Point

- Sono stati tradotti i 20 file delle righe 922-941, comprendendo i generatori di idee, il luogo d'esempio di Whitesparrow e l'indice dell'avventura `Boiling Point` con le prime quattro sezioni.
- Le rese principali adottano `sotterraneo`, `PNG`, `missione`, `incantesimo`, `trappola`, `pericolo`, `tesoro`, `Rocca di Whitesparrow`, `Tempio della Luce` e `Punto di ebollizione`; nomi propri, nomi file, percorsi, anchor, HTML, valori e avvisi tecnici sono stati mantenuti dove richiesto.

## Avventure d'esempio e Free5e in solitaria

- Sono stati tradotti i 20 file delle righe 942-961, completando l'avventura `The Night Blade`, i collegamenti e gli avvisi di `Boiling Point` e le sezioni disponibili di `Solo Free5e`.
- Sono stati mantenuti nomi file, percorsi relativi, anchor, classi HTML, valori, commenti tecnici e avvisi di trasferimento; i nomi propri e le rese specifiche dell'avventura restano da revisionare editorialmente.

## Compendio del Conduttore, guida alla migrazione e Manoscritto mostruoso

- Sono stati tradotti i 19 file delle righe 962-980, includendo le sezioni disponibili di `Solo Free5e`, gli indici e le note legali del Compendio del Conduttore, la guida alla migrazione 5e-Free5e e l'indice iniziale del Manoscritto mostruoso.
- Sono stati mantenuti front matter, nomi file, percorsi relativi, URL, anchor, ID HTML, commenti tecnici e valori; le attribuzioni, gli avvisi e le label visibili sono stati tradotti in italiano naturale.
- I contenuti ancora indicati come non trasferiti e i nomi propri o delle fonti esterne restano da revisionare editorialmente. `cspell` e `markdownlint` non risultano installati nell'ambiente.
