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
| 3 | Webhook-dashboard (`v3_webhook_dashboard.json`) | Eenvoudiger dashboard, getoond als webpagina via een webhook | Databron nog niet gekoppeld — dit is mijn huidige werkpunt |

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

**Huidige status / werkpunt:** De databron is nog niet gekoppeld — het veld voor de Data Table is leeg. Daardoor werkt de koppeling met de gegevens nog niet. Dit is het punt waar ik nu aan werk.

**Waarom deze aanpak:** De keuze voor een webpagina via een webhook sluit bewust aan op de twee belangrijkste klantverwachtingen. "Makkelijk in gebruik" (prioriteit 1): de gebruiker opent simpelweg een link in de browser en ziet meteen het overzicht, zonder een chatbot te hoeven aansturen of door e-mails te zoeken. "Laagdrempelig" (prioriteit 3): iedereen kan een webpagina openen zonder uitleg of externe hulp. Daarnaast loste deze aanpak het dataprobleem van iteratie 2 op door de verwerking te vereenvoudigen: minder stappen betekent minder kans dat de gegevens onderweg misgaan.

**Wat ik hiervan leerde:** Door de klantverwachtingen als meetlat te gebruiken, werd de keuze voor de webpagina-aanpak logisch in plaats van willekeurig. Een browserpagina is voor de eindgebruiker natuurlijker en laagdrempeliger dan een chatbot of een e-mail. De volgende stap is het correct koppelen van de databron, zodat het dashboard de echte facturen toont en daarmee ook "praktisch" en "toepasbaar" wordt (verwachtingen 2 en 4).

## Conclusie en vervolg

De ontwikkeling laat een duidelijke lijn zien: van een open AI-agent, via een te complex e-maildashboard, naar een eenvoudiger en beter passende webpagina-aanpak. Twee dingen stuurden die ontwikkeling: de technische problemen met de dataverwerking, en de klantverwachtingen van de opdrachtgever. Vooral "makkelijk in gebruik" en "laagdrempelig" (de twee hoogste prioriteiten) verklaren waarom ik uiteindelijk koos voor een dashboard dat je gewoon in de browser opent. Mijn volgende stap is het afmaken van iteratie 3: de databron correct koppelen, zodat het dashboard de echte facturen toont en daarmee ook aan de verwachtingen "toepasbaar" en "praktisch" voldoet.
