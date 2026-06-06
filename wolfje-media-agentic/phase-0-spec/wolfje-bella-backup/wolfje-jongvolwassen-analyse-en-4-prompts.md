# 🐺 Wolfje — Jongvolwassen · Fotoanalyse + 4 test-prompts

**Doel:** vier prompts met **exact dezelfde tekenstijl** (gekozen cel-shaded richting), maar met een **verschillende formulering van Wolfjes kenmerken**, zodat we via vergelijking de best werkende formulering vinden. Belangrijkste correctiepunt t.o.v. de vorige ronde: de output werd te "kawaii"/vrouwelijk (te grote ogen, te bolrond, te bleek).

---

## 1. Fotoanalyse — lichaams- en gezichtskenmerken

Gebaseerd op de echte foto's in dit project (front op de bank, profiel-closeup, liggend op het kussen, plus een jongere vergelijkingsfoto).

### Gezicht
- **Overwegend wit gezicht** met een brede, schone **witte bles** over de snuit, wangen, rond de ogen en het midden van het voorhoofd.
- **Zachte, bleke abrikoos/perzik** uitsluitend op de **kruin** en vooral op de **achterkant en punten van de grote oren** — duidelijk **lichter dan klassiek Pommetjes-oranje**, en het vervaagt zacht in het wit (geen harde rand).
- **Grote, rechtopstaande, driehoekige oren**, zwaar **gevederd** met lange franjes die uitsteken (langharig).
- **Donkere, ronde ogen**, **middelgroot / natuurlijk formaat**, iets amandelvormig; rustige, licht ingetogen-maar-alerte blik; onder fel licht een vleugje amber. → **Niet** de grote glanskraal-/anime-ogen.
- **Klein neusje**, overwegend **zwart** met wat bruine/roze spikkeling (leest als zwart op afstand).
- **Korte, fijne, licht spitse vosachtige snuit** (Chihuahua × Pom) — geen platte, ingedrukte Pom-snuit. Witte snorharen.
- Subtiele lichte traanstreepjes onder de binnenste ooghoek (minimaal — niet benadrukken).
- Bek meestal een **rustige gesloten lijn**; kan open met klein tongpuntje.

### Lichaam
- **Langharige toy-hond** (Pom × Chihuahua), **fijn gebouwd**, klein en lichtgebouwd.
- Basis **crème/wit**; een **warme abrikoos "zadel"** over rug en schouders (op de jongere foto duidelijker zichtbaar), flanken/onderzijde lichter.
- **Witte borst, witte poten, witte voeten** (roze/gespikkelde voetzolen).
- **Lange vedering:** zware franjes aan de oren, een **leeuwachtige kraag** rond hals/borst, en **"broekjes"** (vedering) achter de poten.
- **Pluimstaart**, sterk gevederd, **krult op en over de rug**; crème-wit met abrikoostint.
- **Jongvolwassen bouw:** iets **langer lijf** en **slankere poten** dan de bolronde pup → níet als ronde pluizenbol weergeven.

### Wat de output "te vrouwelijk" maakte
1. Ogen te groot/te rond (kawaii) → moet natuurlijk formaat + iets amandelvormig.
2. Silhouet te bolrond/donzig → moet slanker, jongvolwassen.
3. Vacht bijna helemaal wit, abrikoos-zadel verdwenen → zadel + warme crème-toon terugbrengen.
4. Blik te zoet → mag iets zelfverzekerder/alerter.

---

## 2. Constanten (in alle 4 de prompts identiek)

**Stijlregel (NIET wijzigen):**
> `... redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, soft shading, warm and gentle, colorful and family-friendly (Cocomelon-leaning).`

**Openingsregel:**
> `Using the attached reference photos of the real dog "Wolfje" (young adult),`

**Afsluiting:**
> `Pose: sitting in a relaxed 3/4 front pose, full body visible. Plain soft pastel background, soft warm lighting. No text, no letters, no watermark. Square 1:1.`

*Foto's meegeven:* de heldere front-foto (kop/borst/voorpoten vullen het beeld) + de profiel-closeup (voor oog/snuit/oorkleur) + één lichaamsfoto (voor bouw/staart).

---

## 3. De 4 prompts (zelfde stijl, andere formulering van de kenmerken)

### Prompt A — Anatomisch-precies (kleur per zone)
*Strategie: de foto's zo letterlijk mogelijk volgen, kleur strikt per lichaamszone.*

```
Using the attached reference photos of the real dog "Wolfje" (young adult), redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, soft shading, warm and gentle, colorful and family-friendly (Cocomelon-leaning). This is a SPECIFIC real dog — match the reference exactly, do NOT generalise into a generic Pomeranian.
Coat colour by zone: predominantly white / cream. A soft, pale apricot wash sits ONLY on the crown of the head and on the outer/back of both large erect ears, fading gradually into the white (no hard edges); plus a faint warm apricot saddle over the upper back and shoulders. A broad clean white blaze runs up the muzzle and forehead; muzzle, cheeks, chest, belly, all four legs and paws are white.
Coat type: long, fine, silky long-haired coat with heavy feathering on the ears, a full lion-like ruff around the neck and chest, feathered "trousers" behind the legs, and a long fluffy plume tail curling up over the back.
Head: short, fine, slightly pointed fox-like muzzle (Chihuahua × Pomeranian), small mostly-black nose, medium dark-brown round eyes of NATURAL size set fairly wide, gentle alert expression, mouth a soft closed line.
Build: petite young-adult toy dog with a slightly elongated body and slender, fine-boned legs.
Pose: sitting in a relaxed 3/4 front pose, full body visible. Plain soft pastel background, soft warm lighting. No text, no letters, no watermark. Square 1:1.
```

