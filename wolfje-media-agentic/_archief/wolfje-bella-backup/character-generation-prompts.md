# 📑 WOLFJE & BELLA MEDIA AGENTIC — PHASE 0: PROJECT SPECIFICATION

**Version:** 1.1
**Date:** 5 June 2026
**Rol:** Single source of truth. Alle andere fases (1, 2, 3, 4, 5) erven deze keuzes.

> **Wijziging v1.1:** structuur naar **3 seizoenen van 7 dagen (= 21 dagen)**; 1M-doel schuift mee naar **21 dagen**. Seizoenen zijn nu **leeftijdsfases** van Wolfje. Seizoen 1 = de **eerste periode** (jongste-pup-fase), niet letterlijk één dag.

---

## 1. Project in één zin
Een AI-gestuurde pijplijn die dagelijks een volledig getekend, educatief en schattig **stripverhaal + korte animatievideo** over Wolfje (en zus Bella) maakt, in het Engels, en optimaliseert voor TikTok, Instagram en YouTube Shorts — met als doel samen **1.000.000 views in 21 dagen** (3 seizoenen van 7 dagen).

---

## 2. Vastgestelde keuzes (beslissingenlog)

| # | Onderwerp | Beslissing |
|---|-----------|------------|
| 1 | **Taal** | Internationaal bereik. Invoer mag Nederlands; **alle publieksgerichte output (dialoog, titels, captions, hashtags, on-screen tekst) is Engels.** |
| 2 | **Beeldvorm** | **Volledig getekende animatie.** Echte hondenbeelden dienen alléén als AI-input/referentie en verschijnen nooit in de output. |
| 3 | **Accounts** | Alle accounts starten op **0 volgers**, nieuw aangemaakt speciaal voor Wolfje (TikTok, Instagram, YouTube). |
| 4 | **Referentiebeeld** | Komt uit de **echte foto's** (cartoon lijkt op de echte hond). **De maker keurt het definitieve ontwerp goed.** |
| 5 | **Tekenstijl** | Vertrekpunt: voorbeeldtekeningen van de nicht van de maker. Agent onderzoekt de beste methode en mag een eigen stijl voorstellen. **Na vaststelling: style-lock** — elke strip/short houdt exact dezelfde stijl tot de maker bewust iets anders goedkeurt. |
| 6 | **Video ↔ strip** | De dagelijkse video is **altijd gebaseerd op de strip van die dag**; de agent kiest zelf welk deel de short wordt (op basis van verwachte views / mooiste verhaal). |
| 7 | **Strip-distributie** | De agent bepaalt zelf het aantal pagina's per carrousel en mag in **meerdere carrousels** knippen — leidraad: zoveel mogelijk views. |
| 8 | **Bronmateriaal** | De maker stuurt **meerdere foto's/video's per episode**, zodat er genoeg materiaal is. Voldoende Bella-materiaal aanwezig. Materiaal wordt per **leeftijdsfase** (eerste periode / pup / jongvolwassen) gescheiden aangeleverd. |
| 9 | **Audio** | **Alleen rechtenvrije of platform-eigen** audio. Geen auteursrechtelijk beschermde/"trending" tracks (voorkomt Content-ID-claims). |
| 10 | **Dashboard** | N8N-koppeling is een voorbeeld, geen harde eis. De agent mag een betere dashboard-oplossing kiezen. |
| 11 | **Schema** | Tijdlijn aangepast aan de **optimale uploadtijd**: avond-generatie, upload de volgende dag op optimale tijden, metrics-pijplijn houdt data continu vers (zie Phase 5). |
| 12 | **Opslag** | Goedgekeurde bestanden worden opgeslagen in de **GitHub-map**, ook als bewijs voor het persoonlijke portfolio. |
| 13 | **Metrics** | **Volledig automatisch** ophalen/bijwerken/verwerken. YouTube + Instagram nu automatiseren; TikTok = **route A** (officiële API aanvragen) **+ route C** (vision-ingest als brug) tot toegang er is. Zie Phase 5. |
| 14 | **Doel, structuur & scope** | **3 seizoenen van 7 dagen = 21 dagen**; **1M views over 21 dagen** (elke view telt). Seizoenen = leeftijdsfases (zie §3). Echt kanaal, later monetiseren; de **eerste seizoenen onderbouwen het portfolio** (documentatie belangrijk). Vanaf dag 1 **geen auteursrechtproblemen**. |

---

## 3. Personages & seizoensstructuur

**Personages (volledig in Phase 1):**
- **Wolfje** — Chihuahua × Pomeriaan, bougie, blaft "WHOOOWHOOOWOO" — zijn blaf klinkt als die van een **vos**. **Vaste uiterlijk-referentie:** crème/ivoor lijf met **warme abrikoos op kop en oren** (en een lichte abrikoos "zadel" op de rug), **witte borst, poten en bef**, **donkere ronde ogen**, **zwart neusje**, korte fijne snuit, **pluimstaart die over de rug krult**.
- **Bella** — Shih Tzu, prikkelgevoelig (stress bij harde geluiden), graver, beschermend; rustiger in een rustige omgeving. Educatieve framing: prikkelgevoeligheid / omgevingsafhankelijk gedrag (niet "autisme").

