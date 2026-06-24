# Node-documentatie

Automatisch gegenereerd overzicht van de bouwstenen (nodes/stappen) in het verwerkingsscript. Afgeleid uit de code zelf.

Laatst bijgewerkt: 2026-06-24

Bron: `scripts/verwerk_facturen.py`

## `controleer_factuur()`

Controleert een factuur op vijf regels en geeft een lijst met problemen terug. Een lege lijst betekent: geen fouten gevonden.

## `bepaal_status()`

Vertaalt het aantal problemen naar een status en kleur: 0 = groen/goedgekeurd, 1 = geel/waarschuwing, 2 of meer = rood/actie nodig.

## `bouw_dashboard()`

Bouwt een complete HTML-pagina (het dashboard) met telkaarten en een tabel van alle facturen, inclusief kleurcodering per status.

## `main()`

Het hoofdprogramma: leest facturen in, controleert ze, schrijft het resultaat weg en bouwt het dashboard.

