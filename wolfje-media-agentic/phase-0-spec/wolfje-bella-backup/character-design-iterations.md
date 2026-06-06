# 🐺 PHASE 0 · STAP 0.3–0.4 — REFERENTIEBEELD & MODEL SHEETS

**Gebruik dit ná stap 0.1** (zodra je een stijl hebt gekozen uit `style-exploration-prompts.md`).
**Doel:** het definitieve, vergrendelde referentiebeeld van Wolfje in 3 leeftijdsversies + de model sheets die elke latere render consistent houden.

---

## 0. CONSISTENTIE-AANPAK (belangrijk — zo blijft het dezelfde hond)

1. **Plak je gekozen stijlregel** (de bovenste regel van variant A/B/C/D) in elke prompt waar `[GEKOZEN STIJL]` staat.
2. **Werk in volgorde:** eerst jongvolwassen referentie → daarna pup en eerste periode **mét het goedgekeurde referentiebeeld als reference image** (image-to-image). Zo erven de jongere versies kleur/markeringen/stijl.
3. Voor de jongere versies: geef naast het referentiebeeld ook **1–2 echte foto's** van die leeftijd mee (voor de juiste proporties).
4. Genereer alles **een paar keer**, kies de beste, en pas dan **style-lock** toe.
5. Sla op in `reference-material/character-sheets/` (klein/PNG; geen grote media in git).

> **Vaste beschrijving van Wolfje (overal gelijk houden):**
> cream/ivory long-haired toy dog (Pomeranian × Chihuahua mix), warm apricot/tan on head and ears with a light apricot saddle on the back, white chest/legs/paws, dark round friendly eyes, small black nose, short fine muzzle, large erect feathered ears, fluffy plume tail curling over the back, lion-like ruff (young-adult coat).

---

## 1. DEFINITIEF REFERENTIEBEELD — JONGVOLWASSEN WOLFJE

**1A · Hero-portret (gezicht + borst, voor identiteit/kleur):**
```
[GEKOZEN STIJL]
Character reference portrait of "Wolfje": cream/ivory long-haired toy dog (Pomeranian × Chihuahua mix), warm apricot/tan on head and ears, light apricot saddle on the back, white chest/legs/paws, dark round friendly eyes, small black nose, short fine muzzle, large erect feathered ears, lion-like ruff.
Front view, friendly happy expression, centered, plain soft pastel background, soft warm lighting.
Cute, colorful, family-friendly. No text, no watermark. Square 1:1.
```

**1B · Neutrale full-body referentie (voor bouw/proporties):**
```
[GEKOZEN STIJL]
Full-body character reference of "Wolfje" (same dog as the portrait): cream/ivory long-haired toy dog, warm apricot on head/ears, white chest/legs/paws, dark round eyes, black nose, large feathered ears, fluffy plume tail curling over the back, lion-like ruff.
Standing in a neutral 3/4 front pose, full body and all four legs clearly visible, calm friendly expression.
Plain light background, even lighting. Cute, colorful, family-friendly. No text, no watermark. Portrait 3:4.
```
> Kies hieruit je **definitieve referentiebeeld**. Dit is de "canon" waar alles op terugvalt.

---

## 2. PUP-VERSIE (image-to-image vanaf de jongvolwassen referentie)

```
[GEKOZEN STIJL]
Using the provided reference image of "Wolfje", draw the SAME dog as a younger PUPPY: same cream/ivory coat, same warm apricot on head and ears, same white chest/legs/paws, same dark eyes and black nose.
Puppy proportions: smaller and rounder body, bigger fluffy head relative to the body, shorter legs, ears fully erect but a touch smaller, fuller short fluffy coat with a white neck ruff (less long feathering than the adult).
Pose: sitting 3/4 front, full body, cute friendly expression. Plain soft pastel background.
Cute, colorful, family-friendly. No text, no watermark. Square 1:1.
```
*Reference image meegeven:* het goedgekeurde jongvolwassen-beeld **+ 1–2 echte pup-foto's** voor proporties.

---

## 3. EERSTE-PERIODE-VERSIE (jongste pup, image-to-image)