### Prompt B — Negatieve sturing (corrigeert het "te vrouwelijk")
*Strategie: nadrukkelijk wegsturen van de kawaii/te zoete uitkomst.*

```
Using the attached reference photos of the real dog "Wolfje" (young adult), redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, soft shading, warm and gentle, colorful and family-friendly (Cocomelon-leaning). Keep him looking poised and alert — a confident young-adult dog, NOT dainty, NOT babyish, NOT overly cute.
Eyes: medium, dark, slightly almond-round, NATURAL size — do NOT enlarge into big glossy anime/kawaii eyes (that reads too soft and feminine).
Build: lean young-adult proportions, a slightly longer body and slender legs — do NOT render the body as a round fluffy ball.
Coat: mostly white / cream; soft PALE apricot ONLY on the crown and the backs of the large erect feathered ears (low saturation, NOT bright orange), plus a faint apricot saddle on the upper back; white facial blaze, muzzle, chest, legs and paws.
Keep: lion-like neck ruff, feathered legs, long plume tail curling over the back, short fine fox-like muzzle, small dark nose.
Expression: friendly but self-assured — a calm closed-mouth smile (no tongue, or only a tiny tongue tip).
Pose: sitting in a relaxed 3/4 front pose, full body visible. Plain soft pastel background, soft warm lighting. No text, no letters, no watermark. Square 1:1.
```

### Prompt C — Holistisch (silhouet + karakter)
*Strategie: minder micro-details, meer totaalindruk, vosachtig en zelfverzekerd.*

```
Using the attached reference photos of the real dog "Wolfje" (young adult), redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, soft shading, warm and gentle, colorful and family-friendly (Cocomelon-leaning).
Overall impression: a small fox-like long-haired toy dog who looks bright, curious and quietly confident. The silhouette reads as a slim, feathery young adult — big erect feathered ears, a full neck ruff, slender legs and a long plume tail arcing over the back — never a round puffball.
Colour at a glance: a white / cream dog with just a warm apricot cap on the head and the backs of the ears, plus a soft apricot blanket over the back; everything below (white facial blaze, chest, legs, paws) stays white.
Face: fine pointed fox-muzzle, small dark nose, calm dark eyes of natural size, an alert friendly look.
Mood: gentle and warm, with a touch of cheeky self-assurance rather than baby-soft cuteness.
Pose: sitting in a relaxed 3/4 front pose, full body visible. Plain soft pastel background, soft warm lighting. No text, no letters, no watermark. Square 1:1.
```

### Prompt D — Referentie-verankerd (verhoudingen)
*Strategie: sturen op verhoudingen t.o.v. de foto's om rasdrift te voorkomen.*

```
Using the attached reference photos of the real dog "Wolfje" (young adult), redraw the SAME dog as a cute 2D cel-shaded cartoon, clean confident linework, soft shading, warm and gentle, colorful and family-friendly (Cocomelon-leaning). Treat the attached photos as ground truth and match his proportions precisely — not a breed stereotype.
Proportions to respect: eyes take up a modest, natural share of the face (real-dog scale — do NOT inflate them); muzzle is short, fine and slightly pointed (fox-like), clearly present (NOT a flat pushed-in Pomeranian face); ears are large, erect and heavily feathered, set high; the body is a touch longer than it is tall with slim feathered legs (young-adult, NOT puppy-round).
Markings to match: white / cream base; pale apricot confined to the head-crown and the backs of the ears, plus a faint apricot saddle over the back; broad white facial blaze; white chest, ruff, legs and paws.
Texture: long silky feathering, lion-like ruff, long plume tail curling over the back.
Expression: friendly, gentle, quietly confident; eyes dark and clear.
Pose: sitting in a relaxed 3/4 front pose, full body visible. Plain soft pastel background, soft warm lighting. No text, no letters, no watermark. Square 1:1.
```

---

## 4. Hoe te testen
1. Draai elke prompt **2–3×** met dezelfde meegegeven foto's (modellen variëren per run).
2. Beoordeel op: **ooggrootte** (natuurlijk?), **bouw** (slank jongvolwassen, geen bolronde pup?), **kleur** (wit + abrikoos-zadel terug?), **blik** (zelfverzekerd i.p.v. te zoet?).
3. Kies de winnende **formulering** → die wordt de basis voor het **canon-referentiebeeld**, waarna pup en eerste periode worden afgeleid.

> **Noodgreep oren** als ze tóch te oranje worden: vervang "soft, pale apricot" door "very pale cream with the faintest warm beige hint".
