# Hoe het werkt (techniek)

Dit document legt de techniek achter het project uit. Het is bedoeld om te laten zien welke keuzes ik gemaakt heb en hoe de onderdelen samenwerken.

## De pijplijn

```
data/facturen.json          (1. ruwe data)
        |
        v
scripts/verwerk_facturen.py (2. validatie + automatisering)
        |
        +--> data/resultaat.json   (3. gecontroleerde data)
        |
        +--> dashboard/index.html  (4. visueel dashboard)
```

Eén commando (`python verwerk_facturen.py`) doorloopt de hele keten. Dat is het "automatisering"-deel: je hoeft niets handmatig te doen, het script leest, controleert, en bouwt het dashboard.

## De drie technische thema's

### 1. Data
De facturen staan in `data/facturen.json` als gestructureerde data. Het bijbehorende `schemas/factuur_schema.json` beschrijft formeel welke velden een factuur heeft en welke verplicht zijn. Zo is de datastructuur gedocumenteerd en controleerbaar.

### 2. Validatie
In `verwerk_facturen.py` zit de functie `controleer_factuur()`. Die past vijf regels toe:

1. Factuurnummer mag niet leeg zijn
2. Bedragen moeten kloppen (excl + btw = incl)
3. Factuurdatum moet geldig zijn en niet in de toekomst liggen
4. Bankrekeningnummer moet op een IBAN lijken
5. Elke factuurregel moet een projectnummer hebben

Het aantal gevonden problemen bepaalt de status: 0 = groen, 1 = geel, 2+ = rood.

### 3. Automatisering
Het script verwerkt alle facturen in één keer (batch) en genereert automatisch het dashboard. Voeg je een factuur toe aan `facturen.json` en draai je het script opnieuw, dan staat hij direct op het dashboard.

## Waarom deze keuzes?

- **Alleen standaard Python**: geen installatie nodig, het draait overal. Beginnervriendelijk en makkelijk te delen.
- **HTML met data erin gebakken**: je kunt het dashboard openen door te dubbelklikken, zonder webserver.
- **JSON als dataformaat**: leesbaar, makkelijk uit te breiden, en standaard in de meeste systemen (zoals N8N).

## Mogelijke uitbreidingen

- Echte facturen (PDF) uitlezen met de Claude API
- Validatie tegen het JSON-schema (`jsonschema` package)
- Filters en sorteren op het dashboard (met JavaScript)
- Koppeling met N8N om facturen automatisch binnen te halen
