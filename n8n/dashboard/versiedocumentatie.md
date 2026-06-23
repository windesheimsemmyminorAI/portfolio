# Versiedocumentatie: dashboard-workflow in N8N

Dit document beschrijft de ontwikkeling van mijn N8N dashboard-workflow voor de inkoopfacturatie van Bajo Bouw. Het laat zien waar ik mee begon, wat ik per stap veranderde, en waarom.

## Klantverwachtingen als uitgangspunt

Bij de opdrachtgever hebben we de belangrijkste verwachtingen voor een succesvol project opgehaald. Op volgorde van prioriteit (1 = hoogste):

| Prioriteit | Verwachting | Toelichting |
|------------|-------------|-------------|
| 1 | Makkelijk in gebruik | Het product voelt natuurlijk aan voor de eindgebruiker |
| 2 | Toepasbaar | De eindgebruiker heeft het gevoel dat het product hem/haar helpt in het proces |
| 3 | Laagdrempelig | De eindgebruiker leert het product kennen zonder bemiddeling van een externe partij |
| 4 | Praktisch | Het product levert aantoonbaar meerwaarde voor het proces |

Deze verwachtingen vormen de meetlat voor mijn keuzes. Vooral "makkelijk in gebruik" (de hoogste prioriteit) en "laagdrempelig" hebben mijn ontwikkeling gestuurd, zoals hieronder per iteratie blijkt.

## Overzicht

| Iteratie | Workflow | Wat het deed | Waarom ik verder ging |
|----------|----------|--------------|------------------------|
| 1 | AI Agent (`v1_ai_agent.json`) | Chatbot met OpenAI en een Google Sheets-tool | Te ingewikkeld voor mijn doel; ik wilde een dashboard, geen chatbot |
| 2 | Gmail-dashboard (`v2_gmail_dashboard.json`) | Uitgebreid dashboard met statistieken, validatie en grafieken, dagelijks per e-mail | Data uit Google Sheets werd niet goed gelezen; grafieken bleven leeg en het validatie-overzicht was kapot |
| 3 | Webhook-dashboard (`v3_webhook_dashboard.json`) | Eenvoudiger dashboard als webpagina via webhook | Databron (n8n Data Table) was niet gekoppeld; ik ontdekte dat de juiste databron de Google Sheets-log was |
| 4 | Webhook-dashboard werkend (`v4_webhook_werkend.json`) | Webpagina-dashboard dat correct uit de log-sheet leest | Wilde dezelfde werkende opzet ook per e-mail kunnen tonen |
| 5 | E-mail-dashboard werkend (`v5_email_werkend.json`) | Hetzelfde dashboard, mail-veilig opgemaakt en per e-mail verstuurd | Dashboard miste nog de KPI's die de opdrachtgever wil meten |
| 6 | Webhook-dashboard met KPI's (`v6_webhook_kpi.json`) | Webpagina-dashboard met de drie KPI's (gauge, heatmap, top-fouten) | Huidige versie (webpagina) |
| 7 | E-mail-dashboard met KPI's (`v7_email_kpi.json`) | Hetzelfde KPI-dashboard, mail-veilig per e-mail | Opdrachtgever wilde één wekelijks overzicht i.p.v. een losse weergave |
| 8 | Weekrapport (`v8_email_weekrapport.json`) | Verbreed KPI-dashboard als wekelijks e-mailrapport, samengevat per factuurdatum-week | Wilde ook een variant over de volledige dataset |
| 9 | Volledig overzicht (`v9_email_volledig.json`) | Hetzelfde rijke dashboard, maar handmatig over de **volledige** dataset i.p.v. één week | Terug naar een wekelijks ritme, nu met de nieuwe databron |
| 10 | Weekrapport nieuwe koppeling (`v10_email_weekrapport_nieuwe-koppeling.json`) | Wekelijks weekrapport gekoppeld aan de nieuwe databron | Correcties nodig op KPI 3, aandachtslijst en lege-weekgedrag |
| 11 | Severity-correctie KPI 3 | Zwaarste severity per foutcode bijhouden, niet de eerst aangetroffen | — |
| 12 | Voetnoot aandachtslijst | Teller voor afgekapte aandachtsfacturen, automatische voetnoot | — |
| 13 | Lege week KPI 1 | `stpPct` op null bij 0 facturen, balk toont "Geen data" | — |
| 14 | Lege-weekmodus volledig + overdracht (`v11_control_tower_email_overdracht.json`) | Alle KPI-secties verborgen bij lege week; e-mailadres → `indy@bajo-bouw.nl` | Definitieve overdrachtsversie |