> **Tuigje/riem:** geen vast kenmerk. Mag verschijnen bij **buitenverhalen/uitlaten** (situationeel), maar zit niet in het standaard personage-ontwerp.

**3 seizoenen = leeftijdsfases van Wolfje (elk 7 dagen):**

| Seizoen | Leeftijdsfase | Verhaal-focus | Voorbeelden van "eerste keren" / arc | Educatieve hoeken |
|---------|---------------|---------------|--------------------------------------|-------------------|
| **1** | **Eerste periode** (jongste pup) | Wolfje's allereerste tijd in zijn nieuwe huis | eerste keer vastgehouden, eerste nacht, eerste keer rondsnuffelen, eerste speeltje, eerste hapje | pup-ontwikkeling, wat een pasgeboren pup nodig heeft |
| **2** | **Pup** (groeiende pup) | De wereld ontdekken + kennismaken met grote zus Bella | eerste keer uitlaten, eerste keer aan de riem, eerste keer in het hondenzwembad, **eerste ontmoeting met Bella**, socialisatie | socialisatie, riemtraining, lichaamstaal |
| **3** | **Jongvolwassen** | Bonding met Bella: elkaar beschermen en geruststellen | hoe ze bonden, Bella geruststellen bij stress, samen avonturen | bonding-gedrag, omgaan met prikkelgevoeligheid, zelfvertrouwen |

> De **"eerste keren"** zijn verdeeld over de seizoenen op basis van bij welke leeftijd ze pasten; de **Bella-bondingboog** loopt van kennismaking (seizoen 2) naar diepe band (seizoen 3). De storytelling-agent mag de exacte volgorde fijnslijpen, zolang het logisch op het vorige verhaal aansluit.

**Drie vergrendelde leeftijdsversies — herkenbaar dezelfde hond, alleen leeftijd verschilt** (zelfde kleur/markeringen/ogen/neus):

| Versie | Kenmerkend t.o.v. de andere |
|--------|------------------------------|
| **Wolfje-Eerste-periode** | Heel klein, bolrond, donzig; grote fluffy kop t.o.v. lijfje; oortjes klein en net beginnend te staan; korte vacht |
| **Wolfje-Pup** | Groter, "hondvormiger"; oren duidelijk gegroeid, volledig rechtop en driehoekig met beige achterkant; vollere vacht met witte kraag; pluimstaart begint te krullen |
| **Wolfje-Jongvolwassen** | Volwassen proporties (slanke poten, langer lijf); **lange, gevederde vacht** (franjes aan oren/poten/borst/staart) en leeuwachtige kraag; volle pluimstaart over de rug; zelfverzekerde, "lachende" expressie |

> Materiaal wordt per leeftijdsfase **gescheiden** aangeleverd. Status referentiemateriaal: **eerste periode** ✅ (foto's + video's), **pup** ✅ (foto's + video's), **jongvolwassen** ✅ (foto's + video's). Audio/vocabulaire: signatuur **"WHOOOWHOOOWOO"** (klank niet machinaal geanalyseerd; nader te beschrijven door de maker indien gewenst).

---

## 4. Productieprincipes

- **Mens in de loop:** de eerste 14 dagen keurt de maker alles handmatig goed; niets gaat live zonder toestemming. Daarna evalueren of (deels) automatisch uploaden kan.
- **Self-learning met guardrails:** optimaliseren op kijktijd & shares; bijsturen alleen op bewezen trends; kwaliteit, educatie, verhaal en familievriendelijkheid gaan boven views.
- **Zuinig op tokens:** Sonnet 4.6 als default, Opus 4.8 alleen waar nodig; caching binnen de dagrun.

---

## 5. Tool-stack (samenvatting)

| Taak | Tool |
|------|------|
| Script, optimalisatie, reflectie, analyse | Claude (`claude-sonnet-4-6` / `claude-opus-4-8`) |
| Strippagina's renderen | Google beeldmodel (Gemini API) + referentiebeeld |
| Video | Veo (Gemini API), long-running |
| Tekstoverlay | N8N / code |
| Orchestratie, opslag, metrics | N8N + database; metrics-pijplijn per Phase 5 |

---

## 6. Documentenoverzicht

| Fase | Bestand | Inhoud |
|------|---------|--------|
| 0 | `phase-0-spec/project_specification.md` | Dit document — alle keuzes |
| 1 | `phase-1-prompts/..._phase1_prompts_v2.md` | Master prompts (v2.1) |
| 2 | `phase-2-workflow/..._phase2_workflow_v2.md` | N8N-workflow |
| 3 | `phase-3-learning/..._phase3_learning.md` | Self-learning loop |
| 4 | `phase-4-dashboard/wolfje_bella_dashboard.html` | Approval dashboard |
| 5 | `phase-5-metrics/..._phase5_metrics.md` | Automatische metrics-pijplijn |

---

## 7. Stappenplan Phase 0 — vóór dag 1

Volg de stappen in volgorde; de eerste vier blokkeren al het andere (zonder vastgestelde stijl kan er geen consistente content gemaakt worden). Vink af wat klaar is.

