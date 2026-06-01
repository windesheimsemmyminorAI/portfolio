"""
update.py
=========

Het gemak-commando. Draait alles in één keer:
  1. Controleert de facturen en bouwt het dashboard
  2. Werkt de documentatie bij (overdracht, revisielog, nodes)

Gebruik:
    python update.py
"""

import verwerk_facturen
import genereer_docs


def main():
    print("Stap 1: facturen verwerken en dashboard bouwen")
    print("-" * 50)
    verwerk_facturen.main()

    print("\nStap 2: documentatie bijwerken")
    print("-" * 50)
    genereer_docs.main()


if __name__ == "__main__":
    main()
