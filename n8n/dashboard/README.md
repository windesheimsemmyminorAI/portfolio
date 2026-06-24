# Dashboard-workflows

Deze map bevat mijn N8N-workflows voor het inkoopfacturatie-dashboard, in de volgorde waarin ik ze ontwikkeld heb.

## Bestanden

| Bestand | Iteratie | Korte omschrijving |
|---------|----------|--------------------|
| `v1_ai_agent.json` | 1 | AI-agent met chat en Google Sheets-tool |
| `v2_gmail_dashboard.json` | 2 | Uitgebreid dashboard, dagelijks per e-mail |
| `v3_webhook_dashboard.json` | 3 | Eerste webpagina-poging via webhook (databron nog niet gekoppeld) |
| `v4_webhook_werkend.json` | 4 | Werkend webpagina-dashboard uit de Google Sheets-log |
| `v5_email_werkend.json` | 5 | Werkend e-mail-dashboard, mail-veilig opgemaakt |
| `v6_webhook_kpi.json` | 6 | Webpagina-dashboard met KPI's (gauge, heatmap, top-fouten) |
| `v7_email_kpi.json` | 7 | E-mail-dashboard met dezelfde KPI's, mail-veilig |
| `v8_email_weekrapport.json` | 8 | Verbreed KPI-dashboard, wekelijks (ma 05:00), samengevat per factuurdatum-week |
| `v9_email_volledig.json` | 9 | E-mail-dashboard over de **volledige** dataset (handmatig), met het rijke Mistral-schema |
| `v10_email_weekrapport_oude-koppeling.json` | 10 (oud) | Weekrapport gekoppeld aan de **oude** databron (oude Excel-koppeling) |
| `v10_email_weekrapport_nieuwe-koppeling.json` | 10 | Weekrapport gekoppeld aan de **nieuwe** databron |
| `v11_control_tower_email_overdracht.json` | 14 (n8n-tag: v11) | Definitieve overdrachtsversie — vier bugfixes, e-mail naar `indy@bajo-bouw.nl` |
| `versiedocumentatie.md` | — | Beschrijving van wat er per versie veranderde en waarom |
| `versiedocumentatie.docx` | — | Dezelfde documentatie als Word-bestand voor het portfolio |
| `overdrachtsdocument.md` / `.docx` | — | Volledig overdrachtsdocument: node-uitleg, GitHub-wegwijzer en FAQ |
| `NODE_DOCUMENTATIE.md` | — | Diepgaande per-node-documentatie + verwachte Sheets-kolommen |
| `CHECKLIST_INGEBRUIKNAME.md` | — | Afvinkbare checklist voor de stap naar productie |

## De huidige versies (v6 en v14)

- **Webpagina:** `v6_webhook_kpi.json` — het KPI-dashboard als opvraagbare webpagina.
- **E-mail (definitief):** `v11_control_tower_email_overdracht.json` — de overdrachtsversie met
  alle correcties (inhoudelijk v14), verstuurt wekelijks naar `indy@bajo-bouw.nl`.

> **Naamgeving:** het bestand is in n8n getagd als "v11", maar omvat inhoudelijk de correcties
> van v11 t/m v14 (zie `versiedocumentatie.md`). Dat is een naamgevingskwestie, geen
> inhoudelijk probleem.

> **Let op:** de twee v10-bestanden hebben **identieke node-logica**; het verschil zit in de
> data. `…oude-koppeling` heeft de **oude dataset gepind ingebakken** (`pinData`, 104 items uit
> de oude Excel-koppeling); `…nieuwe-koppeling` leest live uit de nieuwe databron. De oude
> variant is bewaard als historische variant.

Beide lezen uit de Google Sheets-log "Bajo Inkoopfacturatie - Log":
- Tabblad **Verwerkte facturen** — de facturen met status PASS/REVIEW/FATAL
- Tabblad **Validatiefouten** — voor de top-5 meest voorkomende fouten

## De workflow-keten (7 nodes)

```
Elke maandag 05:00 ─┐
                    ├──▶ Haal fouten op ──▶ Haal facturen op ──▶ Bereken KPI's ──▶ Bouw dashboard HTML ──▶ Stuur dashboard e-mail
Handmatig testen  ─┘
```

Diepgaande uitleg per node + de verwachte Sheets-kolommen staat in
[`NODE_DOCUMENTATIE.md`](NODE_DOCUMENTATIE.md). De volledige context (waarom-keuzes, FAQ,
openstaande actiepunten) staat in [`overdrachtsdocument.md`](overdrachtsdocument.md).

> **De workflow staat bewust op `active: false`.** Tijdens bouw en test mag de maandag-trigger
> niet vanzelf afgaan. Bij ingebruikname moet iemand de "active"-schakelaar omzetten — zie de
> [checklist](CHECKLIST_INGEBRUIKNAME.md).

**De KPI's (definitieve versie v14):**
1. Reductie handmatige handelingen — percentage automatisch verwerkt, doel min. 60%
2. Matchkwaliteit per leverancier — gemiddelde matchbetrouwbaarheid per leverancier (heatmap)
3. Meest voorkomende fouten — top-5 foutcodes met severity (FATAL/REVIEW)
4. Technische factuurkwaliteit (UBL) — percentage facturen dat technisch valide is

> v8 voegt risicosignalen, KPI 4 en datakwaliteitscijfers toe; v11–v14 lossen vier bugs op
> (severity-correctie, aandachtslijst-voetnoot, lege-weekgedrag). Zie `versiedocumentatie.md`.

## Hoe importeer ik een workflow in N8N?

1. Open N8N, maak een nieuwe workflow aan
2. Drie puntjes (...) rechtsboven, kies "Import from File"
3. Kies het gewenste `.json` bestand
4. Controleer per Google Sheets-node of de credential en het juiste tabblad gekoppeld zijn

> **Let op bij `v11_control_tower_email_overdracht.json`:** de node "Stuur dashboard e-mail"
> bevat een **placeholder-credential** (`VERVANG_MET_NIEUW_CREDENTIAL_ID`). Maak eerst in n8n
> een nieuwe "Gmail OAuth2 API"-credential aan voor `indy@bajo-bouw.nl` en koppel die aan de node,
> anders kan de workflow geen e-mail versturen. Zie de [checklist](CHECKLIST_INGEBRUIKNAME.md).

## Versiebeheer

Elke versie staat als apart bestand bewaard, zodat de ontwikkeling zichtbaar blijft. Nieuwe versies voeg ik toe als `v8_...` enzovoort, en ik beschrijf de wijziging in `versiedocumentatie.md`.
