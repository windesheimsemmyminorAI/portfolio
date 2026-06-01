"""
update.py
=========

Het gemak-commando voor op je eigen computer. Draait:
  1. Controleert de facturen en bouwt het dashboard

De documentatie (overdracht, revisielog, nodes) wordt NIET meer hier
bijgewerkt. Dat doet GitHub automatisch in de cloud na elke push
(via .github/workflows/update-docs.yml). Zo kan er nooit meer een
conflict ontstaan doordat twee plekken dezelfde bestanden aanpassen.

Wil je de documentatie tóch handmatig bijwerken (bijvoorbeeld om lokaal
te kijken)? Draai dan los: python genereer_docs.py

Gebruik:
    python update.py
"""

import verwerk_facturen


def main():
    print("Facturen verwerken en dashboard bouwen")
    print("-" * 50)
    verwerk_facturen.main()
    print("\nKlaar. De documentatie wordt automatisch door GitHub bijgewerkt na het pushen.")


if __name__ == "__main__":
    main()
