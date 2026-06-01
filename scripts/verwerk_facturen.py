"""
verwerk_facturen.py
====================

Wat doet dit script?
--------------------
1. Het leest alle facturen in uit  data/facturen.json
2. Het controleert elke factuur op een aantal regels (validatie)
3. Het schrijft het resultaat naar  data/resultaat.json
4. Het bouwt een dashboard:        dashboard/index.html

Met andere woorden: dit ene script is de hele "pijplijn" van
ruwe data -> controle -> visueel dashboard.

Hoe gebruik je het?
-------------------
Open een terminal in de projectmap en typ:

    python verwerk_facturen.py

Daarna open je  dashboard/index.html  in je browser.
"""

import json
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------
# DEEL 1: De validatieregels
# ---------------------------------------------------------------
# Deze functie kijkt naar EEN factuur en geeft een lijst met
# problemen terug. Een lege lijst betekent: geen problemen.

def controleer_factuur(factuur):
    """Controleert een factuur op vijf regels en geeft een lijst met problemen terug. Een lege lijst betekent: geen fouten gevonden."""
    problemen = []

    # Regel 1: factuurnummer mag niet leeg zijn
    if not factuur.get("factuurnummer"):
        problemen.append("Factuurnummer ontbreekt")

    # Regel 2: bedragen moeten kloppen (excl + btw = incl)
    excl = factuur.get("totaalbedrag_excl_btw", 0)
    btw = factuur.get("btw_bedrag", 0)
    incl = factuur.get("totaalbedrag_incl_btw", 0)
    # We staan 1 cent afrondingsverschil toe
    if abs((excl + btw) - incl) > 0.01:
        problemen.append("Bedragen kloppen niet (excl + btw is niet gelijk aan incl)")

    # Regel 3: factuurdatum moet geldig zijn en niet in de toekomst
    datum_tekst = factuur.get("factuurdatum", "")
    try:
        datum = datetime.strptime(datum_tekst, "%Y-%m-%d").date()
        if datum > date.today():
            problemen.append("Factuurdatum ligt in de toekomst")
    except ValueError:
        problemen.append("Factuurdatum is ongeldig")

    # Regel 4: bankrekeningnummer moet op een IBAN lijken
    iban = factuur.get("bankrekeningnummer", "")
    if not (len(iban) >= 15 and iban[:2].isalpha()):
        problemen.append("Bankrekeningnummer lijkt geen geldige IBAN")

    # Regel 5: elke regel moet een projectnummer hebben
    for nummer, regel in enumerate(factuur.get("regels", []), start=1):
        if not regel.get("projectnummer"):
            problemen.append(f"Regel {nummer} mist een projectnummer")

    return problemen


# ---------------------------------------------------------------
# DEEL 2: Bepaal de status op basis van de problemen
# ---------------------------------------------------------------
# Geen problemen   -> groen  (Goedgekeurd)
# 1 probleem       -> geel   (Waarschuwing)
# 2 of meer        -> rood   (Actie nodig)

def bepaal_status(aantal_problemen):
    """Vertaalt het aantal problemen naar een status en kleur: 0 = groen/goedgekeurd, 1 = geel/waarschuwing, 2 of meer = rood/actie nodig."""
    if aantal_problemen == 0:
        return "goedgekeurd", "groen"
    elif aantal_problemen == 1:
        return "waarschuwing", "geel"
    else:
        return "actie nodig", "rood"


# ---------------------------------------------------------------
# DEEL 3: Het dashboard (HTML) bouwen
# ---------------------------------------------------------------
# We maken een simpele HTML-pagina met een tabel. De data
# stoppen we er meteen in, zodat je het bestand gewoon kunt
# openen zonder webserver.

