# 📋 MISSING-IMAGES-CHECKLIST — handmatig te exporteren

Beelden die **alleen in een chat** leven (niet als projectkennis gekoppeld). De beeldbestanden hiervan kunnen niet automatisch opgehaald worden — Claude ziet bij het doorzoeken van chats alleen tekst, en Claude Code kan de chats sowieso niet bereiken. Exporteer deze handmatig (per-beeld downloaden uit de chat, of via Google Takeout als vangnet) en plaats ze in de aangegeven map.

**Vink af zodra geëxporteerd en geplaatst.**

---

## Chat 01 — workflow setup

- [ ] **Ronde 1 stijlexploratie (4 beelden, ~5 juni).** Volgens `style-results-log.md` *bewust niet bewaard* ("vroege test"). → **Actie: alleen exporteren als je ze nog wilt als bewijs van het allereerste experiment; anders overslaan.** Bestemming indien wel: `reference-material/style-results/round-1/`.
- [ ] **ffmpeg-frames uit referentievideo's (optioneel).** Tussenstap voor karakter-analyse. Alleen relevant als je het analyseproces wilt documenteren. Bestemming indien wel: `reference-material/source-photos/frames/`.

*Alle overige chat-01-beelden (round-2, round-3, bronfoto's, stijlreferentie) zitten al in de import — niets verder te exporteren.*

---

## Chat 02 — jongvolwassen-verfijning (Ronde 5)

- [ ] **Test-renders van prompts A / B / C / D (2–3× elk).** Chat 2 schreef vier formuleringsvarianten om te testen. Alleen de geanalyseerde `output_v2_celshaded_jongvolwassen.png` zit in projectkennis. → **Actie: als je destijds A/B/C/D-renders hebt gemaakt en wilt bewaren als bewijs van de vergelijking, exporteer ze.** Bestemming: `reference-material/style-results/round-5/candidates/`.
- [ ] **Test-renders van prompt v3 (2–3×).** De winnende v3-run was de kandidaat-canon. → **Actie: exporteren indien bewaard.** Bestemming: `reference-material/style-results/round-5/v3-candidates/`.

*Twijfel je of deze renders in chat 2 of pas in chat 3 zijn gemaakt? Dat los ik op bij het verwerken van chat 3 — mogelijk vallen ze daar onder de canon-kandidaten.*
## Chat 03 — Gemini→Gemini + canon-lock  ⚠️ HOOGSTE PRIORITEIT

> **Belangrijke bevinding:** de canon-documenten én de vergrendelde canon/turnaround-beelden van chat 3 zitten **niet** in de projectkennis die ik kan zien. Ze zijn destijds direct naar GitHub gepusht (chat 4). **Controleer eerst je huidige GitHub-repo** — als ze er al staan, hoef je ze NIET opnieuw te exporteren. Vink alleen af wat écht ontbreekt.

- [ ] **`wolfje-jongvolwassen-CANON.png`** — het vergrendelde canon-referentiebeeld (Render 3 uit hals-edit-ronde). Hét belangrijkste asset. → Bestemming: `reference-material/character-sheets/` (of `canon/`).
- [ ] **Turnaround-cellen 02–05** (`wolfje-jv-turn-02..05-*.png`) — de vier vergrendelde cellen. → Bestemming: `reference-material/character-sheets/`.
- [ ] **v1-kandidaten** (te oranje puffball) — als portfolio-bewijs van de fout-richting. → `reference-material/style-results/round-canon/v1/`.
- [ ] **v2-kandidaten + Render 1–5** — inclusief de niet-gekozen renders (o.a. Semmy's gut-favoriet Render 1). Bewijs van het selectieproces. → `reference-material/style-results/round-canon/v2/`.
- [ ] **Hals-edit-kandidaten** (image-to-image vollere kraag, waaruit Render 3 = canon kwam). → `reference-material/style-results/round-canon/neck-edit/`.

> **Bevestigd door Semmy:** `Gemini_Generated_Image_jihli4jihli4jihl.png` is een **kandidaat**, niet de vergrendelde canon. Het eerste vinkje hierboven (officiële `wolfje-jongvolwassen-CANON.png` exporteren) blijft dus staan. De kandidaat houden we als portfolio-bewijs in `canon-candidates/`.

> **Tweede-variant-notitie:** Gemini hangt meerdere gegenereerde varianten onder dezelfde bestandsnaam (in de app swipe je ertussen). Het geëxporteerde bestand bevat er maar één. Wil je een tweede variant bewaren, exporteer die dan apart uit de app. *Optioneel — alleen als die variant portfolio-waarde heeft.*
## Chat 04 — turnaround front cel + push

> In deze chat is alles via GitHub Desktop gepusht. **Grote kans dat onderstaande al in je GitHub-repo staat** — controleer eerst en exporteer alleen wat ontbreekt.

- [ ] **`wolfje-jv-turn-01-*.png`** — de vergrendelde vooraanzicht-cel. → `reference-material/character-sheets/`.
- [ ] **Cel 01-kandidaten** — de afgevallen front-cel-renders (incl. de Render 1 met Papillon-drift). Portfolio-bewijs. → `reference-material/character-sheets/candidates/cel-01/`.
- [ ] **Samengestelde turnaround-strip** (alle vijf cellen naast elkaar). → `reference-material/character-sheets/`.
- [ ] **Pre/post-processing-paren (optioneel)** — als je een "voor desaturatie / na desaturatie"-paar bewaart, is dat sterk portfolio-bewijs van de Pillow-pijplijn. → `reference-material/character-sheets/processing-demo/`.
## Chat 05 — reflectie/rubric

- [ ] **Reflectierapport (markdown)** — het negen-dimensie-zelfreflectierapport uit chat 5. Géén beeld, maar wel waardevol portfolio-bewijs. → `docs/reflectie/rubric-zelfreflectie.md`.
- [ ] **Drie rubric-bronbestanden (optioneel)** — alleen bewaren als dat binnen de minor is toegestaan. → `docs/reflectie/rubric-bronnen/`.