```
[GEKOZEN STIJL]
Using the provided reference image of "Wolfje", draw the SAME dog as a NEWBORN/youngest puppy: same cream/ivory coat, warm apricot tint on head and ears, white chest/paws, same dark eyes and tiny black nose.
Very young proportions: tiny round fluffy body that fits in a hand, very big round head relative to body, short stubby legs, small soft ears just beginning to stand, short downy fluff.
Pose: sitting/cuddled 3/4 front, full body, very cute innocent expression. Plain soft pastel background.
Cute, colorful, family-friendly. No text, no watermark. Square 1:1.
```
*Reference image meegeven:* het jongvolwassen-beeld **+ 1–2 echte eerste-dag-foto's**.

---

## 4. MODEL SHEET (per leeftijdsversie)

> Beeldmodellen maken zelden in één keer een perfecte turnaround. **Aanbevolen:** genereer de views **apart** met het referentiebeeld erbij, en zet ze daarna naast elkaar in één model sheet (compositing). Optioneel kun je ook de "all-in-one"-prompt proberen.

**4A · Aparte views (herhaal per versie: jongvolwassen / pup / eerste periode):**
```
[GEKOZEN STIJL]
Using the provided reference image of "Wolfje", same dog, same colors and style.
Generate a clean character turnaround view: {VIEW}.
{VIEW} = "front view" | "3/4 front view" | "side profile (full body)" | "back / 3-4 rear view (showing the plume tail)".
Neutral standing pose, full body, even lighting, plain light background. No text, no watermark. Square 1:1.
```

**4B · All-in-one model sheet (optioneel, kan minder consistent zijn):**
```
[GEKOZEN STIJL]
Character model sheet of "Wolfje" (use the reference image): the SAME dog shown in four poses side by side on one sheet — front view, 3/4 front, side profile, and rear view — all identical in color and proportions.
Neutral standing poses, full body, even lighting, plain background. No text, no watermark. Wide 16:9.
```

---

## 5. EXPRESSIE-SHEET (Wolfjes persoonlijkheid)

> Genereer elke uitdrukking apart met het referentiebeeld, daarna samenvoegen.

```
[GEKOZEN STIJL]
Using the reference image of "Wolfje" (same dog, same colors/style), head-and-shoulders, expression: {EXPRESSION}.
{EXPRESSION} =
 - "happy smiling, mouth open, tongue out"
 - "sleepy, eyes closed, curled up cozy"
 - "playful little grumble while biting a toy"
 - "barking with head up, mouth open — fox-like bark (WHOOOWHOOOWOO)"
 - "bougie / demanding, expectant look (wants to be fed)"
 - "surprised and curious, ears perked, big eyes"
Plain soft background, soft lighting. Cute, colorful, family-friendly. No text. Square 1:1.
```

---

## 6. NOG NODIG — BELLA

Voor de **formaatvergelijking Wolfje vs. Bella** en seizoen 2/3 hebben we ook Bella's vergrendelde ontwerp nodig. Dat is een **aparte stap** zodra je Bella-foto's aanlevert:
- Bella = Shih Tzu, beschrijving in Phase 1 (prikkelgevoelig, graver, beschermend).
- Zelfde route: referentiebeeld in de gekozen stijl → model sheet → style-lock.
- Daarna een gezamenlijke **size-comparison sheet** (Wolfje naast Bella) voor consistente verhoudingen.

---

## 7. WAT LEVER JE OP NA DEZE STAP (style-lock pakket)
- [ ] Definitief referentiebeeld jongvolwassen Wolfje (1A + 1B)
- [ ] Pup-versie + eerste-periode-versie (consistent)
- [ ] 3 model sheets (per leeftijd: front / 3-4 / side / rear)
- [ ] Expressie-sheet
- [ ] (later) Bella-referentie + size-comparison
- [ ] Korte **stijlbijbel** (kleurcodes, lijn/schaduw, "wel/niet"-voorbeelden) → `reference-material/style-bible.md`
- [ ] Jouw goedkeuring → **STYLE-LOCK** (vanaf hier verandert de stijl niet meer)
