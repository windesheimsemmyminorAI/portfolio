# 🐺 Gemini-prompts v2 — JONGVOLWASSEN Wolfje (ONTPLUIZING / slank silhouet)

**Herkomst:** tweede Gemini→Gemini ronde. Na het testen van v1 bleek het beeldmodel Wolfje als een dichte Pommerian-pluizenbol te tekenen. Deze v2 corrigeert dat gericht.
**Status:** in test. Vervangt v1 als actieve kandidatenset voor de jongvolwassen-lock.

---

## ⚠️ Wat v2 verandert t.o.v. v1 (canon-aanscherping)
Deze ronde wijkt op twee punten bewust af van de eerder vastgelegde beschrijving — bevestigd door de maker:
1. **Veel minder vacht.** Geen "massive/cloud/explosion/dense/thick" meer. Vacht expliciet **4–5 cm, fijn, wispy, silky, naar beneden vallend** — een lichte franje, geen deken. Het slanke, fijngebouwde Chihuahua-achtige lijf moet zichtbaar blijven.
2. **Abrikoos nóg strakker.** Abrikoos nu **uitsluitend op de achterkant van de oren**; kruin-kap en rug-zadel zijn losgelaten. Gezicht, borst, lijf, poten en voorkant oren zijn puur wit.
3. **Ruff teruggeschroefd** van "lion-like" naar een **bescheiden, wispy kraagje van 4–5 cm**.

> Werkt v2 goed → werk de canonbeschrijving in `PROGRESS-LOG.md` / spec bij naar deze versie, zodat pup en eerste periode hierop verder bouwen.

---

## Gemini's zelfreflectie (door maker goedgekeurd)

**Wat ging mis in v1:**
- *Pomeranian-archetype overdrive:* woorden als "massive", "voluminous cloud", "explosion of hair" triggerden het AI-archetype van een raszuivere show-Pommerian.
- *Verlies van anatomie:* het lijf verdween in een dichte driehoek vacht; poten leken stompjes doordat de vacht tot de grond hangt. Het slanke Chihuahua-frame ging verloren.
- *Verkeerde vachttextuur/-lengte:* echte Wolfje heeft fijn, wispy, zijdeachtig haar van ~4–5 cm; v1 gaf een dikke, stijve, naar buiten puffende vacht.

**Wat goed ging:**
- Kleurverdeling flink beter (gezicht/borst/lijf wit, geen oranje zadel).
- 2D cel-shaded stijl en gezichtsuitdrukking (glimlach, donkere ogen) goed gevangen.

**Doorgevoerde verbeteringen:**
- "Cloud"-vocabulaire volledig geschrapt.
- Expliciete vachtlengte/-textuur: "moderately long (about 4 to 5 cm)", "wispy", "silky", "falling naturally downward".
- Anatomie-zichtbaarheid verplicht gesteld: slank lijf moet door de vacht heen zichtbaar zijn.
- Ruff teruggebracht naar "modest, wispy collar of 4-5 cm hair".
- Kleurlocks behouden: gezicht/lijf puur wit, vage abrikoos alleen achterkant oren.

---

## De 5 v2-prompts

### Variant 1 — pastel LAVENDEL
```
A 2D cel-shaded cartoon illustration of Wolfje, an exceptionally small, slender Pomeranian-Chihuahua mix. It is critical that his body does NOT look like a dense, round puffball. He has a very dainty, delicate frame that remains clearly visible. His coat consists of moderately long (about 4 to 5 cm), fine, silky, wispy hair that falls naturally downward rather than puffing outward. His fur is predominantly bright pristine white. The only color is a very faint, subtle apricot wash strictly limited to the back surfaces of his erect ears; the front of the ears, the entire face, and the body are pure white. He has a short, fine white fox-like muzzle, a small dark nose, and natural-sized dark almond eyes. He wears a calm, friendly smile. He has a modest, wispy collar of fur around his neck and light, wispy feathering on his slender legs. He is sitting in a 3/4 front view, showing all four tiny paws clearly, with his lightly plumed tail resting over his back. Set against a solid soft pastel lavender background with gentle lighting. No text, no watermarks. Aspect ratio 1:1.
```

