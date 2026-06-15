# 🧠 WOLFJE & BELLA MEDIA AGENTIC — PHASE 3: SELF-LEARNING LOOP

**Version:** 1.0
**Date:** 5 June 2026
**Bouwt voort op:** Phase 1 (prompts) + Phase 2 (workflow) + Phase 5 (automatische metrics)
**Doel:** samen 1.000.000 views over TikTok + Instagram + YouTube binnen 21 dagen (3 seizoenen van 7 dagen)

> **📌 Vastgelegde keuzes (zie `phase-0-spec/project_specification.md`):** **elke view telt** (geen unieke gebruikers vereist) · publieksgerichte output in het **Engels** · de metrics die deze loop voeden komen uit de **automatische pijplijn van Phase 5** (geen handmatige invoer).

---

## 0. KERNIDEE (en een eerlijke waarschuwing vooraf)

De loop is simpel: **meet → analyseer → pas één ding aan → meet opnieuw.** De agent leert door elke dag de echte cijfers van de vorige post te lezen en daar de volgende keuzes op te baseren.

**Eerlijke nuance die de hele fase stuurt:**
- Je post **1×/dag per platform**. Echte gelijktijdige A/B-tests (twee versies naast elkaar) kunnen dus niet binnen één dag op één platform. Wat je wél hebt is **sequentieel testen over dagen** + **3 platforms als 3 parallelle datapunten**.
- **Kleine steekproeven zijn ruis.** Eén video die viraal gaat of flopt zegt weinig. De agent mag daarom **nooit hard bijsturen op één dag data** — pas na een trend van meerdere dagen (zie guardrails in §6).
- Leren gebeurt op **echte, geposte content**. De eerste 14 dagen upload jij handmatig, dus de loop draait op cijfers die jij (handmatig of via API) aanlevert.

---

## 1. WAT METEN WE (en waarom)

| Metric | Waarom het telt | Bron |
|--------|-----------------|------|
| Views | Hoofd-KPI (1M-doel) | per platform |
| Watch-through / kijktijd | Beste signaal voor het algoritme; bepaalt of je gepusht wordt | TikTok, YT Shorts |
| Likes | Lichte kwaliteitsindicator | alle |
| Comments | Sterk engagement-signaal (algoritme weegt dit zwaar) | alle |
| Shares / saves | Allersterkste signaal voor bereik | alle |
| Follows per video | Groeit het kanaal echt? | alle |
| **Engagement rate** | (likes+comments+shares) ÷ views — vergelijkbaar maken tussen video's | berekend |

> **Belangrijk:** views alleen zijn misleidend. **Kijktijd en shares** voorspellen toekomstig bereik beter. De agent optimaliseert primair op die twee, met views als einddoel.

---

## 2. HET FEEDBACKMECHANISME (concreet)

De cijfers van gisteren zitten al in **Node 3** van de workflow. Die worden in **Prompt 3 (optimalisatie)** en **Prompt 4 (reflectie)** als context meegegeven. Phase 3 voegt dáár een expliciet **"LEERSIGNAAL"-blok** aan toe:

```
LEERSIGNAAL (laatste 1–3 dagen):
- Best presterende video: {titel} — {views}, {watch_through}%, {shares} shares
- Slechtst presterende: {titel} — {views}
- Sterkste platform tot nu toe: {platform}
- Trend posttijd: {tijd} levert consistent meer kijktijd
- Trend contenttype: {type} scoort boven gemiddeld
AANBEVELING VOOR VANDAAG (max 3 punten):
- {door agent ingevuld na analyse}
```

Dit blok wordt door een aparte **analyse-call** (Claude, `claude-sonnet-4-6`) gegenereerd vóór Prompt 3, op basis van de DB. Eén extra goedkope call per dag.

---

## 3. TESTSTRATEGIE — wat je realistisch kunt testen

**Regel: test één variabele tegelijk.** Verander je alles tegelijk, dan weet je nooit wát het verschil maakte.

| Variabele | Hoe testen | Cadans |
|-----------|------------|--------|
| **Posttijd** | 3 platforms = 3 tijdsloten per dag → snelste signaal | dagelijks, per platform |
| **Videolengte** (15/30/45s) | Rouleer per dag; vergelijk kijktijd-% (niet absolute views) | over ±6 dagen |
| **Titelstijl** (vraag vs. statement vs. "eerste keer") | Eén stijl per dag, rouleren | over ±6 dagen |
| **Hook-type** (geluid "WHOOOWHOOOWOO" vs. actie vs. schattig stilstaand) | Rouleren, taggen | over ±6 dagen |
| **Thumbnail/eerste frame** | 2 opties genereren, jij kiest; achteraf koppelen aan resultaat | doorlopend |