def bouw_dashboard(resultaten):
    """Bouwt een complete HTML-pagina (het dashboard) met telkaarten en een tabel van alle facturen, inclusief kleurcodering per status."""
    # Tel hoeveel facturen er per status zijn
    aantal_groen = sum(1 for r in resultaten if r["kleur"] == "groen")
    aantal_geel = sum(1 for r in resultaten if r["kleur"] == "geel")
    aantal_rood = sum(1 for r in resultaten if r["kleur"] == "rood")

    # Maak de tabelrijen
    rijen = ""
    for r in resultaten:
        kleur_css = {
            "groen": "background:#e1f5ee;color:#0f6e56;",
            "geel": "background:#faeeda;color:#854f0b;",
            "rood": "background:#fcebeb;color:#a32d2d;",
        }[r["kleur"]]

        # Toon het eerste probleem, of "Goedgekeurd"
        melding = r["problemen"][0] if r["problemen"] else "Goedgekeurd"

        rijen += f"""
        <tr>
          <td style="font-family:monospace">{r['factuurnummer'] or '(leeg)'}</td>
          <td>{r['leverancier']}</td>
          <td style="text-align:right">&euro; {r['bedrag']:.2f}</td>
          <td><span style="{kleur_css}padding:3px 10px;border-radius:99px;font-size:13px">{melding}</span></td>
        </tr>"""

    # De complete HTML-pagina
    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <title>Inkoopfacturatie dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #2c2c2a; }}
    h1 {{ font-weight: 500; }}
    .kaarten {{ display: flex; gap: 16px; margin: 24px 0; }}
    .kaart {{ background: #f1efe8; border-radius: 8px; padding: 16px 20px; flex: 1; }}
    .kaart .label {{ font-size: 13px; color: #5f5e5a; }}
    .kaart .getal {{ font-size: 28px; font-weight: 500; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th {{ text-align: left; color: #5f5e5a; font-weight: 500; border-bottom: 2px solid #d3d1c7; padding: 8px; }}
    td {{ padding: 10px 8px; border-bottom: 1px solid #e8e6df; }}
  </style>
</head>
<body>
  <h1>Inkoopfacturatie dashboard</h1>
  <p>Automatisch gegenereerd overzicht van gecontroleerde facturen.</p>

  <div class="kaarten">
    <div class="kaart"><div class="label">Totaal</div><div class="getal">{len(resultaten)}</div></div>
    <div class="kaart"><div class="label">Goedgekeurd</div><div class="getal" style="color:#0f6e56">{aantal_groen}</div></div>
    <div class="kaart"><div class="label">Waarschuwing</div><div class="getal" style="color:#854f0b">{aantal_geel}</div></div>
    <div class="kaart"><div class="label">Actie nodig</div><div class="getal" style="color:#a32d2d">{aantal_rood}</div></div>
  </div>

  <table>
    <thead>
      <tr><th>Factuurnr.</th><th>Leverancier</th><th style="text-align:right">Bedrag</th><th>Status</th></tr>
    </thead>
    <tbody>{rijen}
    </tbody>
  </table>

  <p style="color:#888780;font-size:13px;margin-top:24px">
    Gegenereerd op {date.today()} &middot; portfolio Semmy
  </p>
</body>
</html>"""
    return html


# ---------------------------------------------------------------
# DEEL 4: Het hoofdprogramma - alles aan elkaar knopen
# ---------------------------------------------------------------

def main():
    """Het hoofdprogramma: leest facturen in, controleert ze, schrijft het resultaat weg en bouwt het dashboard."""
    # Waar staan de bestanden? (relatief aan dit script)
    basis = Path(__file__).parent.parent  # de projectmap
    invoer = basis / "data" / "facturen.json"
    uitvoer_data = basis / "data" / "resultaat.json"
    uitvoer_dashboard = basis / "dashboard" / "index.html"

    # Lees de facturen in
    with open(invoer, "r", encoding="utf-8") as f:
        facturen = json.load(f)

    # Controleer elke factuur en verzamel het resultaat
    resultaten = []
    for factuur in facturen:
        problemen = controleer_factuur(factuur)
        status, kleur = bepaal_status(len(problemen))
        resultaten.append({
            "factuurnummer": factuur.get("factuurnummer", ""),
            "leverancier": factuur.get("leverancier_naam", "Onbekend"),
            "bedrag": factuur.get("totaalbedrag_incl_btw", 0),
            "status": status,
            "kleur": kleur,
            "problemen": problemen,
        })

    # Schrijf het resultaat weg als JSON
    with open(uitvoer_data, "w", encoding="utf-8") as f:
        json.dump(resultaten, f, indent=2, ensure_ascii=False)

    # Bouw het dashboard
    html = bouw_dashboard(resultaten)
    with open(uitvoer_dashboard, "w", encoding="utf-8") as f:
        f.write(html)

    # Print een korte samenvatting in de terminal
    print(f"{len(resultaten)} facturen verwerkt.")
    for r in resultaten:
        print(f"  - {r['factuurnummer'] or '(leeg)':12} {r['status']}")
    print(f"\nDashboard klaar: {uitvoer_dashboard}")
    print("Open dat bestand in je browser om het te bekijken.")


# Dit zorgt dat main() draait als je het script start
if __name__ == "__main__":
    main()
