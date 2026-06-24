# Overdrachtsdocument — Bajo Bouw Control Tower Dashboard

*Technische node-documentatie, GitHub-wegwijzer en veelgestelde vragen*

**Opgesteld door:** Semmy el Kramti
**Minor:** Digitale Transformatie & Generatieve AI — Hogeschool Windesheim
**Opdrachtgever:** Bajo Bouw & IJzerwerken
**Datum van overdracht:** 23 juni 2026

> Dit document is bedoeld voor iedereen binnen Bajo Bouw die het dashboard na vandaag beheert, gebruikt of doorontwikkelt — ook zonder voorkennis van het project.

> **Let op:** dit is de Markdown-versie van het overdrachtsdocument dat per e-mail is overgedragen. De originele Word-versie staat als [`overdrachtsdocument.docx`](overdrachtsdocument.docx) in dezelfde map. Beide hebben dezelfde inhoud.

---

## 1. Inleiding

Dit document hoort bij de overdracht van het Control Tower-dashboard aan Bajo Bouw. Het dashboard is een n8n-workflow die elke week automatisch een e-mailrapport stuurt over de verwerkte inkoopfacturen. Dit verslag legt drie dingen vast die bij een overdracht onmisbaar zijn:

1. Een diepgaande uitleg van elke node in de workflow — wat hij doet, hoe hij is ingesteld en wat er misgaat als hij uitvalt.
2. Een wegwijzer naar de GitHub-repository — waar de broncode, versiegeschiedenis en aanvullende documentatie te vinden zijn, en hoe je daar zelf in navigeert.
3. Een uitgebreide lijst veelgestelde vragen, geschreven vanuit het perspectief van iemand die het project voor het eerst onder ogen krijgt.

Dit document is bewust geschreven zonder voorkennis te veronderstellen. Waar een term voor het eerst valt (zoals "node", "trigger" of "credential"), wordt die kort uitgelegd.

### Wat dit dashboard wél en niét is

Het Control Tower-dashboard is een **rapportage-workflow, geen AI-agent**. Het neemt geen beslissingen en het gebruikt geen taalmodel. Het haalt cijfers op uit een vaste Google Sheets-log, telt en rekent die om met vaste, deterministische logica (dezelfde invoer geeft altijd dezelfde uitvoer), en stuurt het resultaat als HTML-e-mail. Dat is een bewuste keuze: voor een terugkerende rapportagetaak is voorspelbaarheid en controleerbaarheid belangrijker dan flexibiliteit.

---

## 2. Wat doet het dashboard? (functioneel overzicht)

De inkoopfacturatie-automatisering van Bajo Bouw (gebouwd door de projectgroep, los van dit dashboard) verwerkt elke binnenkomende factuur en schrijft per factuur één rij weg in een centrale Google Sheets-log, plus een apart tabblad voor fouten die tijdens de verwerking zijn opgetreden. Die log groeit continu, maar is op zichzelf geen overzicht.