## Iteratie 1 — De AI Agent

**Bestand:** `v1_ai_agent.json`

**Wat het was:** Mijn eerste poging was een AI-agent. De workflow bestond uit een chat-trigger, een AI Agent-node, een OpenAI-model (`gpt-5-mini`), een geheugen-node en een Google Sheets-tool waarmee de agent een spreadsheet kon aanmaken. Het idee was dat je via een chatgesprek met de agent zou kunnen werken.

**Wat er technisch in zat:**
- Trigger: een chatbericht
- AI Agent gekoppeld aan OpenAI
- Geheugen-node (stond ingesteld op een contextlengte van 0)
- Google Sheets-tool om een spreadsheet aan te maken

**Waarom ik verder ging:** Deze opzet was te ingewikkeld voor wat ik nodig had. Belangrijker nog: een chatbot was niet wat ik zocht. Mijn doel was een overzichtelijk dashboard van de facturatie, niet een gesprekspartner. Een chatbot botste bovendien met de belangrijkste klantverwachting, "makkelijk in gebruik": de gebruiker moet weten wat hij moet typen en hoe hij de agent moet aansturen. Dat voelt niet natuurlijk. Ik wilde meer grip op het resultaat en een vaste, herhaalbare weergave.

**Wat ik hiervan leerde:** Een AI-agent is krachtig maar niet altijd het juiste gereedschap. Voor een vast overzicht (een dashboard) past een gestructureerde workflow beter dan een open chat-agent.

## Iteratie 2 — Het Gmail-dashboard

**Bestand:** `v2_gmail_dashboard.json`

**Wat het was:** Een veel uitgebreidere workflow die de facturen uit een Google Sheet haalde, statistieken berekende (aantal facturen, bedragen, BTW, unieke leveranciers), validatiefouten analyseerde, grafieken genereerde en daarvan een opgemaakt HTML-dashboard bouwde. Dat dashboard werd dagelijks om 08:00 uur per e-mail naar Gmail gestuurd, met daarnaast archivering van de gegevens.

**Wat er technisch in zat:**
- Trigger: handmatig én een dagelijkse planning (08:00 uur)
- Databron: Google Sheets (echte spreadsheet)
- Bewerking: filteren op recente data, statistieken berekenen, validatiefouten samenvoegen, foutpatronen analyseren
- Grafieken via gegenereerde afbeeldings-URL's
- Opbouw van een uitgebreid HTML-dashboard met KPI's en grafieken
- Verzending per e-mail (Gmail) en archivering

**Waarom ik verder ging:** In de praktijk werd de data uit Google Sheets niet goed uitgelezen en verwerkt. Op het verzonden dashboard was te zien dat:
- het validatie-overzicht een kapotte reeks toonde (een rij losse cijfers in plaats van een net statusoverzicht);
- de grafieken leeg bleven (geen waarden);
- de inhoud daardoor onbetrouwbaar oogde.

Een dashboard dat de gegevens niet correct toont, schiet zijn doel voorbij. Daarom besloot ik de aanpak te vereenvoudigen.

**Wat ik hiervan leerde:** Veel functies tegelijk toevoegen maakt een workflow kwetsbaar. Als de databron-koppeling en de dataverwerking niet kloppen, helpt mooie opmaak niets. Eerst de data goed laten stromen, dan pas uitbreiden.

## Iteratie 3 — Het Webhook-dashboard

**Bestand:** `v3_webhook_dashboard.json`

**Wat het was:** Een eenvoudiger opzet, gemaakt met behulp van de AI van N8N. In plaats van het dashboard te mailen, wordt het nu via een webhook als webpagina aangeboden. De workflow haalt facturen op, berekent in een code-node de statistieken en bouwt daar een HTML-dashboard van met statistiekkaarten en een tabel van recente facturen.

