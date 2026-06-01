# Automatische documentatie

Dit project houdt drie documentatiebestanden automatisch bij:

- `OVERDRACHT.md` — overzicht voor wie het project overneemt
- `REVISIE_LOG.md` — geschiedenis van wijzigingen (uit Git)
- `NODE_DOCUMENTATIE.md` — uitleg van de stappen in de code

Het bijzondere: deze bestanden worden niet met de hand geschreven, maar **afgeleid uit het project zelf**. De revisielog komt uit je Git-geschiedenis, de node-documentatie uit je eigen Python-code, en de overdracht uit de bestanden die er staan. Zo lopen ze nooit achter op de werkelijkheid.

## Drie manieren om ze bij te werken

### 1. Met de hand (simpelste, altijd betrouwbaar)

Draai voordat je commit dit ene commando in de map `scripts`:

```
python update.py
```

Dit controleert je facturen, bouwt het dashboard, én werkt alle docs bij. Daarna commit en push je zoals altijd.

### 2. Automatisch bij elke commit (Git hook, lokaal)

Je kunt Git zo instellen dat de docs vanzelf worden bijgewerkt elke keer dat je commit. Maak een bestand `.git/hooks/pre-commit` (zonder extensie) met deze inhoud:

```bash
#!/bin/sh
cd scripts && python update.py
cd ..
git add OVERDRACHT.md REVISIE_LOG.md NODE_DOCUMENTATIE.md data/resultaat.json dashboard/index.html
```

Let op: een hook draait vóór de commit, dus de allernieuwste commit staat nog niet in de revisielog. Hij loopt dus één commit achter. Voor de meeste gevallen prima.

### 3. Automatisch bij elke push (GitHub Actions, in de cloud)

Dit is de echte "automatisch bij wijzigingen"-optie en vereist geen installatie op je laptop. Het bestand `.github/workflows/update-docs.yml` regelt dit al.

Hoe het werkt:
- Elke keer dat je naar GitHub pusht, start GitHub een kleine virtuele computer
- Die draait je scripts en werkt de documentatie bij
- De bijgewerkte docs worden automatisch teruggezet in je repo

Je hoeft alleen het workflow-bestand mee te pushen. Daarna gebeurt het vanzelf. Je ziet de runs onder het tabblad "Actions" op GitHub.

Omdat dit pas draait ná je push, is de revisielog hier wél compleet (jouw commit staat er dan al in).

## Welke kies je?

- Begin met **optie 1** — simpel en je hebt volledige controle.
- Wil je het echt automatisch? Gebruik **optie 3** (Actions). Die staat al klaar.
