# N8N workflows

Deze map bevat mijn N8N dashboard-workflows voor de inkoopfacturatie, in de volgorde waarin ik ze ontwikkeld heb.

## Bestanden

| Bestand | Iteratie | Korte omschrijving |
|---------|----------|--------------------|
| `v1_ai_agent.json` | 1 | AI-agent met chat en Google Sheets-tool |
| `v2_gmail_dashboard.json` | 2 | Uitgebreid dashboard, dagelijks per e-mail |
| `v3_webhook_dashboard.json` | 3 | Eenvoudiger dashboard als webpagina via webhook |
| `versiedocumentatie.md` | — | Beschrijving van wat er per versie veranderde en waarom |
| `versiedocumentatie.docx` | — | Dezelfde documentatie als Word-bestand voor het portfolio |

## Hoe importeer ik een workflow terug in N8N?

1. Open N8N
2. Maak een nieuwe workflow aan
3. Klik op de drie puntjes (...) rechtsboven, kies "Import from File"
4. Kies het gewenste `.json` bestand

## Versiebeheer

Elke versie staat als apart bestand bewaard, zodat de ontwikkeling zichtbaar blijft. Nieuwe versies voeg ik toe als `v4_...`, `v5_...` enzovoort, en ik beschrijf de wijziging in `versiedocumentatie.md`.