### Stap 0.1 — Beslis animatievorm & leeftijd *(blokkeert alles, neem hier rustig de tijd)*
- [ ] Onderzoek 2–3 **animatie-/tekenstijlen** binnen de leidende toon (zie hieronder). Stijlreferentie van de nicht: `reference-material/style-reference/`.
- [x] **Stijlbeslissing:** de **schattige, kleurrijke, familievriendelijke Cocomelon-toon is leidend** in het ontwerp. De gedetailleerde inktstijl van de nicht wordt **alleen als accent** ingezet wanneer de situatie daarom vraagt (bv. een dramatisch/spannend moment), nooit als basisstijl.
- [ ] Beslis: **groeit cartoon-Wolfje zichtbaar mee** (bv. puppy in seizoen 1, jongvolwassen in seizoen 2), of is er **één vaste canonieke leeftijd**? Leg dit expliciet vast — anders vermengt het model puppy- en volwassen-kenmerken.
- [ ] Kies de definitieve stijl + leeftijdsaanpak en **keur die zelf goed**.

### Stap 0.2 — Cureer de referentieset *(kwaliteit boven kwantiteit)*
- [ ] Stel een **gecureerde set** samen i.p.v. een ongesorteerde dump: meerdere hoeken, uitdrukkingen en lichtsituaties.
- [ ] Neem Wolfje's **signatuurmomenten** mee: bougie houding, speels grommen, de "whooowhooowoo"-bek, tegen jullie aan liggen.
- [ ] Doe hetzelfde voor **Bella** (incl. gestreste vs. ontspannen houding).
- [ ] Als Wolfje meegroeit: label het materiaal per **leeftijdsfase** (puppy / jongvolwassen), gescheiden gehouden.

### Stap 0.3 — Maak het character model sheet *(het artefact dat de look vergrendelt)*
- [ ] Wolfje van **voor / zij / achter**, een rij **gezichtsuitdrukkingen** en zijn **signatuurposes**.
- [ ] Een **formaatvergelijking** Wolfje vs. Bella (zodat verhoudingen consistent blijven).
- [ ] Idem model sheet voor Bella.

### Stap 0.4 — Leg de stijlbijbel vast (style-lock)
- [ ] Documenteer **kleurenpalet, lijndikte, schaduwstijl, achtergrondstijl**.
- [ ] Voeg een paar **"wel / niet"-voorbeelden** toe.
- [ ] Sla model sheet + stijlbijbel op als referentie waar **elke render** op terugvalt. **Vanaf hier: stijl vergrendeld.**

### Stap 0.5 — Merk & accounts
- [ ] Kies een **kanaalnaam/handle die op alle drie platforms vrij is** (Engels).
- [ ] Maak profielfoto (cartoon-Wolfje), **bio en banner** (Engels).
- [ ] Maak de accounts aan: **TikTok**, **Instagram (Business/Creator)**, **YouTube**.

### Stap 0.6 — Serie-outline
- [ ] Koppel de **7 afleveringen van seizoen 1** aan concrete "eerste keren".
- [ ] Schets seizoen 2 ruw (bonding-boog). De agent mag de volgorde fijnslijpen, maar de kapstok ligt vast.

### Stap 0.7 — Audio-kit
- [ ] Kies je **rechtenvrije / platform-eigen bronnen** (bv. YouTube Audio Library + platform-eigen geluiden).
- [ ] Leg een paar **vaste thema's per stemming** vast (schattig / avontuur / emotioneel), zodat dag 1 een goedgekeurde bron heeft.

### Stap 0.8 — Technische koppelingen
- [ ] **YouTube + Instagram** metrics-API's koppelen (Google OAuth / Meta-app).
- [ ] **TikTok API for Business aanvragen** (route A) + **vision-ingest** opzetten als brug (route C).
- [ ] **Avond-generatieschema** + **3×/dag metrics-runs** instellen.
- [ ] **GitHub-map** inrichten: `approved-content/` als opslag + portfolio-bewijs.

### Stap 0.9 — Golden-sample-test (pilot) *(vóór je je vastlegt op 21 dagen)*
- [ ] Genereer **één volledige aflevering** (strip + short) end-to-end met de vergrendelde stijl.
- [ ] Controleer: klopt de stijl, de Engelse output, de lengte, de audio, de hele pijplijn?
- [ ] Meet **hoeveel tijd en tokens** één dag echt kost.

### Stap 0.10 — Go / no-go
- [ ] Alles hierboven afgevinkt en de pilot goedgekeurd? → start dag 1.
- [ ] Iets niet rond (stijl twijfelachtig, API's nog niet klaar, te weinig materiaal)? → eerst oplossen.

> **Aanbevolen volgorde voor morgen:** eerst **0.1 → 0.4** (leeftijd/animatievorm + model sheet + style-lock, want dat blokkeert alles), dan de **golden-sample-test (0.9)** om de pijplijn én stijl te valideren, en pas daarna **accounts (0.5)** en **audio (0.7)**. De technische koppelingen (0.8) kun je parallel laten lopen.
