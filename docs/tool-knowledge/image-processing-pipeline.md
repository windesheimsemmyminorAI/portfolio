# 🛠️ Tool-knowledge — Beeldverwerkingspijplijn (Pillow)

**Herkomst:** Chat 04 (turnaround front cel), 7 juni 2026.
**Doel:** portfolio-bewijs van de deterministische post-processing die Nano-Banana-renders productie-klaar maakt. Deze technieken zijn betrouwbaarder dan re-generatie voor subtiele, gelokaliseerde correcties.

> **Kernprincipe:** waar het beeldmodel onbetrouwbaar is (bv. "apricot" → verzadigd oranje), corrigeer je **deterministisch in post-processing** i.p.v. opnieuw te genereren. Re-rollen herintroduceert alle andere faalmodi.

---

## 1. Achtergrond neutraliseren (grijze Gemini-UI → project off-white)

`ImageDraw.floodfill` vanuit **alle vier de hoeken plus de middens van elke rand**, met `thresh=30`, vervangt de grijze Gemini-achtergrond door de project-off-white `(248, 247, 243)` zonder in de hond te bloeden.

- Meerdere zaadpunten (hoeken + randmiddens) vangen achtergrondgebieden die niet aaneengesloten zijn.
- `thresh=30` is ruim genoeg voor de grijstinten maar bloedt niet door de lijncontour van de hond.

## 2. Bounding-box-detectie van de hond

Vergelijk elke pixel met de hoek-achtergrondkleur:

```
verschil = max(abs(r-bg[0]), abs(g-bg[1]), abs(b-bg[2]))
hond = verschil > thresh   # thresh 16–22 werkt betrouwbaar
```

De pixels boven de drempel vormen de hond → bounding box voor strak bijsnijden.

## 3. Abrikoos desatureren (oranje vossenmasker temmen)

Target pixels in HSV:
- **Hue** 15–55 (het oranje/abrikoos-bereik)
- **Saturation** > 0.22
- **Value** > 0.55 (sluit donker lijnwerk uit)

Verlaag de saturatie naar **30% van origineel**. In één pass effectief, **zonder** het lijnwerk of het crème-lijf aan te tasten.

## 4. Bekende artefacten & valkuilen

- **Hoogte-normalisatie-artefact (turnaround-strips):** cellen met een rechtopstaande pluimstaart hebben een grotere bounding box, waardoor hun lijf relatief kleiner oogt dan een front-cel zonder hoog staart-element. Gevolg: het vooraanzicht lijkt bonkiger dan het werkelijk is in de samengestelde strip. → houd hier rekening mee bij het beoordelen van proporties over cellen heen.
- **Twee-honden-composieten bijsnijden:** voor de specifieke 1024px-brede Nano-Banana-twee-honden-outputs werkte een splitpunt rond **x = 490**.
- **Resolutieval:** UI-screenshots cappen op ~140px per hond → altijd het volledige-resolutiebestand downloaden.

---

*Deze pijplijn hoort bij de bredere werkwijze: één hero-referentie i.p.v. gemengde referenties, gerichte correctie i.p.v. re-rollen, en beoordeling tegen de vaste checklist vóór vergrendeling.*