**Wat er technisch in zat:**
- Trigger: een webhook (de pagina is op te vragen via een URL)
- Databron: een n8n Data Table
- Bewerking: statistieken berekenen in een code-node
- Opbouw van een HTML-dashboard met overzichtskaarten en een factuurtabel
- Antwoord: het dashboard wordt als webpagina teruggestuurd

**Waarom deze aanpak:** De keuze voor een webpagina via een webhook sluit bewust aan op de twee belangrijkste klantverwachtingen. "Makkelijk in gebruik" (prioriteit 1): de gebruiker opent simpelweg een link in de browser en ziet meteen het overzicht, zonder een chatbot te hoeven aansturen of door e-mails te zoeken. "Laagdrempelig" (prioriteit 3): iedereen kan een webpagina openen zonder uitleg of externe hulp.

**Waarom ik verder ging:** Het dashboard bleef leeg. De databron was ingesteld op een lege n8n Data Table. Bij het uitzoeken hiervan ontdekte ik de werkelijke oorzaak: de verwerkte facturen staan niet in een Data Table, maar in een Google Sheets-log (tabblad "Verwerkte facturen") die door mijn factuurverwerkings-workflow wordt gevuld. Bovendien kwamen de veldnamen niet overeen: het dashboard zocht naar velden als `factuurNummer` en `status`, terwijl de sheet kolommen heet als `factuurnummer` en `validatieResultaat`. Dit verklaarde meteen waarom ook iteratie 2 leeg bleef.

**Wat ik hiervan leerde:** Een dashboard valt of staat met de juiste databron en exact overeenkomende veldnamen. Dit was het kantelpunt in mijn project: pas toen ik de echte log-sheet en de juiste kolomnamen in beeld had, kon het dashboard werken.

## Iteratie 4 — Webhook-dashboard werkend

**Bestand:** `v4_webhook_werkend.json`

**Wat het was:** Dezelfde webpagina-opzet als iteratie 3, maar nu gekoppeld aan de juiste databron: het tabblad "Verwerkte facturen" van de Google Sheets-log. De veldnamen zijn afgestemd op de werkelijke kolomnamen, en de bedragverwerking houdt rekening met de Nederlandse notatie (bijvoorbeeld 845,50).

**Wat er technisch in zat:**
- Trigger: een webhook
- Databron: Google Sheets, tabblad "Verwerkte facturen"
- Bewerking: statistieken berekenen met de juiste kolomnamen
- Opbouw van een HTML-dashboard met overzichtskaarten en een factuurtabel

**Waarom ik verder ging:** Met een werkende webpagina wilde ik dezelfde opzet ook per e-mail beschikbaar maken, zodat de opdrachtgever beide vormen kon vergelijken en kiezen welke het best bij hun manier van werken past.

**Wat ik hiervan leerde:** Zodra de databron en veldnamen klopten, werkte het dashboard direct. De eerdere problemen lagen dus niet aan de opzet, maar aan de koppeling.

## Iteratie 5 — E-mail-dashboard werkend

**Bestand:** `v5_email_werkend.json`

**Wat het was:** Hetzelfde dashboard als iteratie 4, maar verstuurd per e-mail. De opmaak is bewust mail-veilig gemaakt: opgebouwd met tabellen en inline-styling in plaats van moderne CSS (zoals grids en gradients), omdat e-mailprogramma's als Gmail die opmaak vaak verwijderen. Dit voorkomt het opmaakprobleem dat bij iteratie 2 speelde.

**Wat er technisch in zat:**
- Trigger: handmatig
- Databron: Google Sheets, tabblad "Verwerkte facturen"
- Mail-veilige HTML (tabellen, inline-styling)
- Verzending per e-mail

**Waarom ik verder ging:** Het dashboard toonde nog niet de KPI's die de opdrachtgever wil meten. Uit het ontwerp van de "Control Tower" volgden twee vaste KPI's plus een overzicht van veelvoorkomende fouten. Die wilde ik toevoegen.

**Wat ik hiervan leerde:** Mail-veilige opmaak vraagt een andere techniek dan een webpagina. Dezelfde data kan in twee weergaven, maar elke weergave heeft zijn eigen ontwerpregels.

