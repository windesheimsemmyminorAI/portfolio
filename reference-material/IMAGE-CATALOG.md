# 🖼️ IMAGE-CATALOG — Wolfje & Bella Media Agentic

Centrale catalogus die elk beeld traceerbaar maakt: niet alleen het plaatje, maar het **waarom** erachter (portfolio-bewijs). Groeit per chat.

**Status-legenda:**
`bronfoto` = echte foto van de hond · `experiment` = vroege test · `verworpen` = bewust afgevallen (met reden) · `gekozen-richting` = vergrendelde stijlrichting · `canon` = definitief vergrendeld referentiebeeld

> **Herkomst-disclaimer:** datums bij gegenereerde beelden volgen de sessie waarin ze beoordeeld zijn. Datums bij bronfoto's komen uit de bestandsnaam (opnamedatum).

---

## Chat 01 — workflow setup + stijlexploratie (6 juni 2026)

### Stijlreferentie

| Bestand | Map | Wat | Status |
|---|---|---|---|
| `niece_style_reference.jpeg` | `style-reference/` | Gedetailleerde inkttekening; dient als stijlbasis | referentie |

### Ronde 2 — met echte foto's (9 beelden) → `style-results/round-2/`

| Bestand | Stijl | Wat | Status |
|---|---|---|---|
| `single_A_3d.png` | 3D | Losse jongvolwassen-render | experiment |
| `single_B_vector.png` | Vector | Losse jongvolwassen-render | experiment |
| `single_C_storybook.png` | Storybook | Losse jongvolwassen-render | experiment |
| `single_D_celshaded.png` | Cel-shaded | Losse jongvolwassen-render | experiment |
| `3stage_3d_a.png` | 3D | Drie leeftijdsfasen naast elkaar (variant a) | experiment |
| `3stage_3d_b.png` | 3D | Drie leeftijdsfasen (variant b) | experiment |
| `3stage_storybook.png` | Storybook | Drie leeftijdsfasen | experiment |
| `3stage_vector.png` | Vector | Drie leeftijdsfasen | experiment |
| `3stage_D_celshaded.png` | Cel-shaded | Drie leeftijdsfasen | experiment |

*Uitkomst ronde 2: kleurverdeling beter, maar nog generiek → reden om naar één hero-foto + exact identity-block te gaan.*

### Ronde 3 — hero-foto + identity-block (6 beelden) → `style-results/round-3/`

| Bestand | Stijl | Wat | Status |
|---|---|---|---|
| `A1_3d.png` | 3D | Hero-render | verworpen — aaibaar maar duur/traag te animeren, minder onderscheidend |
| `A2_vector.png` | Vector | Hero-render | verworpen — te "sticker", minste gelijkenis |
| `A3_storybook.png` | Storybook | Hero-render (staand) | verworpen-als-richting — mooiste zachtheid/gelijkenis, maar aquarel schaalt slecht naar animatie |
| `A3_storybook_sit.png` | Storybook | Hero-render (zittend) | verworpen-als-richting (idem) |
| `A4_celshaded_a.png` | Cel-shaded | Hero-render variant a | gekozen-richting (kandidaat) |
| `A4_celshaded_b_CHOSENdirection.png` | Cel-shaded | Hero-render variant b | **gekozen-richting (vergrendeld)** |

*Uitkomst ronde 3: cel-shaded vergrendeld als richting; openstaand pijnpunt "oren te oranje" → chat 2.*

### Bronfoto's — echte Wolfje (12 beelden) → `source-photos/`

Gedeelde referentieset die in deze chat is gebruikt voor het verzamelen van de karakter-referentie. Klein genoeg voor git; conform `README.md` mogen lichte referentieframes in de repo.

| Bestand | Opname (uit bestandsnaam) |
|---|---|
| `20250801_164033.jpg` | 1 aug 2025 |
| `20260324_010146.jpg` | 24 mrt 2026 |
| `20260501_140420.jpg` | 1 mei 2026 |
| `20260501_140724.jpg` | 1 mei 2026 |
| `20260501_140725.jpg` | 1 mei 2026 |
| `20260518_194034.jpg` | 18 mei 2026 |
| `20260518_194125.jpg` | 18 mei 2026 |
| `20260518_194132.jpg` | 18 mei 2026 |
| `20260601_000746.jpg` | 1 jun 2026 |
| `20260605_170508.jpg` | 5 jun 2026 |
| `Snapchat398132089.jpg` | — (Snapchat-export) |
| `wolfje_voor.jpg` | — (vooraanzicht) |

