# 📚 CHARACTER & STYLE — ITERATIE-LOGBOEK

Dit logboek documenteert de **evolutie** van Wolfjes karakterontwerp en de tekenstijl, zodat het denkproces en de bijsturing navolgbaar zijn (portfolio). Elke ronde heeft een eigen map onder `reference-material/style-results/`.

---

## Ronde 1 — Stijlexploratie (zonder foto's)
**Datum:** 5 juni 2026
**Prompt:** `style-exploration-prompts.md` (4 varianten: 3D / vector / storybook / cel-shaded), alleen tekstbeschrijving.
**Resultaat:** stijlen geslaagd, maar **te oranje over het hele lijf** (generiek Pommetje); geen gelijkenis.
**Beeldmateriaal:** niet in repo bewaard (vroege test).
**Conclusie:** tekst alleen is onvoldoende → echte foto's als referentie meegeven.

## Ronde 2 — Met echte foto's + kleurcorrectie
**Datum:** 6 juni 2026
**Map:** `reference-material/style-results/round-2/` (9 beelden: 4 single + 5 three-stage)
**Prompt:** `style-prompts-v2-met-fotos.md` ("mostly white, apricot alleen op kop/oren").
**Resultaat:** kleurverdeling beter, maar nog **generiek** (geen specifieke gelijkenis). Analyse in `style-results-log.md`.
**Oorzaken:** unieke aftekening niet vastgelegd · ogen te groot · rasdrift · te veel/mix referentiefoto's.
**Conclusie:** één heldere hero-foto + exact identity-block + ogen op natuurlijk formaat.

## Ronde 3 — Hero-foto + aangescherpt identity-block
**Datum:** 6 juni 2026
**Map:** `reference-material/style-results/round-3/` (6 beelden, jongvolwassen)
**Prompt:** `character-generation-prompts.md` sectie A (4 stijlen) met één hero-foto.
**Resultaat:** duidelijk betere gelijkenis (overwegend wit, abrikoos op oren, vosachtige kop).
**Beoordeling:**
- 3D (A1): aaibaar maar duur/traag te animeren, minder onderscheidend.
- Vector (A2): te "sticker"-achtig, minste gelijkenis.
- Storybook (A3, A3_sit): mooiste *zachtheid* en gelijkenis, **maar** aquarel schaalt slecht naar animatie en leest minder op klein scherm.
- **Cel-shaded (A4_a, A4_b): GEKOZEN richting.** Beste leesbaarheid op klein scherm, meest expressief voor educatieve comedy, best consistent te animeren binnen de stack.
**Maker-feedback:** storybook leek het meest op Wolfje (zachtheid), maar cel-shaded past het beste bij de projectdoelen. Openstaand pijnpunt: **oren te oranje**.
**Besluit:** cel-shaded vergrendelen als richting; **oren bijstellen naar zachte, lichte abrikoos** (zie A4 v2 in `character-generation-prompts.md`). De zachtheid van de aquarel wordt meegenomen via "soft shading, warm and gentle".

## Ronde 4 — (gepland) Canon-beeld jongvolwassen
**Status:** open
**Doel:** cel-shaded v2 (zachte oren) draaien met de hero-foto → beste resultaat vastleggen als **canon** → daarna pup & eerste periode afleiden → model sheets → **style-lock**.

---

> **Voor de beoordelaar:** de chronologie is ook te volgen via de Git-commit-historie (zie commits met "Phase 0 / round-x"). Per ronde is een map + dit logboek bijgewerkt.