## Iteratie 6 — Webhook-dashboard met KPI's

**Bestand:** `v6_webhook_kpi.json`

**Wat het was:** De webpagina-versie uitgebreid met de drie KPI's uit het Control Tower-ontwerp. Het dashboard leest nu twee tabbladen uit de log: "Verwerkte facturen" en "Validatiefouten".

**De KPI's:**
- **KPI 1 — Reductie handmatige handelingen:** een gauge (snelheidsmeter) die het percentage handmatige handelingen toont, berekend als het aandeel facturen met status REVIEW of FATAL ten opzichte van het totaal. De 40%-doellijn is in de meter gemarkeerd.
- **KPI 2 — Factuurkwaliteit per leverancier:** een heatmap die per leverancier het percentage afwijkende facturen toont, kleurgecodeerd van groen (geen afwijkingen) naar rood (veel afwijkingen). Dit is bewust een benadering op factuurniveau; de exacte artikelmatch volgt zodra het tabblad Factuurregels wordt meegenomen.
- **KPI 3 — Meest voorkomende fouten:** een top-5 van foutcodes uit het tabblad "Validatiefouten".

**Waarom deze aanpak:** De KPI's maken het dashboard "praktisch" (verwachting 4): het levert aantoonbaar inzicht in de voortgang van de automatisering en de factuurkwaliteit per leverancier.

**Wat ik hiervan leerde:** Niet elke KPI uit het ontwerp is één-op-één meetbaar met de beschikbare data. Door eerlijk te benoemen dat KPI 2 een benadering is, blijft het dashboard betrouwbaar en bespreekbaar in plaats van schijnzekerheid te geven.

## Iteratie 7 — E-mail-dashboard met KPI's

**Bestand:** `v7_email_kpi.json`

**Wat het was:** De e-mailversie met dezelfde drie KPI's, opnieuw mail-veilig opgemaakt. De gauge uit de webversie is hier vervangen door een mail-veilige voortgangsbalk, zodat de KPI ook in een e-mail goed weergegeven wordt.

**Waarom deze aanpak:** Zo zijn beide weergaven (webpagina en e-mail) inhoudelijk gelijkwaardig: dezelfde KPI's, dezelfde data, maar elk in een vorm die past bij het medium. De opdrachtgever kan zo een eerlijke vergelijking maken.

**Wat ik hiervan leerde:** Een KPI-visualisatie moet je soms per medium anders vormgeven. De inhoud blijft gelijk, de techniek verschilt.

## Iteratie 8 — Weekrapport met verbrede KPI's

**Bestand:** `v8_email_weekrapport.json`

**Wat het is:** De e-mailversie is fors verbreed en omgezet naar een wekelijks
rapport. Het dashboard leest nog steeds de twee tabbladen "Verwerkte facturen"
en "Validatiefouten", maar gebruikt nu het rijkere schema van de nieuwe
inkoopfacturatie-workflow (Mistral-extractie).

**Wat er nieuw is:**
- Risicosignalen-blok (IBAN-afwijking, nieuwe/onbekende leverancier, lage
  AI-betrouwbaarheid, technische UBL-fouten) — vervangt de weggevallen risicoscore.
- KPI 4 — Technische factuurkwaliteit (UBL): percentage technisch valide facturen.
- Kwaliteitsrij: gemiddelde OCR-betrouwbaarheid, gemiddelde leveranciersmatch,
  percentage uniek gematcht, percentage regels zonder grootboekrekening,
  eenheidsnormalisatie en een samenvatting van de matchmethode.
- KPI 2 toont nu ook de gemiddelde matchbetrouwbaarheid per leverancier;
  KPI 3 toont het type fout (FATAL/REVIEW); een lijst "Facturen die aandacht vragen".

**Wekelijks rapport:** De handmatige trigger is vervangen door een Schedule
Trigger die elke maandag om 05:00 (Europe/Amsterdam) draait. Het dashboard vat
de vorige kalenderweek (maandag t/m zondag) samen, gefilterd op **factuurdatum**.
De validatiefouten worden via het factuurnummer aan diezelfde set facturen
gekoppeld. De periode staat in de header en in het e-mailonderwerp. Een
handmatige test-trigger blijft beschikbaar.

