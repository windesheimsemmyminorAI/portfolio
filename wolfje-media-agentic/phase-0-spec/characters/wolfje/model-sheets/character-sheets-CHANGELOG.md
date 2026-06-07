# CHANGELOG — Wolfje & Bella Media Agentic

Doorlopend logboek van beslissingen en mijlpalen (nieuwste bovenaan). Dient ook als portfolio-bewijs van het denk- en bijsturingsproces.

> Let op: deze changelog is met terugwerkende kracht opgebouwd uit de beslislogs (`style-results-log.md`, `wolfje-jongvolwassen-prompt-v3.md`, `project_specification.md`). De data van vóór 7 juni zijn daaruit overgenomen; pas ze gerust aan als jouw commit-historie iets anders zegt.

---

## 2026-06-07 — Cel 01 (FRONT) VERGRENDELD — turnaround compleet

- `reference-material/character-sheets/wolfje-jv-turn-01-front.png` vastgelegd. De jongvolwassen turnaround model sheet is COMPLEET: cellen 01–05 allemaal locked.
- Bron: hoog-res front-render, op volle resolutie **gedownload** uit Gemini (niet gescreenshot), gebaseerd op de goedgekeurde kandidaat-C2-richting. Render bevatte twee honden; linker gekozen (rechter had dubbele-staart-artefact). Achtergrond geneutraliseerd naar off-white; abrikoos was al canon-correct, dus geen kleuringreep.
- Checklist volledig akkoord: warm crème · abrikoos alleen op de oren · slank lijf + vollere bef · fijne wispy vacht · één pluimstaart over de rug · vier poten · donkere natuurlijke ogen + vossenkopje · proportionele oren · schone contour.
- Kandidaat-backups bewaard onder `character-sheets/candidates/`: A, B, C, C2, D_hires.
- **Geleerd:** subtiele lokale kleur is onbetrouwbaar via Nano Banana (woord "apricot" → oranje masker); resolutie kwam van downloaden i.p.v. screenshotten; één hero-referentie > meerdere gemengde; de front mág de volste cel zijn (kraag framet naar voren, valt in profiel weg).

## 2026-06-07 — Turnaround-cellen 02–05 vergrendeld

- Image-to-image vanaf het canon-beeld, elke hoek apart vastgelegd: cel 02 (¾-front), cel 03 (zij), cel 04 (¾-achter), cel 05 (achter).
- Werkwijze: één hoek per keer, beoordeeld tegen de vaste checklist; front (cel 01) bewust als laatste/lastigste uitgesteld om de andere vier als referentie-stack te gebruiken.

## 2026-06-06/07 — Canon jongvolwassen Wolfje VERGRENDELD

- Bron van waarheid vastgelegd: `CANON-wolfje-jongvolwassen.md` + `wolfje-jongvolwassen-CANON.png` + `CANON-selectie-log.md`.
- Canon-spec: zeer klein/slank Pommerian×Chihuahua · warm crème/ivoor (niet stark wit) · vage abrikoos alleen op de oorruggen · fijne wispy 4–5 cm drapérende vacht · vollere zachte nek/kraag op slank lijf · grote rechtopstaande proportionele oren · korte fijne vossensnuit · donkere ogen natuurlijke grootte · volle pluimstaart over de rug · schone 2D cel-shaded Cocomelon-stijl.
- Canon-selectie als portfolio-bewijs gelogd: technisch sterkste render bewust verkozen boven de gut-favoriet, mét argumentatie.

## 2026-06-06 — Ronde 5: prompt v3 (cel-shaded jongvolwassen, gecorrigeerd)

- Output `output_v2_cel-shaded_jongvolwassen.png` geanalyseerd; wins behouden, regressies gecorrigeerd in v3.
- Behouden: natuurlijke ooggrootte, rustige zelfverzekerde expressie, slanke jongvolwassen bouw, witte bles/borst/poten, vossensnuit, consistente cel-shading.
- Gecorrigeerd in v3: (1) abrikoos te uitgebreid → strak begrensd tot oren + lichte kruin; (2) staart hing laag → omhoog/over de rug; (3) beenbevedering ("broek") teruggebracht; (4) vacht te plat/vector → langharig en gevederd.

## 2026-06-06 — Ronde 3: hero-foto + aangescherpt identity-block → cel-shaded GEKOZEN

- Vier stijlen met één heldere hero-foto; duidelijk betere gelijkenis.
- Beoordeling: 3D (duur/traag te animeren), vector (te sticker-achtig, minste gelijkenis), storybook/aquarel (mooiste zachtheid + gelijkenis maar schaalt slecht naar animatie en leest minder op klein scherm).
- **Besluit: cel-shaded als richting vergrendeld** — beste leesbaarheid op klein scherm, meest expressief voor educatieve comedy, best consistent te animeren. Zachtheid van de aquarel meegenomen via "soft shading, warm and gentle". Openstaand pijnpunt destijds: oren te oranje → bijgesteld in v2/v3.

## 2026-06-06 — Ronde 2: met echte foto's + kleurcorrectie

- Generatie mét echte Wolfje-foto's + harde kleurregel ("mostly white/cream, apricot alleen op kop/oren").
- Kleurverdeling beter, maar nog generiek. Oorzaken: unieke aftekening niet vastgelegd, ogen te groot, rasdrift, te veel/gemengde referentiefoto's.
- Conclusie: één heldere hero-foto + exact identity-block + ogen op natuurlijk formaat.

## 2026-06-05 — Ronde 1: stijlexploratie (zonder foto's)

- Vier varianten (3D / vector / storybook / cel-shaded), alleen tekstbeschrijving.
- Stijlen geslaagd, maar te oranje over het hele lijf en geen gelijkenis. Conclusie: echte foto's als referentie nodig.

## 2026-06-05 — Architectuurcorrecties Phase 0-spec

- DALL-E verwijderd (geen OpenAI-abonnement); **Veo** vervangt generieke Gemini-videogeneratie (geïmplementeerd als long-running operation met polling).
- Prompt caching gecorrigeerd naar binnen-run (TTL max één uur, niet cross-day).
- N8N-expressiesyntax gecorrigeerd van Jinja naar JavaScript.
- Speech bubbles als tekstoverlay (beeldmodellen renderen in-beeld-tekst onbetrouwbaar).

## 2026-06-05 — Projectopzet & leidende stijlbeslissing

- Doel: AI-pijplijn voor dagelijkse cartoon-strips + korte video's met Wolfje (en Bella) → TikTok / Instagram / YouTube Shorts, familievriendelijk, Engels, doelgroep hondenliefhebbende vrouwen ~18–45.
- **Stijlbeslissing:** schattige, kleurrijke, familievriendelijke Cocomelon-toon is leidend; de detail-inktstijl (referentie van de nicht) alleen als accent voor dramatische momenten, nooit als basis.
- Fasenstructuur vastgelegd (Phase 0 character/style-lock → Phase 1 prompts → Phase 2 N8N-workflow → Phase 3 self-learning → Phase 4 dashboard → Phase 5 metrics).
