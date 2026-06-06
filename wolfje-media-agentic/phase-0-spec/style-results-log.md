# 🎨 STYLE RESULTS LOG — RONDE 2 (met echte foto's)

**Datum:** 6 juni 2026
**Wat:** stijlvarianten gegenereerd mét echte Wolfje-foto's als referentie (single prompts + 3-stage).
**Resultaten:** zie `style-results/round-2/`.

## Uitkomst
Kleurverdeling nu goed (overwegend wit/crème, abrikoos op kop/oren). **Maar gelijkenis nog onvoldoende** — het blijft een *generiek* schattig hondje, niet specifiek Wolfje. Dichtst in de buurt: **cel-shaded (variant D)** — `single_D_celshaded.png` en `3stage_D_celshaded.png`.

## Waarom het nog niet lijkt (4 oorzaken)
1. **Unieke aftekening niet vastgelegd** → model verzint generieke vlekken i.p.v. zijn echte patroon (abrikoos-cap op kop/oren, witte bles, abrikoos zadel op rug).
2. **Ogen te groot** ("big expressive eyes" → Disney-drift) verandert zijn hele gezicht.
3. **Rasdrift** naar Papillon/Pomeriaan (te grote oren / te ronde kop) i.p.v. zijn spitse vosachtige Chihuahua×Pom-kop.
4. **Te veel verschillende referentiefoto's tegelijk** (mix leeftijden/hoeken/wazig) verwatert de identiteit.

## Oplossing in de prompt
- Gebruik **één scherpe hero-foto** (niet een mix).
- Voeg het **identity-block** toe (exacte aftekening).
- Ogen terug naar **natuurlijk formaat**.
- **Dwing identiteit af:** "match his exact markings from the reference photo, do not generalise."

### Wolfje identity-block (in elke prompt opnemen)
```
This is a SPECIFIC real dog named "Wolfje" — match his exact markings from the reference photo, do not generalise. Markings: body and legs pure white/cream; warm apricot/tan covers the EARS and forms a cap over the top of the head and around the eyes; a WHITE BLAZE runs down the centre of the forehead and muzzle; muzzle, cheeks, chest, belly and paws are white; ONE apricot patch (saddle) on the upper back near the shoulders; cream plume tail with a little apricot near the base. Short, fine, slightly pointed fox-like muzzle (Chihuahua x Pomeranian) — NOT a flat round Pomeranian face, NOT a Papillon. Medium erect triangular feathered ears (not oversized). Round dark eyes, friendly, NATURAL size (not oversized cartoon eyes).
```

### Verbeterde prompt (cel-shaded jongvolwassen — startpunt)
```
Using the ONE attached reference photo of the real dog "Wolfje", redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, colorful, soft and family-friendly (Cocomelon-leaning).
[identity-block hierboven]
Pose: sitting 3/4 front, full body, friendly happy expression, tongue tip out. Plain soft pastel background, soft warm lighting. No text, no watermark. Square 1:1.
```
> Andere stijlen: vervang alleen de eerste (stijl)zin; identity-block identiek houden.

## Eerlijke verwachting & route
Een exacte cartoon-match van een specifieke echte hond is lastig voor huidige modellen. Route: maak een **herkenbaar genoeg** beeld → **leg dat vast als canon (hero)** → genereer al het andere daarvan af. Consistentie > perfecte foto-match. Niet blijven jagen op 1-op-1.

## Volgende stap
- [ ] Cel-shaded jongvolwassen opnieuw met identity-block + één hero-foto.
- [ ] Bij goede gelijkenis → vastleggen als canon → pup & eerste-periode afleiden → model sheets → style-lock.