**Waarom deze aanpak:** De opdrachtgever wil één wekelijks overzicht in plaats
van een losse weergave. Filteren op factuurdatum sluit aan op hoe de
administratie naar een week kijkt (de facturen van die week), niet op het
toevallige moment van verwerken.

**Aandachtspunt:** Bij weinig facturen in een week worden percentages in KPI 2
en de gemiddelde-confidence-cijfers grof (bij één factuur 0% of 100%). De
absolute aantallen ernaast houden het interpreteerbaar.

## Iteratie 9 — Volledig overzicht (alle data)

**Bestand:** `v9_email_volledig.json`

**Wat het is:** Dezelfde rijke KPI-opzet als het weekrapport, maar zonder weekfilter:
het dashboard rekent over de **volledige** dataset en wordt handmatig verstuurd. Handig
voor een totaaloverzicht of een ad-hoc controle los van het wekelijkse ritme.

**Waarom deze aanpak:** Naast het wekelijkse rapport bleek er behoefte aan een
overzicht over alle verwerkte facturen tegelijk (bijvoorbeeld voor een periodieke
totaalcontrole). De onderliggende KPI-berekening en opmaak zijn gelijk aan het
weekrapport; alleen het tijdvenster en de trigger verschillen.

## Iteratie 10 — Weekrapport op de nieuwe databron

**Bestanden:** `v10_email_weekrapport_nieuwe-koppeling.json` (huidig) en
`v10_email_weekrapport_oude-koppeling.json` (historische variant)

**Wat het is:** Het wekelijkse weekrapport, nu gekoppeld aan de **nieuwe databron**.
De oude variant (`…oude-koppeling`) hing nog aan de oude Excel-koppeling en is bewaard
als historisch bestand.

**Belangrijk:** de **node-logica is in beide identiek** — dezelfde KPI-berekening,
dezelfde mail-veilige opmaak en dezelfde Google Sheets-bron. Het echte verschil zit in de
data: de `…oude-koppeling`-variant heeft **104 gepinde data-items (`pinData`)** ingebakken
— de oude dataset uit de oude Excel-koppeling, vandaar het grotere bestand. De
`…nieuwe-koppeling`-variant heeft geen gepinde data en leest live uit de nieuwe databron.
Het onderscheid is ook terug te zien in de interne workflow-naam en tag
(`v10 nieuwe koppeling` vs. `v10 oude koppeling`).

**Wat ik hiervan leerde:** een versieverschil hoeft niet altijd in de code te zitten.
Door de twee koppeling-varianten expliciet te benoemen (in plaats van twee bestanden met
dezelfde naam) blijft traceerbaar welke versie aan welke databron hing.

## Iteratie 11 — Severity-correctie in KPI 3

**Bestand:** `v11_control_tower_email_overdracht.json` (bevat ook v12 t/m v14, zie toelichting)

**Wat er is veranderd:** In de "Bereken KPI's"-node werd de zwaarste severity per foutcode
niet altijd correct bijgehouden. Als een foutcode meerdere keren voorkwam met wisselende ernst
(bijv. eerst REVIEW, dan FATAL), bleef de eerst aangetroffen severity staan. De foutTeller-logica
is aangepast zodat bij een zwaarder type (FATAL vóór REVIEW vóór ONBEKEND) de severity wordt
bijgewerkt — zodat een ernstige fout nooit per ongeluk als lichte fout verschijnt.

**Waarom:** Een FATAL-fout die later in de rij staat, werd tot nu toe getoond als REVIEW als
het eerste voorkomen REVIEW had. Dat geeft een misleidend beeld van de ernst.

## Iteratie 12 — Voetnoot bij afgekapte aandachtslijst

**Wat er is veranderd:** De aandachtslijst toont maximaal 10 facturen. Daarvoor werd de volledige
lijst direct afgekapt, zonder te melden hoeveel er buiten beeld vielen. Nu wordt eerst de volledige
gesorteerde lijst (`alleAandacht`) opgebouwd, vervolgens afgekapt tot 10 (`aandacht`), en het
verschil (`aandachtVerborgen`) apart doorgegeven. Zodra er meer dan 10 aandachtsfacturen zijn,
verschijnt automatisch een voetnoot ("Toont 10 van X facturen · overige Y niet weergegeven.").

