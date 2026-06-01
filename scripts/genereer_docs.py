"""
genereer_docs.py
================

Dit script maakt automatisch drie documentatiebestanden aan, op basis
van de ECHTE staat van je project. Je hoeft dus niets met de hand bij
te houden.

Het maakt:
  OVERDRACHT.md          - overzicht voor wie het project overneemt
  REVISIE_LOG.md         - geschiedenis van wijzigingen (uit Git)
  NODE_DOCUMENTATIE.md   - uitleg van de stappen in de code

Hoe gebruik je het?
-------------------
    python genereer_docs.py

Waar haalt het de informatie vandaan?
-------------------------------------
- REVISIE_LOG:       uit de Git-geschiedenis (git log)
- NODE_DOCUMENTATIE: uit de functies in verwerk_facturen.py
- OVERDRACHT:        uit de bestanden die in het project staan
"""

import ast
import json
import subprocess
from datetime import date
from pathlib import Path


# De projectmap (een niveau boven de scripts-map)
BASIS = Path(__file__).parent.parent


# ---------------------------------------------------------------
# 1. REVISIE_LOG.md  - uit de Git-geschiedenis
# ---------------------------------------------------------------

def haal_git_geschiedenis():
    """Haalt de lijst van commits op via 'git log'. Geeft een lege lijst terug als Git niet beschikbaar is."""
    try:
        resultaat = subprocess.run(
            ["git", "log", "--pretty=format:%ad|%h|%s", "--date=short"],
            cwd=BASIS,
            capture_output=True,
            text=True,
            check=True,
        )
        regels = resultaat.stdout.strip().splitlines()
        return [r for r in regels if r]
    except Exception:
        return []


def genereer_revisie_log():
    """Bouwt REVISIE_LOG.md op uit de commitgeschiedenis."""
    commits = haal_git_geschiedenis()

    tekst = "# Revisielog\n\n"
    tekst += "Automatisch gegenereerd overzicht van alle wijzigingen, "
    tekst += "afgeleid uit de Git-geschiedenis.\n\n"
    tekst += f"Laatst bijgewerkt: {date.today()}\n\n"

    if not commits:
        tekst += "_Nog geen commits gevonden. Maak eerst een commit, "
        tekst += "draai dit script daarna opnieuw._\n"
    else:
        tekst += "| Datum | Versie | Wijziging |\n"
        tekst += "|-------|--------|------------|\n"
        for regel in commits:
            datum, hash_kort, bericht = regel.split("|", 2)
            tekst += f"| {datum} | `{hash_kort}` | {bericht} |\n"

    (BASIS / "REVISIE_LOG.md").write_text(tekst, encoding="utf-8")
    print(f"REVISIE_LOG.md bijgewerkt ({len(commits)} wijzigingen)")


# ---------------------------------------------------------------
# 2. NODE_DOCUMENTATIE.md  - uit de code zelf
# ---------------------------------------------------------------

def lees_functies(bestandspad):
    """Leest een Python-bestand en haalt de functienamen + hun beschrijving (docstring) eruit."""
    bron = bestandspad.read_text(encoding="utf-8")
    boom = ast.parse(bron)
    functies = []
    for node in boom.body:
        if isinstance(node, ast.FunctionDef):
            beschrijving = ast.get_docstring(node) or "(geen beschrijving)"
            functies.append((node.name, beschrijving))
    return functies


def genereer_node_documentatie():
    """Bouwt NODE_DOCUMENTATIE.md op uit de functies in het verwerkingsscript."""
    script = BASIS / "scripts" / "verwerk_facturen.py"
    functies = lees_functies(script)

    tekst = "# Node-documentatie\n\n"
    tekst += "Automatisch gegenereerd overzicht van de bouwstenen (nodes/stappen) "
    tekst += "in het verwerkingsscript. Afgeleid uit de code zelf.\n\n"
    tekst += f"Laatst bijgewerkt: {date.today()}\n\n"
    tekst += f"Bron: `scripts/verwerk_facturen.py`\n\n"

    for naam, beschrijving in functies:
        tekst += f"## `{naam}()`\n\n{beschrijving}\n\n"

    (BASIS / "NODE_DOCUMENTATIE.md").write_text(tekst, encoding="utf-8")
    print(f"NODE_DOCUMENTATIE.md bijgewerkt ({len(functies)} functies)")


# ---------------------------------------------------------------
# 3. OVERDRACHT.md  - uit de projectstaat
# ---------------------------------------------------------------

def tel_facturen_per_status():
    """Leest resultaat.json en telt hoeveel facturen er per status zijn."""
    pad = BASIS / "data" / "resultaat.json"
    if not pad.exists():
        return None
    resultaten = json.loads(pad.read_text(encoding="utf-8"))
    telling = {"goedgekeurd": 0, "waarschuwing": 0, "actie nodig": 0}
    for r in resultaten:
        telling[r["status"]] = telling.get(r["status"], 0) + 1
    return len(resultaten), telling


def genereer_overdracht():
    """Bouwt OVERDRACHT.md op: een overzicht voor wie het project overneemt."""
    tekst = "# Overdracht\n\n"
    tekst += "Dit document helpt iemand die het project overneemt snel op weg. "
    tekst += "Automatisch gegenereerd uit de huidige projectstaat.\n\n"
    tekst += f"Laatst bijgewerkt: {date.today()}\n\n"

    tekst += "## Hoe draai je het project?\n\n"
    tekst += "1. Open een terminal in de map `scripts`\n"
    tekst += "2. Draai `python verwerk_facturen.py` (controleert facturen + bouwt dashboard)\n"
    tekst += "3. Open `dashboard/index.html` in je browser\n"
    tekst += "4. Draai `python genereer_docs.py` om deze documentatie bij te werken\n\n"

    tekst += "## Huidige stand van zaken\n\n"
    standen = tel_facturen_per_status()
    if standen is None:
        tekst += "_Nog geen resultaat. Draai eerst `verwerk_facturen.py`._\n\n"
    else:
        totaal, telling = standen
        tekst += f"Er zijn op dit moment **{totaal} facturen** verwerkt:\n\n"
        tekst += f"- Goedgekeurd: {telling['goedgekeurd']}\n"
        tekst += f"- Waarschuwing: {telling['waarschuwing']}\n"
        tekst += f"- Actie nodig: {telling['actie nodig']}\n\n"

    tekst += "## Bestanden in dit project\n\n"
    for pad in sorted(BASIS.rglob("*")):
        if pad.is_file() and ".git" not in pad.parts:
            relatief = pad.relative_to(BASIS)
            tekst += f"- `{relatief}`\n"

    (BASIS / "OVERDRACHT.md").write_text(tekst, encoding="utf-8")
    print("OVERDRACHT.md bijgewerkt")


# ---------------------------------------------------------------
# Alles uitvoeren
# ---------------------------------------------------------------

def main():
    genereer_revisie_log()
    genereer_node_documentatie()
    genereer_overdracht()
    print("\nAlle documentatie is bijgewerkt.")


if __name__ == "__main__":
    main()
