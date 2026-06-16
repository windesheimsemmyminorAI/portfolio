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

### Definitieve panelen (`-gekozen`) — in verhaalvolgorde van de strip

| # | Paneel | Scene |
|---|---|---|
| 1 | `beat-1-rust-gekozen` | rust in de tuin (vlinder) + content close-up |
| 2 | `beat-2-alert-b-gekozen` | alert staan + opgewonden kop (bliksem/sterren) |
| 3 | `beat-4-rennen-e-gekozen` | rent weg + ravot in stofwolk |
| 4 | `beat-3-kier-gekozen` | tuurt door de kier + lege straat met "?" |
| 5 | `beat-5-auto-sterretjes-gekozen` | ziet de auto aankomen + ogen met sterretjes ✨ |
| 6 | `beat-6-titelkaart-gekozen` | titelkaart **"THE FAMILY ARRIVES"** |
| 7 | `beat-7-finale-gekozen` | finale: zoomies met hartjes + propeller-staart |

> De volledige set komt 1-op-1 overeen met de panelen in de strip-HTML.

### Varianten / opties (niet gebruikt)

- `beat-2-alert-a`
- `beat-3-kier-a` … `-d`
- `beat-4-rennen-a` … `-d`

### Overige renders

Twee eerdere renders met een **onafgemaakte (grijze) onderhelft** zijn vervangen
door de schone `-gekozen` panelen hierboven en blijven als iteratie bewaard:

- een **full-body reveal**-render (2 staande poses) → `phase-0-spec/characters/wolfje/model-sheets/wolfje-jv-modelsheet-gemini-afgekapt.png`;
- de eerdere **"spot door de schutting"**-render → `_archief/wolfje-bella-s1e01-render-kapot.png` (nu vervangen door `beat-3-kier-gekozen`).