> Sequentieel testen betekent: pas concluderen als een variant **meerdere keren** beter scoort, niet na één meevaller.

---

## 4. CONTENT-TAGGING (de motor onder het leren)

Zonder labels kan de agent niets vergelijken. Elke post krijgt bij opslag (Node 13) **tags** mee:

```json
{
  "content_id": "dag7_seizoen1",
  "tags": {
    "content_type": "eerste_keer | avontuur | bonding | klunzig_grappig | rustmoment",
    "main_character": "wolfje | bella | beiden",
    "hook_type": "geluid | actie | schattig_stil",
    "video_length": 30,
    "title_style": "vraag | statement | eerste_keer",
    "posting_time": { "tiktok": "19:30", "instagram": "18:00", "youtube": "12:00" },
    "educational_topic": "socialisatie | lichaamstaal | prikkelgevoeligheid | ..."
  }
}
```

Na een paar dagen kan de agent zeggen: *"bonding-video's met Bella scoren 30% meer shares dan avontuur-video's"* — en dáár stuurt hij op.

---

## 5. ADAPTATIEREGELS (expliciet, met drempels)

De agent mag alleen bijsturen als een patroon **stabiel** is. Voorbeeldregels:

```
ALS een posttijd op één platform 3 dagen op rij de hoogste kijktijd geeft
   → maak dat de standaardtijd voor dat platform (blijf 1 alternatief testen).

ALS een contenttype over ≥4 datapunten >20% boven de mediaan zit op shares
   → verhoog het aandeel van dat type in de verhaalplanning (max 60%, zie guardrail).

ALS een videolengte over ≥4 datapunten de laagste watch-through heeft
   → schrap die lengte uit de rotatie.

ALS een titelstijl consistent meer comments trekt
   → maak het de default, rouleer de andere als test.

ALS engagement rate 2 dagen op rij daalt ondanks stabiele views
   → de agent flagt dit in de reflectie en stelt een koerswijziging voor (niet automatisch doorvoeren).
```

> Drempels (3 dagen / 4 datapunten / 20%) zijn bewust gekozen om **niet op ruis te reageren**. Pas ze gerust aan als je meer data hebt.

---

## 6. GUARDRAILS — leren mag de serie niet kapot maken

Dit is het belangrijkste deel. Een view-maximaliserende agent kan ontsporen. Daarom harde grenzen:

1. **Kwaliteit boven views.** Geen clickbait, geen misleidende titels, geen rage-bait. Familievriendelijk blijft de bovengrens, altijd.
2. **Geen monocultuur.** Eén type mag max ~60% van de content worden, ook al scoort het — anders wordt de serie eentonig en haakt je publiek af.
3. **Educatieve waarde blijft verplicht**, ook als "puur schattig zonder uitleg" toevallig beter scoort. De educatie ís je merk.
4. **Geen overfitting op één viral hit.** Eén uitschieter verandert de strategie niet.
5. **Verhaalcontinuïteit gaat vóór optimalisatie.** De seizoensboog (eerste keren → bonding) wordt niet opgeofferd voor een trending format.
6. **Mens in de loop.** De eerste 14 dagen voert de agent niets automatisch door op social — hij *stelt voor*, jij beslist.

---

## 7. COLD START (dag 1–3, nog geen data)

- **Dag 1:** geen historie → start met algemeen onderbouwde defaults (TikTok ±19:00, IG ±18:00, YT ±12:00; lengte 20–30s; "eerste keer"-titel). De agent zegt eerlijk in de reflectie: *"nog geen data, dit zijn startaannames."*
- **Dag 2–3:** eerste cijfers binnen, maar te weinig om op te sturen → de agent **verzamelt en observeert**, doet voorzichtige micro-aanpassingen, en zegt expliciet dat conclusies nog onbetrouwbaar zijn.
- **Vanaf dag 4:** genoeg datapunten om de regels uit §5 te laten meedoen.

---

## 8. EXTRA ZELFVERBETERPUNTEN (zoals gevraagd)

Aanvullend op metrics/A-B/feedback laat de agent zichzelf groeien via:

