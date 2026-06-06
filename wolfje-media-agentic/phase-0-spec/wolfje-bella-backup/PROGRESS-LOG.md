# 📌 VOORTGANGSLOG & BACKUP — Wolfje & Bella Media Agentic

**Backup gemaakt:** 6 juni 2026
**Doel van dit bestand:** snapshot van de stand van zaken, zodat je later naadloos verder kunt.

---

## Projectrol
**Claude = hoofdengineer** van dit project (architectuur, prompts, workflow, documentatie en correcties).
**Gemini = uitvoerend hulpmodel** voor het schrijven van zijn eigen Nano Banana beeldprompts (Gemini→Gemini), aangestuurd via de meta-prompt van Claude.

---

## Waar staan we nu

### Karakter-pipeline (Phase 0 — style & character lock)
- **Stijl gekozen:** 2D cel-shaded, Cocomelon-leunend (variant A4 = `A4_celshaded_b_CHOSENdirection.png`).
- **Actieve focus:** JONGVOLWASSEN Wolfje vergrendelen. ⏳ *Nog niet definitief gelockt.*
- **Pup en eerste periode:** ⛔ bewust uitgesteld tot jongvolwassen canon staat (worden daarna afgeleid via image-to-image vanaf het goedgekeurde beeld).
- **Nieuwe aanpak deze ronde:** meta-prompt waarmee Gemini zelf de Nano Banana prompt schrijft → `wolfje_metaprompt_gemini_naar_nanobanana.md`.
- **In test:** 5 door Gemini geschreven varianten → `prompts-gemini-output/wolfje-jongvolwassen-gemini-prompts.md` (+ ruwe originelen als `raw-gemini-variant*.txt`).

### Vergrendelde karakterbeschrijving (canon — niet wijzigen zonder reden)
Crème/ivoor langharige toy-hond (Pommerian × Chihuahua), overwegend WIT; warme zachte abrikoos alleen als vage kap op kruin + achterkant oren + heel vaag zadel over bovenrug dat in wit overloopt. Witte bles/snuit/borst/kraag/buik/poten. Donkere ronde ogen op natuurlijke grootte. Klein donker neusje. Korte fijne licht-spitse vossensnuit. Grote rechtopstaande zwaar bevederde oren. Leeuwachtige ruff. Lange "broek"-bevedering op alle poten. Lange pluimstaart die over de rug krult. Jongvolwassen verhoudingen (lijf iets langer dan hoog, slank — geen ronde puppybal). Blaf: vos-achtig "WHOOOWHOOOWOO".

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
