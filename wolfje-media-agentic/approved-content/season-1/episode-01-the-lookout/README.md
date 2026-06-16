# Episode 1 — "The Lookout" (Seizoen 1)

Wolfje ligt rustig in de tuin, hoort iets, tuurt door de schutting en ziet de
auto van het gezin aankomen — en barst los in vrolijke zoomies. *The Lookout* =
Wolfje als wachter die als eerste ziet dat het gezin thuiskomt.

## Definitieve content (eindversie)

| Bestand | Wat |
|---|---|
| `wolfje-bella-s1e01-the-lookout-strip.html` | **De afgemaakte strip** — zelfstandige HTML met 7 ingebouwde panelen in verhaalvolgorde. Werkt offline (dubbelklik). |
| `wolfje-bella-s1e01-pagina-1.png` | Samengestelde pagina 1 (los beeld) |
| `wolfje-bella-s1e01-video-1.mp4` | Definitieve video-output 1 |
| `wolfje-bella-s1e01-video-2.mp4` | Definitieve video-output 2 |

## Verhaalvolgorde van de afgemaakte strip (7 panelen)

1. Rust in de tuin (vlinder) + content close-up
2. Alert staan + opgewonden kop (bliksem/sterren)
3. Rent weg + ravot in stofwolk
4. Tuurt door de kier van de schutting + lege straat met "?"
5. Ziet de auto van het gezin aankomen + ogen met sterretjes ✨
6. Titelkaart **"THE FAMILY ARRIVES"** — gezin bij het hek
7. Finale: vrolijke zoomies met hartjes en propeller-staart

## `panels/` — bronmateriaal (Gemini-generaties)

De losse panelen zijn de ruwe generaties waaruit de strip is gebouwd, benoemd
per verhaalmoment (beat) met varianten (`-a`, `-b`, …):

- `beat-1-rust-gekozen` — **gebruikt** in de strip (paneel 1)
- `beat-2-alert-a`, `beat-2-alert-b-gekozen` — `-b` is **gebruikt** (paneel 2)
- `beat-3-kier-a..d` — alternatieven voor paneel 4 (één variant is gebruikt)
- `beat-4-rennen-a..e` — alternatieven voor paneel 3 (één variant is gebruikt)

> Let op: de panelen 5, 6 en 7 van de eindstrip (auto-aankomst, titelkaart,
> hartjes-finale) zijn **nieuwere renders die niet als los bestand bewaard zijn**;
> ze bestaan alleen ingebouwd in de strip-HTML. De `-gekozen`-markering is daarom
> alleen gezet waar het bronpaneel met zekerheid in de eindstrip terugkomt.

Modelsheets en een onbruikbare render uit dezelfde generatieronde staan in
`phase-0-spec/characters/wolfje/model-sheets/` resp. `_archief/`.