**Waarom:** Zonder die voetnoot kon de ontvanger ten onrechte denken dat het rapport volledig was,
terwijl hogere-risicore facturen buiten beeld vielen.

## Iteratie 13 — Lege week: KPI 1-balk verborgen, stpPct op null

**Wat er is veranderd:** Bij een week zonder facturen (totaal = 0) werd `stpPct` eerder berekend
als 100% (want 0 van 0 facturen zijn handmatig = 0% handmatig = 100% automatisch). Dat verscheen
dan in de balk als "100% automatisch · doel gehaald", wat feitelijk onjuist is. Nu wordt `stpPct`
bij een lege week expliciet op `null` gezet. In de HTML-node toont de balk dan de tekst
"Geen data beschikbaar voor deze periode" in plaats van een misleidende 100%-balk.

**Waarom:** Een lege week is geen prestatie — ze mag er niet uitzien als een perfect resultaat.

## Iteratie 14 — Lege-weekmodus volledig + overdrachtsversie

**Bestand:** `v11_control_tower_email_overdracht.json`

**Wat er is veranderd:** Bij een week zonder facturen werden eerder alle KPI-secties nog steeds
opgebouwd (met nullen en € 0,00), waarna alleen de balk de "geen data"-tekst toonde. Nu worden
alle KPI-, risico- en tabelblokken volledig overgeslagen (`kpiSectie = ''`) als er geen facturen
zijn. Het rapport toont dan uitsluitend de kopregel, een nette grijze banner ("Geen facturen
verwerkt") en de voettekst. Daarnaast is het ontvangersadres in de "Stuur dashboard e-mail"-node
gewijzigd van het persoonlijke testadres naar het definitieve zakelijke adres `indy@bajo-bouw.nl`.

**Naamgeving-opmerking:** Het workflowbestand is in n8n getagd als "v11". Inhoudelijk omvat het
de correcties van v11 t/m v14 in deze versiedocumentatie. Dat verschil is een naamgevingskwestie,
geen inhoudelijk probleem — de code is consistent en correct. Bij toekomstig onderhoud wordt
aangeraden de n8n-tag bij te werken naar "v14" of een notitie toe te voegen die naar deze
versiedocumentatie verwijst.

**Openstaand actiepunt:** De Gmail-credential voor `indy@bajo-bouw.nl` moet nog worden aangemaakt
in n8n (het workflowbestand bevat een placeholder-ID). Pas daarna kan de workflow op "active"
worden gezet. Zie het overdrachtsdocument (hoofdstuk 8.1 en 8.3) voor de stap-voor-stap aanpak.

---

## Conclusie en vervolg

De ontwikkeling laat een duidelijke lijn zien: van een open AI-agent (iteratie 1), via een te
complex e-maildashboard (iteratie 2) en een eerste webpagina-poging (iteratie 3), naar een
werkend dashboard zodra de juiste databron en veldnamen gevonden waren (iteratie 4-5), naar een
dashboard dat de KPI's van de opdrachtgever toont (iteratie 6-7), naar een wekelijks weekrapport
met verbrede KPI's (iteratie 8), een volledig-overzichtvariant (iteratie 9), het weekrapport op
de nieuwe databron (iteratie 10), en ten slotte vier gerichte bugfixes (iteraties 11-14) die
resulteren in de definitieve overdrachtsversie.

Twee dingen stuurden die ontwikkeling: de technische problemen met de databron en de
dataverwerking, en de klantverwachtingen van de opdrachtgever. Het kantelpunt was de ontdekking
dat de juiste databron de Google Sheets-log was, met exact overeenkomende veldnamen. Vanaf dat
moment kon ik het dashboard niet alleen laten werken, maar ook uitbreiden met betekenisvolle KPI's.

Het definitieve product is het wekelijkse e-mailrapport (`v11_control_tower_email_overdracht.json`,
inhoudelijk v14) dat elke maandagochtend om 05:00 uur automatisch wordt verstuurd naar
`indy@bajo-bouw.nl`. De webpagina-versie (`v6_webhook_kpi.json`) blijft beschikbaar als
alternatieve weergave.