Het Control Tower-dashboard lost dat op. Elke maandagochtend om 05:00 uur leest de workflow automatisch de log van de afgelopen week, rekent een vaste set kengetallen (KPI's) en risicosignalen uit, bouwt daarvan een opgemaakte HTML-e-mail en verstuurt die naar de ontvanger. Niemand hoeft de Sheets-log te openen om te weten hoe de week eruitzag.

### 2.1 Wat staat er in het wekelijkse rapport?

- **Vier basistellingen:** aantal facturen, aantal factuurregels, aantal leveranciers en het totaalbedrag inclusief btw.
- **De verdeling over de drie validatie-uitkomsten:** Goedgekeurd (PASS), Review (handmatige controle nodig) en Actie nodig (FATAL, geblokkeerd).
- **Vier risicosignalen** voor betaal- en fraudecontrole: IBAN-afwijkingen, nieuwe/onbekende leveranciers, lage AI-betrouwbaarheid en technische fouten.
- **KPI 1 — Reductie handmatige handelingen:** het percentage facturen dat volledig automatisch is afgehandeld, afgezet tegen een doel van minimaal 60% automatisch.
- **KPI 4 — Technische factuurkwaliteit (UBL):** het percentage facturen dat technisch valide is volgens de UBL-standaard voor elektronisch factureren.
- **KPI 2 — Matchkwaliteit per leverancier:** een tabel met de gemiddelde matchbetrouwbaarheid per leverancier, laagste kwaliteit boven.
- **KPI 3 — Meest voorkomende fouten:** de top 5 foutcodes uit de Validatiefouten-log, met severity (ernst) en aantal.
- **Een aandachtslijst:** de tien facturen met het hoogste bedrag die om welke reden dan ook opvallen (geblokkeerd, IBAN-afwijking, technische fout, nieuwe leverancier of lage betrouwbaarheid).

Als er in een gegeven week geen facturen zijn verwerkt, toont het rapport een nette banner ("Geen facturen verwerkt") in plaats van kengetallen met misleidende nullen of percentages.

### 2.2 Wie ontvangt het rapport, en hoe vaak?

Het rapport wordt wekelijks verstuurd, elke maandag om 05:00 uur (tijdzone Europe/Amsterdam), en vat altijd de voorgaande kalenderweek (maandag t/m zondag) samen. Naast de automatische planning is er een tweede manier om de workflow te starten: een handmatige testknop in n8n.

In deze overdrachtsversie wordt het rapport verstuurd naar het zakelijke adres **indy@bajo-bouw.nl**. Het eerdere persoonlijke testadres is hiermee vervangen. Eén punt vraagt nog aandacht: de Gmail-koppeling (credential) voor dit adres moet nog in n8n worden aangemaakt — zie hoofdstuk 4.7 en 8.1.

---

## 3. Architectuur van de workflow

De workflow bestaat uit zeven "nodes". Een node is één stap in een n8n-workflow: een blokje dat iets doet (data ophalen, data bewerken, een e-mail versturen) en zijn resultaat doorgeeft aan de volgende node. De nodes worden met lijnen ("connections") met elkaar verbonden, en die lijnen bepalen in welke volgorde de stappen worden uitgevoerd.

### 3.1 De volgorde van de workflow

| Stap | Node | Wat gebeurt hier in één zin |
|------|------|------------------------------|
| 1a | Elke maandag 05:00 | Automatische start, elke maandagochtend. |
| 1b | Handmatig testen | Alternatieve, handmatige start voor testdoeleinden. |
| 2 | Haal fouten op | Leest het tabblad "Validatiefouten" uit de Google Sheets-log. |
| 3 | Haal facturen op | Leest het tabblad "Verwerkte facturen" uit de Google Sheets-log. |
| 4 | Bereken KPI's | Filtert op de juiste week en rekent alle kengetallen en signalen uit. |
| 5 | Bouw dashboard HTML | Zet de uitgerekende cijfers om in een opgemaakte HTML-e-mail. |
| 6 | Stuur dashboard e-mail | Verstuurt de e-mail via Gmail. |

Schematisch (een pijl betekent "geeft door aan"):

```
Elke maandag 05:00 ─┐
                    ├──▶ Haal fouten op
Handmatig testen  ─┘          │
                              ▼
                       Haal facturen op
                              │
                              ▼
                        Bereken KPI's
                              │
                              ▼
                      Bouw dashboard HTML
                              │
                              ▼
                     Stuur dashboard e-mail
```

### 3.2 De twee triggers (startpunten)

Een "trigger" is de node waarmee een workflow start. Deze workflow heeft er twee, en beide leiden naar exact dezelfde keten van stappen:

- **Elke maandag 05:00** — de automatische, geplande trigger die in productie het rapport verstuurt.
- **Handmatig testen** — een knop die alleen in de n8n-editor zichtbaar is, voor het direct testen van de hele keten zonder op maandag te wachten.

### 3.3 Belangrijk: de workflow staat uit

In het meegeleverde workflowbestand staat `active` op `false`. Dat betekent dat de automatische maandagtrigger nog niet vanzelf afgaat totdat iemand de workflow in n8n actief zet (de schakelaar rechtsboven in de workflow-editor). Dit is een bewuste keuze geweest tijdens de bouw- en testfase, maar moet bij de daadwerkelijke ingebruikname binnen Bajo Bouw worden aangezet.

---

## 4. Diepgaande nodedocumentatie

Dit hoofdstuk behandelt elke node afzonderlijk. De volgorde volgt de uitvoeringsketen uit hoofdstuk 3.

### 4.1 Elke maandag 05:00

**n8n-type:** `n8n-nodes-base.scheduleTrigger`

De automatische starttrigger. Een "schedule trigger" start een workflow op vaste momenten, vergelijkbaar met een wekker. Ingesteld op een wekelijks interval: elke maandag om 05:00 uur.

**Instellingen:**
- `rule.interval.field = weeks` — het interval is in weken.
- `triggerAtDay = [1]` — dag 1 staat in n8n voor maandag (0 = zondag).
- `triggerAtHour = 5` — om 05:00 uur, tijdzone Europe/Amsterdam.

**Input / output:** Geen input (beginpunt). Geeft een lege trigger door aan "Haal fouten op".

**Aandachtspunten:** Werkt alléén als de workflow op "active" staat (zie 3.3). Het rapport vat altijd de vorige kalenderweek samen — dit wordt bepaald in "Bereken KPI's", niet hier.

### 4.2 Handmatig testen

**n8n-type:** `n8n-nodes-base.manualTrigger`

De tweede, alternatieve starttrigger. Voegt een knop ("Execute workflow") toe in de n8n-editor.

**Input / output:** Geen input. Output gaat naar dezelfde "Haal fouten op"-node.

**Let op bij testen:** Het handmatig draaien verstuurt ook daadwerkelijk een e-mail (als de keten succesvol doorloopt). Test bewust, niet onnodig vaak — zeker zodra het rapport naar een zakelijk adres gaat.

### 4.3 Haal fouten op

**n8n-type:** `n8n-nodes-base.googleSheets`

Leest alle rijen uit het tabblad "Validatiefouten" van de Google Sheets-log "Bajo Inkoopfacturatie - Log". Eén rij per fout, met onder andere een foutcode, severity en omschrijving.

**Instellingen:**
- `documentId = 1Mwl2_tiohh5s_vaXaL6cJjiZbHevHQeeU_qKIpFHttk`
- `sheetName = gid=754329244` ("Validatiefouten")
- Credential: Google Sheets OAuth2 API (id `EXKuWy0KsFqaf0Ln`)

**Aandachtspunten:** Als de credential verloopt, faalt deze node en stopt de hele workflow. Haalt altijd álle rijen op; de weekfiltering gebeurt pas in "Bereken KPI's".

### 4.4 Haal facturen op

**n8n-type:** `n8n-nodes-base.googleSheets`

Leest alle rijen uit het tabblad "Verwerkte facturen" van dezelfde log. Eén rij per verwerkte factuur, met factuurnummer, leverancier, bedragen, validatieresultaat (PASS/REVIEW/FATAL) en alle risicovelden.

**Instellingen:**
- `documentId = 1Mwl2_tiohh5s_vaXaL6cJjiZbHevHQeeU_qKIpFHttk`
- `sheetName = gid=0` ("Verwerkte facturen")
- Credential: dezelfde Google Sheets OAuth2 API (id `EXKuWy0KsFqaf0Ln`)

**Belangrijk aandachtspunt — node-volgorde:** In een eerdere versie stonden beide Sheets-nodes naast elkaar en kwam de verkeerde dataset als hoofdinvoer binnen: ~480 foutrijen werden aangezien voor facturen, waardoor alle KPI's op nul stonden. Opgelost door (a) de nodes duidelijk na elkaar te zetten en (b) in "Bereken KPI's" beide datasets expliciet bij naam op te halen (de functie `haalOp()`).

### 4.5 Bereken KPI's

**n8n-type:** `n8n-nodes-base.code`

Het rekenhart van de workflow: een Code-node met zelfgeschreven JavaScript. Ontvangt de ruwe rijen, filtert op de juiste week en rekent alle kengetallen, gemiddelden en signalen uit.

- **Stap 1 — Data ophalen ongeacht node-volgorde:** een hulpfunctie `haalOp(naam)` vraagt via `$(naam).all()` de data van een specifieke node op, in plaats van te vertrouwen op de toevallige eerste input.
- **Stap 2 — Hulpfuncties:** `num(v)` (tekst → getal), `bool(v)` (herkent true/waar/ja/1/yes), `pct(deel, geheel)` (veilig afgerond percentage), `datumDeel(v)` (datums naar één vast formaat).
- **Stap 3 — Weekvenster:** berekent zelf de vorige week (ma t/m zo) op basis van de huidige datum in Europe/Amsterdam, en filtert facturen (`verwerktOp`) en fouten (`verwerktOp`/`foutdatum`/`datum`).
- **Stap 4 — Aggregatie:** PASS/REVIEW/FATAL-verdeling, bedragen, unieke leveranciers, de vier risicosignalen, technische validatie (KPI 4), omrekening-tellingen, gemiddelden (OCR, leveranciersmatch, % regels zonder GL) en matchmethode.
- **Stap 5 — Aandachtslijst (compound key):** sleutel = factuurnummer **én** leveranciernaam, zodat twee leveranciers met hetzelfde/leeg factuurnummer niet ten onrechte worden samengevoegd. Bij meerdere redenen wordt de zwaarste getoond: Geblokkeerd (FATAL) > IBAN-afwijking > Technische fout > Nieuwe leverancier > Lage betrouwbaarheid.
- **Stap 6 — KPI-specifieke logica (eerder opgeloste knelpunten):**
  - *KPI 1:* bij een lege week wordt `stpPct` op `null` gezet i.p.v. 100% (anders lijkt een lege week "100% automatisch, doel gehaald").
  - *KPI 3:* de zwaarste severity per foutcode wordt bijgehouden (FATAL vóór REVIEW vóór ONBEKEND), niet de eerst aangetroffen.
  - *Aandachtslijst:* eerst volledige lijst opbouwen, dan afkappen tot 10; het verschil (`aandachtVerborgen`) apart doorgeven voor een eerlijke voetnoot.

**Aandachtspunten:** Verwacht specifieke kolomnamen (zie [Verwachte Sheets-kolommen](NODE_DOCUMENTATIE.md)). Bij kolomwijzigingen blijven kengetallen stilletjes op 0 staan. KPI 2 is bewust een benadering op factuurniveau. Drempelwaarden (`doelAutomatisch = 60`, `heatmapMax = 8`, top-5, top-10) staan hard in de code.

### 4.6 Bouw dashboard HTML

**n8n-type:** `n8n-nodes-base.code`

Neemt het resultaat-item van "Bereken KPI's" en bouwt de e-mail: een HTML-tabel-layout (e-mailclients ondersteunen geen moderne CSS, dus bewust een tabelstructuur).

- **Opmaakhelpers:** `kpi()` (grijs kengetal-kaartje), `riskCard()` (rood/groen risicokaartje), `balk()` (voortgangsbalk voor KPI 1 en 4), `confKleur()`/`sevKleur()`/`redenKleur()` (badge-kleuren). `eur(n)` (euro-notatie), `mv()` (enkelvoud/meervoud).
- **Lege week (`legeWeek`):** als `aantalFacturen === 0` toont de e-mail alleen kopregel, een banner ("Geen facturen verwerkt") en de voettekst — alle KPI-, risico- en tabelsecties worden overgeslagen (`kpiSectie` wordt leeg).
- **Voetnoten bij afgekapte lijsten:** zowel KPI 2 (tot 8 leveranciers) als de aandachtslijst (tot 10 facturen) krijgen automatisch een voetnoot zodra er meer items zijn.
- **KPI 1-balk:** groen als doel (min. 60%) gehaald, oranje vanaf twee derde, anders rood. Bij een lege week (`stpPct` is null) verschijnt "Geen data beschikbaar voor deze periode".

**Resultaat:** drie velden — `html`, `subject` ("Bajo Bouw - Control Tower weekoverzicht (…)") en `periodeLabel`.

**Aandachtspunten:** Verwacht exact de veldnamen die "Bereken KPI's" aanlevert. Alle visuele aanpassingen gebeuren hier in JavaScript — er is geen visuele editor.

### 4.7 Stuur dashboard e-mail

**n8n-type:** `n8n-nodes-base.gmail`

De laatste node: verstuurt de opgebouwde HTML-e-mail via Gmail.

**Instellingen:**
- `sendTo = indy@bajo-bouw.nl` — het definitieve zakelijke ontvangersadres.
- `subject = {{ $json.subject }}` — expressie die het onderwerp overneemt van de vorige node.
- `message = {{ $json.html }}` — expressie die de volledige e-mailinhoud overneemt.
- Credential: **Gmail OAuth2 API - indy@bajo-bouw.nl** — een nieuwe, nog aan te maken credential.

> **Belangrijk — de credential moet nog worden aangemaakt.** Het bestand bevat een placeholder-credential-ID (`VERVANG_MET_NIEUW_CREDENTIAL_ID`). Voordat de workflow kan versturen moet in n8n een nieuwe Gmail OAuth2-credential worden aangemaakt en ingelogd met het account van indy@bajo-bouw.nl, en moet deze node daaraan worden gekoppeld. Test daarna via "Handmatig testen" voordat de workflow op "active" gaat.

**Waarom de velden als expressie staan, niet als platte tekst:** In een eerdere versie stonden `subject` en `message` als losse, platte tekst (de standaardplaceholder). Daardoor kwam er een e-mail met generieke titel en zonder inhoud aan. Opgelost door beide velden naar "Expression"-modus (`{{ }}`) te zetten.

**Aandachtspunten:** Het veld `webhookId` ("bajo-ct-email") is een interne n8n-identificatie — Gmail-nodes versturen altijd alleen uitgaand. Het ontvangersadres staat hard ingesteld; voor meerdere ontvangers moet `sendTo` worden uitgebreid met door komma's gescheiden adressen.

---

## 5. Welke versie wordt hier overgedragen?

Het workflowbestand bij deze overdracht bevat alle vier de correcties uit de laatste ontwikkelronde: de afkapnotities bij KPI 2 en de aandachtslijst, de severity-correctie in KPI 3, en de behandeling van lege weken bij KPI 1. Inhoudelijk komt dit overeen met wat in de versiedocumentatie "v14" wordt genoemd.

**Aandachtspunt — het label in n8n:** In de n8n-omgeving is dit bestand getagd als "v11", terwijl de inhoud overeenkomt met v14 uit [`versiedocumentatie.md`](versiedocumentatie.md). Dit is een naamgevingsverschil, geen inhoudelijk probleem. Aangeraden wordt de tag in n8n bij te werken naar "v14", of een notitie toe te voegen die naar de versiedocumentatie verwijst.

Voor de volledige geschiedenis (v1 t/m v14): zie [`REVISIE_LOG.md`](../../REVISIE_LOG.md) en [`versiedocumentatie.md`](versiedocumentatie.md). Daarnaast bevat dit bestand één extra wijziging: het ontvangersadres is gewijzigd van het persoonlijke testadres naar het definitieve `indy@bajo-bouw.nl`.

---

## 6. De databron: Google Sheets-log

Alle cijfers zijn herleidbaar tot één Google Sheets-bestand: "Bajo Inkoopfacturatie - Log". Dit bestand wordt gevuld door de inkoopfacturatie-automatisering; het Control Tower-dashboard **leest dit bestand alleen, het schrijft er nooit in**.

| Onderdeel | Waarde |
|-----------|--------|
| Bestandsnaam | Bajo Inkoopfacturatie - Log |
| Document-ID | `1Mwl2_tiohh5s_vaXaL6cJjiZbHevHQeeU_qKIpFHttk` |
| Tabblad 1 | "Verwerkte facturen" (gid=0) — één rij per verwerkte factuur |
| Tabblad 2 | "Validatiefouten" (gid=754329244) — één rij per geconstateerde fout |
| Google Sheets-credential | "Google Sheets OAuth2 API" (id `EXKuWy0KsFqaf0Ln`) |

De directe link is te openen door de document-ID achter `https://docs.google.com/spreadsheets/d/` te plakken.

**Waarom de cijfers altijd narekenbaar zijn:** Omdat het dashboard geen eigen database heeft en alleen leest uit dit ene bestand, kan elk getal bij twijfel direct in de log worden teruggeverifieerd: filter "Verwerkte facturen" op de juiste week en de aantallen moeten overeenkomen.

---

## 7. GitHub-repository: waar vind je wat

### 7.1 De repository openen

Open een webbrowser en ga naar: **github.com/windesheimsemmyminorAI/portfolio**. Je ziet de hoofdmap ("root"). Klik op een mapnaam om erin te kijken, of op een bestandsnaam om de inhoud direct te lezen.

### 7.2 Mapstructuur — wat staat waar

| Locatie | Inhoud |
|---------|--------|
| `README.md` (hoofdmap) | Algemeen overzicht van het hele project. |
| `BEOORDELAAR.md` (hoofdmap) | Leeswijzer met overzicht van alle onderdelen en bewijsstukken. |
| `OVERDRACHT.md` (hoofdmap) | Automatisch gegenereerd overzicht (huidige stand + bestandenlijst). |
| `REVISIE_LOG.md` (hoofdmap) | Volledige wijzigingsgeschiedenis uit de Git-commitgeschiedenis. |
| `NODE_DOCUMENTATIE.md` (hoofdmap) | Automatisch gegenereerde uitleg van de functies in `verwerk_facturen.py`. |
| `n8n/dashboard/` | De n8n-workflowbestanden (JSON), versiedocumentatie en dit overdrachtsdocument. |
| `scripts/` | Het Python-validatiescript en de documentatiegeneratoren. |
| `dashboard/` | Het door `verwerk_facturen.py` gegenereerde HTML-dashboard (losse Python-uitwerking). |
| `.github/workflows/` | GitHub Actions: genereert bij elke commit de documentatie opnieuw. |

### 7.3 De laatste versie van de n8n-workflow vinden

Ga naar `n8n/dashboard/` en zoek het JSON-bestand met het hoogste versienummer (op het moment van overdracht: de v14-versie, `v11_control_tower_email_overdracht.json`). Klik op het bestand, gebruik de downloadknop, en importeer in n8n via "Import from file".

### 7.4 Wijzigingsgeschiedenis terugvinden

- Wát er in een versie veranderde en waarom → [`versiedocumentatie.md`](versiedocumentatie.md).
- Chronologische commitgeschiedenis → [`REVISIE_LOG.md`](../../REVISIE_LOG.md).
- Welke bestanden er nu in het project staan → [`OVERDRACHT.md`](../../OVERDRACHT.md).

### 7.5 GitHub Actions — de "cloud-robot"

Deze repository gebruikt GitHub Actions: een automatisering die bij elke commit op GitHub's servers draait en `OVERDRACHT.md`, `REVISIE_LOG.md` en `NODE_DOCUMENTATIE.md` opnieuw genereert, zodat die documentatie nooit veroudert. Terug te vinden onder het tabblad "Actions".

*Een eerder opgelost knelpunt:* in een eerdere fase genereerden zowel `update.py` als de GitHub Actions-robot dezelfde bestanden, wat tot merge-conflicten leidde. Opgelost door `update.py` lokaal geen documentatie meer te laten genereren — dat doet voortaan uitsluitend de cloud-robot.

### 7.6 De Python-uitwerking los van het dashboard

Naast de n8n-workflow staat er een losstaande Python-implementatie (`verwerk_facturen.py` in `scripts/`) die facturen op vijf vaste regels controleert en een eigen HTML-dashboard bouwt. Dit is een apart technisch bewijsstuk en niet nodig om het n8n-dashboard te laten werken.

---

## 8. Openstaande actiepunten bij overdracht

Deze punten zijn gedocumenteerde, herkende keuzes met een duidelijk vervolgpad. Zie [`CHECKLIST_INGEBRUIKNAME.md`](CHECKLIST_INGEBRUIKNAME.md) voor een afvinkbare versie.

### 8.1 Gmail-credential voor het zakelijke adres afronden

Het ontvangersadres is al gewijzigd naar `indy@bajo-bouw.nl`. Wat nog moet:
1. Open in n8n het overzicht van Credentials en maak een nieuwe "Gmail OAuth2 API"-credential aan.
2. Log in met het Google-account van indy@bajo-bouw.nl.
3. Open de node "Stuur dashboard e-mail" en koppel deze nieuwe credential (ter vervanging van de placeholder `VERVANG_MET_NIEUW_CREDENTIAL_ID`).
4. Test met de "Handmatig testen"-trigger voordat de workflow op "active" gaat.

### 8.2 Drempelwaarden kalibreren

De huidige drempelwaarden zijn testwaarden, nog niet gekalibreerd op echte Bajo-data. Na een aantal weken productiedraaien aan te raden te herzien:
- Het automatiseringsdoel (`doelAutomatisch`, nu 60) in "Bereken KPI's".
- De matchkwaliteits-kleurgrenzen (`confKleur`: groen vanaf 90%, oranje vanaf 75%) in "Bouw dashboard HTML".
- Het aantal getoonde leveranciers in KPI 2 (`heatmapMax`, nu 8) en aandachtsfacturen (nu 10).

### 8.3 De workflow op "active" zetten

De workflow staat nu op inactief. Voor wekelijkse verzending moet iemand de "active"-schakelaar omzetten, ná 8.1 en het testen.

### 8.4 Beheerder aanwijzen

Voor doorontwikkeling van de Code-nodes is enige programmeerkennis (JavaScript) nodig. Leg vast wie binnen de organisatie verantwoordelijk wordt voor toekomstig onderhoud.

---

## 9. Veelgestelde vragen (zonder voorkennis)

### 9.1 Basisbegrip: wat is dit eigenlijk?

**Wat is het Control Tower-dashboard in één zin?** Een automatische workflow die elke maandagochtend een e-mail stuurt met een samenvatting van alle inkoopfacturen die de afgelopen week zijn verwerkt.

**Is dit een AI-agent of "kunstmatige intelligentie"?** Nee. Dit dashboard gebruikt zelf geen taalmodel en neemt geen beslissingen. De AI (voor het lezen en beoordelen van facturen) zit in een ander, los project — de inkoopfacturatie-automatisering.

**Wat is n8n?** Een platform voor workflow-automatisering: een online tool waarin je stappen ("nodes") verbindt om een taak automatisch te laten verlopen.

**Wat betekent "node" precies?** Eén stap binnen een n8n-workflow: een blokje dat iets doet en zijn resultaat doorgeeft. Dit dashboard bestaat uit zeven nodes.

**Wat is een "trigger"?** De node waarmee een workflow start. Deze workflow heeft er twee: een automatische (elke maandag 05:00) en een handmatige testknop.

**Wat is een "credential"?** Een opgeslagen toegangssleutel die n8n gebruikt om bij een extern systeem te mogen lezen of schrijven — hier voor Google Sheets (lezen) en Gmail (versturen).

**Waarom in n8n in plaats van met AI?** Voor een terugkerende rapportagetaak zijn betrouwbaarheid en reproduceerbaarheid belangrijker dan flexibiliteit.

**Hoe verhoudt dit zich tot de "inkoopfacturatie-agent" van het team?** Twee gescheiden onderdelen. De agent (met Mistral OCR) leest en beoordeelt facturen en schrijft naar de log. Dit dashboard vat die log alleen wekelijks samen — het raakt de facturen zelf nooit aan.

### 9.2 Het rapport lezen en interpreteren

**Wanneer komt het rapport binnen?** Elke maandag om 05:00 uur (Europe/Amsterdam), zodra de workflow op "active" staat. Het vat de voorgaande kalenderweek samen.

**Wat betekenen PASS, REVIEW en FATAL?** De drie validatie-uitkomsten: PASS = goedgekeurd, REVIEW = een mens moet de factuur nalopen, FATAL = geblokkeerd, actie vereist. In het rapport: "Goedgekeurd", "Review" en "Actie nodig".

**Verschil tussen "facturen" en "factuurregels"?** Eén factuur kan meerdere regels bevatten. "Facturen" = aantal afzonderlijke facturen; "Factuurregels" = optelsom van alle regels.

**Wat zijn de vier risicosignalen?** IBAN-afwijking (rekeningnummer wijkt af — controleer voor betaling), Nieuwe leverancier (nog niet in stamdata), Lage betrouwbaarheid (AI had weinig zekerheid), Technische fouten (voldoet niet aan UBL-standaard). Elk is een signaal om extra te controleren, geen automatische blokkade (tenzij ook FATAL).

**Wat is KPI 1?** Het percentage facturen dat volledig automatisch is afgehandeld, tegenover een doel van minimaal 60%.

**Wat is KPI 2 en waarom een "benadering"?** Per leverancier de gemiddelde matchbetrouwbaarheid. Bewust een benadering: een proxy op factuurniveau (OCR-/matchconfidence), geen analyse van losse artikelregels.

**Wat is KPI 3?** De top 5 meest voorkomende foutcodes uit de Validatiefouten-log, met severity en aantal.

**Wat is KPI 4?** De technische factuurkwaliteit volgens de UBL-standaard: het percentage facturen dat technisch correct is opgebouwd.

**Wat is de aandachtslijst?** De tien facturen met het hoogste bedrag die om een risicoreden zijn opgevallen, gesorteerd op bedrag.

**Waarom soms alleen een grijze banner zonder cijfers?** Als er die week geen facturen zijn verwerkt. Bewust geen kengetallen, om te voorkomen dat een lege week eruitziet als "100% automatisch".

**Voetnoot dat niet alles getoond wordt — waar vind ik de rest?** Het rapport toont max. 8 leveranciers en 10 aandachtsfacturen. De volledige lijst staat in de Google Sheets-log (zie hoofdstuk 6).

**Klopt elk getal echt?** Ja: elk getal is rechtstreeks afgeleid uit de log met vaste rekenregels, met uitzondering van KPI 2 (bewuste benadering).

### 9.3 Beheer en techniek

**De wekelijkse e-mail komt niet aan — wat nu?** Controleer in n8n onder "Executions" of de workflow is gestart. Faalt het bij de Sheets-nodes → meestal Google Sheets-credential verlopen. Faalt alleen de laatste stap → controleer of de Gmail-credential is aangemaakt (8.1). Faalt er niets → controleer de spamfolder.

**De cijfers lijken niet te kloppen — wat controleren?** Open de Google Sheets-log en controleer de rijen van die week. Wijken de kolomnamen af van hoofdstuk 4.5 → werk "Bereken KPI's" bij; anders blijven kengetallen stilletjes op 0.

**Kan ik zelf de drempelwaarden aanpassen?** Ja, door de code in "Bereken KPI's" te openen en de betreffende regel aan te passen — er is geen apart instellingenscherm. Vraagt JavaScript-kennis.

**Wat als ik de twee Sheets-nodes verwissel?** In principe niets ernstigs: "Bereken KPI's" haalt beide datasets bij naam op (4.5, Stap 1). In een eerdere versie was dit wél een probleem (zie 4.4).

**Kan het rapport naar meerdere mensen?** Ja. Pas in "Stuur dashboard e-mail" het veld `sendTo` aan met door komma's gescheiden adressen, of koppel een distributielijst.

**Hoe test ik zonder tot maandag te wachten?** Gebruik de "Handmatig testen"-trigger.

**Is dit veilig met leveranciers- en factuurgegevens?** Het dashboard leest alleen uit de beveiligde Google Sheets-log via een geautoriseerde credential en verstuurt per e-mail. Geen data naar externe partijen buiten Google en Gmail; geen taalmodel op de factuurinhoud.

**Is dit een vervanging voor handmatig controleren?** Nee. Het vervangt het handmatig spitten in de log om een overzicht te krijgen, maar beoordeelt of betaalt geen facturen.

### 9.4 GitHub en documentatie

**Geen GitHub-ervaring — hoe vind ik het juiste bestand?** Volg 7.1 t/m 7.3: open de repository-link, klik op `n8n/dashboard/`, zoek het hoogste versienummer. Geen Git-commando's nodig om te bekijken/downloaden.

**Waarom zoveel versies (v1 t/m v14)?** Elke versie is een afgeronde ontwikkelstap. `versiedocumentatie.md` beschrijft per versie wat er veranderde en waarom.

**Verschil tussen de n8n-versie en de Python-versie?** Twee afzonderlijke uitwerkingen. De n8n-workflow is de operationele versie die Bajo Bouw gebruikt. Het Python-script is een losse technische uitwerking voor portfoliodoeleinden.

**Waar vind ik uitleg over een eerder opgeloste bug?** In `versiedocumentatie.md` en `REVISIE_LOG.md`, plus samengevat in hoofdstuk 4 van dit document.

### 9.5 Overdracht-specifieke vragen

**Is dit dashboard "klaar"?** De workflow is functioneel klaar en getest, en het ontvangersadres is definitief gezet. Er resteren twee organisatorische stappen: de Gmail-credential aanmaken en de workflow op "active" zetten — plus op termijn de drempelwaarden kalibreren.

**Wat moet er als eerste gebeuren na vandaag?** (1) Gmail-credential aanmaken en koppelen, (2) workflow een paar weken laten meedraaien en drempelwaarden bijstellen, (3) op "active" zetten, (4) intern vastleggen wie verantwoordelijk is voor onderhoud.

**Wie kan ik bereiken bij vragen?** Voor dit dashboard: Semmy el Kramti (bouwer/auteur). Voor de inkoopfacturatie-automatisering: de teamgenoten die dat onderdeel bouwden.

---

## 10. Samenvatting

Het Control Tower-dashboard is een deterministische n8n-workflow van zeven nodes die elke maandag automatisch de Bajo-inkoopfacturatielog samenvat tot een leesbaar weekrapport met kengetallen, risicosignalen en een aandachtslijst. De volledige broncode, versiegeschiedenis en aanvullende documentatie staan publiek op **github.com/windesheimsemmyminorAI/portfolio**, met de operationele workflow in `n8n/dashboard/`. Het rapport wordt verstuurd naar het definitieve zakelijke adres **indy@bajo-bouw.nl**.

Voor een succesvolle overdracht resteren nog twee concrete stappen: de Gmail-credential aanmaken en koppelen in n8n, en de workflow op "active" zetten — plus, op termijn, de drempelwaarden kalibreren.

> **Kernprincipe:** Voor een terugkerende rapportagetaak is een voorspelbare, narekenbare workflow betrouwbaarder dan een AI-agent. Elk getal in dit rapport is terug te herleiden tot de onderliggende Google Sheets-log, en de logica verandert nooit van gedrag tussen twee identieke runs. Die transparantie is bewust de kern van het ontwerp.