1. **Comment-mining:** lees de top-comments en haal er terugkerende thema's/vragen uit ("welk ras is Wolfje?") → voed nieuwe educatieve hoeken én pinned-comment-antwoorden.
2. **Hook-retentie-analyse:** kijk specifiek naar de kijktijd in de **eerste 3 seconden**. Daar valt het meeste bereik te winnen of te verliezen.
3. **Cross-platform transfer:** wat op TikTok werkt, sneller uitproberen op Shorts (vergelijkbaar algoritme) vóór Instagram.
4. **"Waarom werkte dit?"-logboek:** bij elke uitschieter (boven of onder) schrijft de agent 2 zinnen hypothese → na een week terugkijken of de hypothesen klopten. Zo leert de agent over zijn eigen aannames.
5. **Verzadigingsdetectie:** als een format daalt na herhaald succes, signaleer "publiek is het zat" en stel iets nieuws voor.
6. **Trend-scan (optioneel):** check wekelijks trending audio/hooks in de honden-niche en toets of er een past binnen de toon — nooit een trend forceren die niet bij Wolfje & Bella past.

---

## 9. PACING NAAR 1M VIEWS

21 dagen, samen 1M views = gemiddeld **~47.600 views/dag** over drie platforms. Maar groei is zelden lineair — verwacht een langzame start en (hopelijk) versnelling.

**Eenvoudige pacing-check die de agent dagelijks meldt:**
```
Cumulatief tot nu toe: {som_views}
Verwacht op dit punt (lineair): {dag × 47.600}
Status: {voor / op schema / achter}
Benodigd gemiddelde resterende dagen: {(1.000.000 − som) ÷ resterende_dagen}
```

> Dit is een **kompas, geen garantie.** 1M in 21 dagen vanaf nul is ambitieus; het hangt sterk af van of één video doorbreekt. De agent rapporteert eerlijk of het doel realistisch in zicht is, en zegt het ook als het dat niet is.

---

## 10. DATA-SCHEMA VOOR DE LEER-STORE

```sql
-- tabel: daily_metrics (gevuld door de aparte metrics-workflow)
content_id        TEXT
content_date      DATE
platform          TEXT          -- tiktok | instagram | youtube
views             INT
watch_through_pct FLOAT
likes             INT
comments          INT
shares            INT
follows           INT
engagement_rate   FLOAT

-- tabel: content_tags (gevuld bij goedkeuring, Node 13)
content_id        TEXT
content_type      TEXT
main_character    TEXT
hook_type         TEXT
video_length      INT
title_style       TEXT
educational_topic TEXT

-- tabel: learning_log (de "waarom werkte dit"-hypothesen)
content_id        TEXT
observation       TEXT
hypothesis        TEXT
verified_after_7d BOOLEAN
```

De analyse-call joint `daily_metrics` × `content_tags` om de patronen uit §5 te vinden.

---

## 11. WEKELIJKSE / SEIZOENS-EVALUATIE

- **Eind elk seizoen (dag 7 / 14 / 21):** wat scoorde het best (type/tijd/lengte/titel)? Welke educatieve onderwerpen vielen aan? → input voor de planning van het volgende seizoen.
- **Eind dag 21:** is het 1M-doel gehaald of in zicht? Is er publieksvraag naar een vervolg (comments, follows, shares-trend)? → go/no-go-advies van de agent, met onderbouwing.

---

## 🔌 WAT PHASE 3 TOEVOEGT AAN DE WORKFLOW

1. **Eén extra analyse-call/dag** (Claude, goedkoop) die het LEERSIGNAAL-blok maakt vóór Prompt 3.
2. **Twee extra DB-tabellen** (`content_tags`, `learning_log`).
3. **Tagging-stap** bij goedkeuring (Node 13 uitgebreid).
4. **Pacing-regel** in de dagelijkse reflectie/goedkeuringsmelding.

Geen nieuwe externe tools nodig — alles draait op je bestaande Claude + Gemini + N8N.

---

## ✅ SAMENVATTING

De loop leert door **te taggen, te meten en pas op bewezen trends bij te sturen** — met harde guardrails die kwaliteit, educatie, verhaal en familievriendelijkheid boven views zetten. Hij is eerlijk over onzekerheid (cold start, ruis, haalbaarheid van 1M) en houdt jou de eerste 14 dagen aan het stuur.

**Volgende:** Phase 4 — Approval Dashboard (wat jij dagelijks ziet + beslist), als je daar klaar voor bent.
