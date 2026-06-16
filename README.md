# Inkoopfacturatie dashboard

> 🎓 **Beoordelaar?** Begin bij **[`BEOORDELAAR.md`](BEOORDELAAR.md)** — de leeswijzer met een overzicht van alle onderdelen, bewijsstukken en versiehistorie.

Een portfolio-project dat laat zien hoe je ruwe factuurdata automatisch kunt controleren en overzichtelijk kunt presenteren in een dashboard.

## Wat het doet

Dit project neemt een set inkoopfacturen, controleert ze automatisch op fouten, en bouwt een dashboard waarop je in één oogopslag ziet welke facturen goedgekeurd zijn en welke aandacht nodig hebben.

De rode draad:

```
ruwe data  ->  Python valideert  ->  dashboard toont resultaat
```

## Wat ik hiermee laat zien

- **Data**: gestructureerde JSON-data met een formeel schema
- **Validatie**: Python-logica die facturen controleert op vijf regels
- **Automatisering**: één commando verwerkt alle facturen en bouwt het dashboard

## Hoe draai ik het?

Je hebt alleen Python nodig (geen extra packages).

1. Open een terminal in de map `scripts`
2. Draai het script:
   ```
   python verwerk_facturen.py
   ```
3. Open `dashboard/index.html` in je browser

Het script toont ook een korte samenvatting in de terminal.

## Mappen

| Map | Inhoud |
|-----|--------|
| `data/` | De facturen (`facturen.json`) en het resultaat (`resultaat.json`) |
| `scripts/` | Het verwerkingsscript |
| `schemas/` | Het JSON-schema dat de datastructuur beschrijft |
| `dashboard/` | Het gegenereerde dashboard (`index.html`) |
| `docs/` | Technische uitleg |

## De validatieregels

1. Factuurnummer mag niet leeg zijn
2. Bedragen moeten kloppen (excl + btw = incl)
3. Factuurdatum moet geldig zijn en niet in de toekomst liggen
4. Bankrekeningnummer moet op een IBAN lijken
5. Elke factuurregel moet een projectnummer hebben

Meer technische uitleg staat in `docs/hoe_het_werkt.md`.

## Context

Het onderwerp (inkoopfacturatie) komt uit een groepsproject voor een bouwbedrijf. Dit dashboard is mijn eigen, losstaande uitwerking om de techniek erachter te demonstreren.

## Andere onderdelen in deze repo

Deze repository is mijn portfolio en bundelt meerdere projecten:

| Onderdeel | Map | Wat |
|-----------|-----|-----|
| Factuur-dashboard (dit project) | `scripts/`, `dashboard/`, `data/`, `schemas/` | Python-validatie + gegenereerd HTML-dashboard |
| N8N-workflows | `n8n/` | De inkoopfacturatie-dashboardworkflow in N8N (v1–v10), met versiedocumentatie |
| Wolfje & Bella — Media Agentic | `wolfje-media-agentic/` | AI-contentpijplijn voor een getekende stripserie; incl. Episode 1 "The Lookout" |

Elk onderdeel heeft een eigen `README.md` met uitleg.

---

Gemaakt door Semmy &middot; 2026