### Variant 2 — pastel MINTGROEN (met tipje tong)
```
A delicate 2D cel-shaded cartoon character illustration of a tiny, very slender Pomeranian-Chihuahua mix. The dog has a slight, fragile anatomy that must be clearly recognizable, avoiding any heavy, bulky, or overly fluffy Pomeranian stereotypes. His hair is silky, wispy, and only about 4 to 5 cm long, creating a light fringe rather than a thick coat. The fur is brilliant white across the face, chest, body, and the front of the ears. A very slight, diluted apricot tone appears exclusively on the reverse (back) side of his prominent, lightly feathered ears. The face features a fine, delicate short muzzle and distinct natural dark eyes with a friendly, self-assured expression and a tiny visible tongue tip. He sits gracefully, his slim legs and tiny paws fully visible beneath the naturally draping 4-5 cm wisps of hair. His tail is lightly plumed, curling up. Solid soft pastel mint green background, warm natural lighting. No text, no watermarks. Aspect ratio 1:1.
```

### Variant 3 — pastel BLAUW (animation still)
```
A high-quality 2D cel-shaded animation still of a very small, dainty Pomeranian-Chihuahua mix dog. The prompt requires a slender, visible body shape—do not draw a massive ball of fluff. The dog's coat is fine, silky, and wispy, measuring only around 4 to 5 cm in length, allowing his slim form to show through the draping locks. His coat is pure, bright white everywhere—face, muzzle, chest, belly, legs, and the front of the ears. The only exception is a very faint hint of apricot color applied solely to the back side of his ears. He features a delicate, short, somewhat pointed white muzzle, a small black nose, and dark, kind eyes. He is sitting, facing 3/4 toward the camera, looking happy and confident. His slender legs are clearly visible, accented by 4-5 cm wispy feathering. Solid soft pastel blue background with clean, simple shading. No text, no watermarks. Aspect ratio 1:1.
```

### Variant 4 — pastel PERZIK (warm, familievriendelijk)
```
A warm, family-friendly 2D cel-shaded cartoon illustration of an exceptionally slender and tiny Pomeranian-Chihuahua mix. He is distinctly small-boned. His coat is not a dense cloud; rather, he has light, wispy, silky hair about 4 to 5 cm long that hangs loosely, framing his slim body without obscuring his underlying shape. The character is completely pure white (face, chest, front of the ears, body, paws). There is only a microscopic, faint touch of warm apricot on the very back surface of his tall ears. His facial features include a finely structured, short white muzzle, dark nose, and natural dark eyes conveying a gentle, confident smile. He sits in a relaxed 3/4 profile, ensuring his delicate slim legs and tiny paws are entirely visible, unhidden by heavy fur. The lightly plumed tail curls neatly. Solid soft pastel peach background with soft illumination. No text, no watermarks. Aspect ratio 1:1.
```

### Variant 5 — pastel GEEL (clean linework)
```
A clean 2D cel-shaded cartoon illustration of a miniature, very slender Pomeranian-Chihuahua mix. The artwork must emphasize his dainty underlying anatomy, ensuring he does not look like a thick, puffy show dog. His silky fur is wispy, light, and moderate in length (around 4 to 5 cm), draping softly rather than standing on end. His entire visible face, chest, body, and the front interior of his ears are pristine white. Exclusively on the exterior back of the ears is a very subtle, low-saturation apricot tint. He has a refined, short white muzzle, a small dark nose, and friendly, realistic dark eyes. He is sitting comfortably, displaying his slender, lightly feathered legs and tiny paws. He has a modest 4-5 cm wispy ruff at the neck and a loosely plumed tail. Solid soft pastel yellow background with warm, inviting lighting. Crisp linework and simple shadows. No text, no watermarks. Aspect ratio 1:1.
```

---

## Scoretabel (vul in tijdens testen)
Beoordeel 1–5 per punt (5 = perfect). Let v2 vooral op de twee nieuwe ijkpunten: **slank silhouet zichtbaar** en **vacht kort/wispy (geen pluizenbol)**.

| Variant | Achtergrond | Slank silhouet zichtbaar | Vacht kort & wispy (geen bol) | Kleur (wit + abrikoos alleen achter oren) | Ogen natuurlijk | Staart over rug | Totaalindruk | Run-notities |
|---|---|---|---|---|---|---|---|---|
| 1 | lavendel |  |  |  |  |  |  |  |
| 2 | mintgroen |  |  |  |  |  |  |  |
| 3 | blauw |  |  |  |  |  |  |  |
| 4 | perzik |  |  |  |  |  |  |  |
| 5 | geel |  |  |  |  |  |  |  |

**Beslisregel:** de formulering die over 2–3 runs het meest consistent een **slank, herkenbaar lijf met lichte 4–5 cm vacht** geeft, wordt de canon jongvolwassen.
