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
per verhaalmoment (beat) met varianten (`-a`, `-b`, …). De maker heeft de
**definitief gebruikte** panelen aangewezen; die dragen het achtervoegsel
`-gekozen`. Alle overige varianten zijn **opties/alternatieven**.

| Paneel | Status |
|---|---|
| `beat-1-rust-gekozen` | **definitief** (rust in de tuin + close-up) |
| `beat-2-alert-b-gekozen` | **definitief** (alert + opgewonden kop) |
| `beat-2-alert-a` | optie |
| `beat-4-rennen-e-gekozen` | **definitief** (rent weg + ravot in stof) |
| `beat-4-rennen-a` … `-d` | opties |
| `beat-3-kier-a` … `-d` | opties (tuurt door de schutting) |

> **Niet als los, schoon bestand bewaard:** enkele eindpanelen bestaan alleen
> ingebouwd in de strip-HTML (auto-aankomst + sterretjesogen, titelkaart
> "THE FAMILY ARRIVES", hartjes-finale). Daarnaast zijn er twee door de maker
> als definitief aangewezen renders met een **onafgemaakte (grijze) onderhelft**,
> die daarom niet als nette eindpanelen zijn opgenomen:
> - een **full-body reveal**-render (2 staande poses) → staat als referentie in
>   `phase-0-spec/characters/wolfje/model-sheets/wolfje-jv-modelsheet-gemini-afgekapt.png`;
> - een **"spot door de schutting"**-render → staat in
>   `_archief/wolfje-bella-s1e01-render-kapot.png`.
>
> Zodra hiervan een schone versie bestaat, kunnen ze als `-gekozen` paneel
> naar deze map verhuizen.
