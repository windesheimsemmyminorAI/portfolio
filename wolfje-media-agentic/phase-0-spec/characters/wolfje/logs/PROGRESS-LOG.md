# 📌 VOORTGANGSLOG & BACKUP — Wolfje & Bella Media Agentic

**Backup gemaakt:** 6 juni 2026
**Doel van dit bestand:** snapshot van de stand van zaken, zodat je later naadloos verder kunt.

---

## Update — 2026-06-07 (project-hygiëne)

Versie-audit uitgevoerd op de repo. Bevinding: het beslisproces is volledig gedocumenteerd, maar
**niet alle afgewezen beelden zijn als bestand bewaard** (ronde 1, afgewezen canon-renders 1/2/4,
de meeste afgewezen turnaround-renders, en een deel van de A/B/C/D-prompttest).

- Vastgelegd in `phase-0-spec/ONTBREKENDE-BEELDEN-phase-0.md` en als GitHub-issues **#1–#4**.
- **Nieuwe werkafspraak:** vanaf de volgende generatieronde elke kandidaat/afgewezen render meteen
  opslaan (bv. een `rejected/`-submap per ronde), zodat deze gaps niet opnieuw ontstaan.
- Volledige sessie-analyse + leerpunten staan in `CHANGELOG.md` (Sessie J).

---

## Projectrol
**Claude = hoofdengineer** van dit project (architectuur, prompts, workflow, documentatie en correcties).
**Gemini = uitvoerend hulpmodel** voor het schrijven van zijn eigen Nano Banana beeldprompts (Gemini→Gemini), aangestuurd via de meta-prompt van Claude.

---

## Waar staan we nu

### Karakter-pipeline (Phase 0 — style & character lock)
- **Stijl gekozen:** 2D cel-shaded, Cocomelon-leunend (variant A4 = `A4_celshaded_b_CHOSENdirection.png`).
- **Actieve focus:** JONGVOLWASSEN Wolfje. ✅ **VERGRENDELD** (6 juni 2026) → `CANON-wolfje-jongvolwassen.md` is de bron van waarheid; definitief beeld = `wolfje-jongvolwassen-CANON.png` (Render 3, vollere nek + slank lijf).
- **Pup en eerste periode:** ⛔ nu aan de beurt — afleiden via image-to-image vanaf het canon-referentiebeeld (zelfde kleur/markeringen/stijl, jongere proporties).
- **Aanpak:** meta-prompt waarmee Gemini zelf de Nano Banana prompt schrijft → `wolfje_metaprompt_gemini_naar_nanobanana.md`.
- **Winnaar:** afbeelding 1 (blauw, v2-variant 3) → verfijnd tot canon-prompt (vollere staart + warm crème terug).
- **Promptgeschiedenis:** v1 (te oranje/pluizig) → v2 ontpluisd (`...-v2-defluffed.md`) → **canon** (`CANON-wolfje-jongvolwassen.md`).

### Vergrendelde karakterbeschrijving (canon — zie `CANON-wolfje-jongvolwassen.md`)
Zeer kleine, slanke, fijngebouwde Pommerian × Chihuahua mix; lijf duidelijk zichtbaar (geen pluizenbol). Vacht fijn/zijdeachtig/wispy ≈4–5 cm, valt naar beneden. Overwegend wit met zachte warme crème/ivoor toon; vage abrikoos UITSLUITEND op achterkant oren — rest zacht wit-crème. Korte fijne licht-spitse vossensnuit, klein donker neusje, donkere amandelogen op natuurlijke grootte, rustige vriendelijke zelfverzekerde blik. Grote rechtopstaande licht bevederde oren. Bescheiden wispy kraagje + lichte bevedering op slanke poten. Volle lange pluimstaart die uitwaaiert en over de rug krult. 2D cel-shaded, schone lijn, Cocomelon-toon. Blaf: vos-achtig "WHOOOWHOOOWOO".
> Dit vervangt de oudere pre-v2 beschrijving (kruin-kap + rug-zadel + leeuwen-ruff + lange vacht).

### Terugkerende faalpunten om op te scoren bij elke test
1. Te oranje / generiek Pommetje (kleur moet strak begrensd zijn)
2. Ogen te groot (moeten natuurlijke grootte zijn)
3. Bolronde pup i.p.v. slanke jongvolwassen
4. Staart hangt laag i.p.v. over de rug
5. Poten te glad i.p.v. bevederd

### Overige fases (eerder afgerond, ongewijzigd in deze backup)
- Phase 0: projectspecificatie + voorbereidingschecklist
- Phase 1: master-prompts (script, image, Veo, optimalisatie, self-reflection) — v2
- Phase 2: N8N workflow-architectuur (14 nodes, sequentieel) — v2
- Phase 3: self-learning loop met tagging, adaptatieregels, cold-start
- Phase 4: HTML approval-dashboard
- Phase 5: metrics-pipeline (TikTok route A + C)

---

## Volgende stappen (bij hervatten)
1. De 5 Gemini-varianten 2–3× draaien in Nano Banana met dezelfde 3 referentiefoto's; scoretabel invullen.
2. Winnende formulering kiezen → **canon jongvolwassen** vastleggen.
3. Pas dáárna: pup + eerste periode afleiden (image-to-image vanaf het goedgekeurde jongvolwassen-beeld).
4. Model sheets per leeftijd genereren en in `reference-material/character-sheets/` opslaan.
5. Resterende Phase 0 voorbereidingschecklist afronden vóór Day 1.

---

## Backup-inhoud
Deze backup bevat een volledige kopie van alle projectbestanden zoals aanwezig op de backupdatum, plus de nieuwe toevoegingen:
- `wolfje_metaprompt_gemini_naar_nanobanana.md` (nieuw — meta-prompt)
- `prompts-gemini-output/` (nieuw — 5 Gemini-prompts + ruwe originelen + scoretabel)
- `PROGRESS-LOG.md` (dit bestand)

Alle overige `.md`, `.png`, `.jpg` en `.html` bestanden zijn ongewijzigde kopieën uit de bestaande repo.
