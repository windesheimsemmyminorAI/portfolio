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
| `versiedocumentatie.md` | — | Beschrijving van wat er per versie veranderde en waarom |
| `versiedocumentatie.docx` | — | Dezelfde documentatie als Word-bestand voor het portfolio |

## De twee huidige versies (v6 en v7)

Beide lezen uit de Google Sheets-log "Bajo Inkoopfacturatie - Log":
- Tabblad **Verwerkte facturen** — de facturen met status PASS/REVIEW/FATAL
- Tabblad **Validatiefouten** — voor de top-5 meest voorkomende fouten

**De KPI's:**
1. Reductie handmatige handelingen (gauge, doel max 40%)
2. Factuurkwaliteit per leverancier (heatmap)
3. Meest voorkomende fouten (top-5)

## Hoe importeer ik een workflow in N8N?

1. Open N8N, maak een nieuwe workflow aan
2. Drie puntjes (...) rechtsboven, kies "Import from File"
3. Kies het gewenste `.json` bestand
4. Controleer per Google Sheets-node of de credential en het juiste tabblad gekoppeld zijn

## Versiebeheer

Elke versie staat als apart bestand bewaard, zodat de ontwikkeling zichtbaar blijft. Nieuwe versies voeg ik toe als `v8_...` enzovoort, en ik beschrijf de wijziging in `versiedocumentatie.md`.
