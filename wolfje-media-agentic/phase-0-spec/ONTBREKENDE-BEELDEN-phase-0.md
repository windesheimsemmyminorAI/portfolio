# 🕳️ ONTBREKENDE BEELDEN — PHASE 0 (known gaps)

Dit logboek documenteert welke Wolfje-versies/opties uit Phase 0 **wél in tekst** zijn vastgelegd
(in de iteratie- en selectielogboeken) maar **niet als afbeelding** in de repo bewaard zijn.
Doel: transparantie over het beslisproces voor het portfolio en een checklist voor eventueel later
aanvullen.

> Bron: analyse van `character-design-iterations.md`, `style-results-log.md`,
> `wolfje-bella-backup/CANON-selectie-log.md` en
> `wolfje-bella-backup/model-sheets/wolfje-jongvolwassen-turnaround-prompts.md`,
> afgezet tegen de daadwerkelijk gecommitte bestanden.

---

## 1. Ronde 1 ontbreekt volledig
Het logboek zegt letterlijk: *"Beeldmateriaal: niet in repo bewaard (vroege test)."*
De vroegste stijlvarianten / afgewezen beelden van Ronde 1 (stijlexploratie zonder foto's:
3D / vector / storybook / cel-shaded) zijn er dus **niet**.

- **Status:** alleen beschreven in `character-design-iterations.md` (Ronde 1).
- **Impact:** de allereerste stijlrichting is niet visueel terug te zien.

## 2. Afgewezen canon-renders ontbreken als bestand
Van de nek-edit-ronde is alleen **Render 3** (de canon) opgeslagen als
`wolfje-jongvolwassen-CANON.png`. De afgewezen **Renders 1, 2 en 4** bestaan alleen als
beschrijving in de checklist-tabel, **niet als afbeelding**.

- **Status:** alleen beschreven in `wolfje-bella-backup/CANON-selectie-log.md` (checklist-tabel).
- **Impact:** de visuele vergelijking die tot de canon-keuze leidde, is niet reproduceerbaar uit beeld.

## 3. Afgewezen turnaround-renders ontbreken grotendeels
Elke hoek van de turnaround is 2–3× gedraaid (de log noemt bv. "Render 4", "Render 6"),
maar per hoek is alleen de **gekozen cel** bewaard.

- **Uitzondering:** voor de lastige **front** zijn de kandidaten **A / B / C / C2 / D_hires** wél bewaard
  (`reference-material/character-sheets/candidates/`).
- **Status:** keuzes beschreven in `wolfje-bella-backup/model-sheets/wolfje-jongvolwassen-turnaround-prompts.md`.
- **Impact:** voor ¾-front, zij, ¾-achter en achter zijn de afgewezen alternatieven niet als beeld bewaard.

## 4. A/B/C/D-prompttest maar deels in beeld vastgelegd
De prompttest met 4 formuleringen (A/B/C/D), elk 2–3× gedraaid, is maar **deels** als afbeelding bewaard:
de **5 Gemini-varianten** (`Gemini_Generated_Image_*.png`) en **één v2-output**
(`output_v2_celshaded_jongvolwassen.png`). **Niet elke run van elke prompt** is als bestand opgeslagen.

- **Status:** prompts beschreven in `wolfje-bella-backup/wolfje-jongvolwassen-analyse-en-4-prompts.md`.
- **Impact:** niet alle prompt-formuleringen zijn één-op-één aan een beeld te koppelen.

---

## Samenvatting

| # | Onderwerp | In tekst vastgelegd | Beeld bewaard |
|---|-----------|:---:|:---:|
| 1 | Ronde 1 stijlexploratie | ✅ | ❌ |
| 2 | Afgewezen canon-renders (1, 2, 4) | ✅ | ❌ |
| 3 | Afgewezen turnaround-renders per hoek | ✅ | ⚠️ alleen front-kandidaten |
| 4 | A/B/C/D-prompttest runs | ✅ | ⚠️ deels (5 Gemini + 1 v2) |

> **Conclusie:** het beslisproces is volledig navolgbaar via de logboeken, maar niet álle versies en
> afgewezen beelden zijn als afbeelding bewaard. Wel volledig bewaard zijn Ronde 2 (9/9), Ronde 3 (6/6),
> de front-turnaround-kandidaten, de 5 definitieve turnaround-cellen, de canon, de Gemini-kleurvarianten
> en de input-referentiefoto's.

---

## Status — opgevolgd als GitHub-issues (2026-06-07)

De 4 punten zijn als trackbare taken op GitHub gezet, zodat ze afvinkbaar zijn:

| Punt | Issue |
|------|-------|
| 1 — Ronde 1 ontbreekt | [#1](https://github.com/windesheimsemmyminorAI/portfolio/issues/1) |
| 2 — Afgewezen canon-renders | [#2](https://github.com/windesheimsemmyminorAI/portfolio/issues/2) |
| 3 — Afgewezen turnaround-renders | [#3](https://github.com/windesheimsemmyminorAI/portfolio/issues/3) |
| 4 — A/B/C/D-prompttest deels | [#4](https://github.com/windesheimsemmyminorAI/portfolio/issues/4) |

---

## Reflectie — wat ik hiervan leer (persoonlijke ontwikkeling)

- **Bewaar afgewezen outputs, niet alleen de winnaar.** Een keuze is pas echt navolgbaar als de
  alternatieven óók als beeld bestaan. Tekst beschrijft *dat* iets is afgewezen; alleen het beeld laat
  *waarom* zien. Dit is direct portfolio-bewijs van mijn beslisproces.
- **Leg de bewaarregel vast aan de bron.** Vanaf de volgende generatieronde sla ik elke kandidaat
  meteen op in `reference-material/…` (bv. een `rejected/`-submap per ronde), zodat deze gaps niet
  opnieuw ontstaan.
- **Onderscheid "gedocumenteerd" van "gearchiveerd".** Een logboek-tabel is documentatie; de bijbehorende
  bestanden zijn het archief. Beide zijn nodig voor reproduceerbaarheid.