---

## Chat 02 — jongvolwassen-verfijning · Ronde 5 (6 juni 2026)

### Ronde 5 — geanalyseerde output → `style-results/round-5/`

| Bestand | Stijl | Wat | Status |
|---|---|---|---|
| `output_v2_celshaded_jongvolwassen.png` | Cel-shaded | De v2-output die in chat 2 tegen de echte foto's is geanalyseerd; aanleiding voor prompt v3 (abrikoos te ruim, staart te laag, beenbevedering weg, vacht te plat) | verworpen — diende als correctie-input voor v3 |

*Referentie: round 5 gebruikte een 4-foto-subset uit `source-photos/` (front + profiel-closeup + lichaamsfoto + jongere vergelijkingsfoto), in het oorspronkelijke round-5-pakket hernoemd naar `wolfje-real-ref-01..04`. De originelen staan al in `source-photos/`; geen nieuw beeld nodig.*

*De 4 test-prompts (A/B/C/D) en v3 staan in `wolfje-jongvolwassen-analyse-en-4-prompts.md` en `wolfje-jongvolwassen-prompt-v3.md`. Eventuele test-renders daarvan: zie missing-checklist.*

## Chat 03 — Gemini→Gemini + canon-lock (6 juni 2026)

### Cel-shaded canon-grade render → `canon-candidates/`

| Bestand | Wat | Status |
|---|---|---|
| `Gemini_Generated_Image_jihli4jihli4jihl.png` | Cel-shaded jongvolwassen-render die de canon-spec volgt: crème/ivoor, abrikoos op oor-achterkant, slank lijf, pluimstaart over de rug, natuurlijke donkere amandelogen, zittende ¾-front pose | **kandidaat** (bevestigd door Semmy — dit is *niet* de vergrendelde canon, maar een kandidaat-render ernaast) |

### Echte referentiefoto's (achter/front) → `source-photos/rear-reference/`

Onscherpe foto's uit één sessie, geëxporteerd uit de Gemini-app (sterretje in de hoek). Waardevol als referentie voor de achteraanzicht-cellen (04/05).

| Bestand | Aanzicht |
|---|---|
| `Gemini_Generated_Image_e1y0yde1y0yde1y0.png` | Achter, staart/poten |
| `Gemini_Generated_Image_75x9mw75x9mw75x9.png` | Achter, rug/oren |
| `Gemini_Generated_Image_zct55azct55azct5.png` | Achter ¾, oren/kruin |
| `Gemini_Generated_Image_pkev1vpkev1vpkev.png` | Front, gezicht/oren |

> **Niet in projectkennis (alleen in GitHub/chat):** de officiële `wolfje-jongvolwassen-CANON.png` en de vergrendelde turnaround-cellen 02–05 (`wolfje-jv-turn-02..05`) + de v1/v2- en Render-kandidaten. Zie missing-checklist.

## Chat 04 — turnaround front cel + push (7 juni 2026)

**Geen nieuwe beelden in projectkennis.** Alle beelden van deze chat zijn in de sessie zelf naar GitHub gepusht (via GitHub Desktop) en zitten niet in de projectkennis die hier zichtbaar is:

| Verwacht bestand | Wat | Waar |
|---|---|---|
| `wolfje-jv-turn-01-*.png` | Vergrendelde vooraanzicht-cel (de laatste, moeilijkste cel) | GitHub: `reference-material/character-sheets/` |
| cel 01-kandidaten | Portfolio-bewijs van de front-cel-selectie | GitHub (controleren) |
| turnaround-strip (5 cellen) | Samengestelde complete turnaround | GitHub (controleren) |

Zie missing-checklist. De technische beeldverwerking van deze chat staat in `docs/tool-knowledge/image-processing-pipeline.md`.

## Chat 05 — reflectie/rubric (7 juni 2026)

**Geen beelden.** Deze chat produceerde een Nederlandstalig reflectierapport (negen-dimensie-rubric, eerlijke zelfbeoordeling). Tekstartefact, geen beeldmateriaal — zie `docs/session-logs/chat-05-rubric-reflectie.md` en de missing-checklist voor het rapport zelf.
