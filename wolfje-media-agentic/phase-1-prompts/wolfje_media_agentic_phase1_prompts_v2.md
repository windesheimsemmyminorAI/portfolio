# 🐕 WOLFJE & BELLA MEDIA AGENTIC — PHASE 1 (v2.1): MASTER PROMPTS

**Version:** 2.1 (decisions integrated)
**Date:** 5 June 2026
**Status:** GitHub-ready
**Bron van waarheid voor keuzes:** zie `phase-0-spec/project_specification.md`

> **Nieuw in v2.1 (vastgelegde keuzes):** publieksgerichte output in het **Engels** (input blijft Nederlands) · **volledig getekende animatie** (echte hondenbeelden alleen als AI-input, nooit in de output) · **referentiebeeld uit de echte foto's**, door de maker goedgekeurd · **één vaste tekenstijl die na vaststelling niet meer verandert** · **alleen rechtenvrije / platform-eigen audio**.

> **Wat is er gecorrigeerd t.o.v. v1?**
> 1. ❌ DALL-E geschrapt → vereiste een OpenAI-abonnement dat je niet hebt. Vervangen door **Google's beeldmodel** (via je bestaande Gemini-abonnement).
> 2. ✅ **Echte video toegevoegd** via **Veo** (Gemini API). v1 leverde alleen tekst op, geen videobestand.
> 3. ✅ **Rollen ontvlochten:** Claude schrijft het *script*; het beeldmodel *rendert* de pagina's; tekstballonnen worden als **overlay** toegevoegd (modellen renderen tekst-in-beeld onbetrouwbaar).
> 4. ✅ **Caching realistisch gemaakt:** cache vervalt na max 1 uur, dus géén besparing tussen dagen. Wel binnen één dagrun.
> 5. ✅ **Caveman-varianten** toegevoegd (zoals gevraagd) + correcte modelstrings.
> 6. ✅ Datums, taal en de "overloop"-vertaling gecorrigeerd.

---

## 📋 CONTENT REFERENCE BIBLE

**Wolfje (hoofdpersoon)**
- Ras: Chihuahua × Pomeriaan (dwergkeeshond) mix, 1 jaar oud
- Traits: bougie, wil gevoerd worden, ligt graag tegen z'n baasjes, gromt zachtjes bij spelen, bijt speels in vingers
- Signature geluid: **"WHOOOWHOOOWOO"** (klinkt als een echt klein wolfje)
- Persoonlijkheid: speels, veeleisend, aanhankelijk, dramatisch
- Season 1-arc: zijn eerste keren (eerste keer zien/vasthouden, eerste keer mee naar huis, eerste keer in z'n huisje, eerste keer uitlaten, eerste ontmoeting met grote zus Bella)

**Bella (bijrol)**
- Ras: Shih Tzu, woont niet bij ons maar is vaak op bezoek
- Traits: kleine stresskip, blaft bij elk geluid, hoge stembanden (doordringende blaf), echte buitenvrouw, graaft gaten in de tuin
- Stresstrigger: **harde geluiden** geven haar stress (bv. iemand die luid de overloop/trap op- en afloopt). Bij stress gaat ze zelfs op steen graven.
- Prikkelgevoelig & omgevingsafhankelijk: bij haar eigen baasjes is ze veel drukker; bij ons is ze juist rustiger. *(Educatieve framing: beschrijf dit als prikkelgevoeligheid / omgevingsafhankelijk gedrag — niet als "autisme", want dat is geen diagnose bij honden. Zo blijft de educatieve content kloppend.)*
- Persoonlijkheid: nerveus, avontuurlijk, beschermend, dramatisch; bloeit op in een rustige omgeving
- Season 2-arc: hoe Wolfje en Bella bonden, elkaar beschermen en geruststellen

**Vaste contentregels (geldt voor alles)**
- Educatief (hondengedrag, verzorging, pup-ontwikkeling) + schattig + grappig
- Familievriendelijk: geen geweld, geen zielig/triest einde
- Humor & storytelling met diepgang; lichte "drama-twist" mag bij een klunzig/grappig moment
- Toon: Cocomelon (schattig/herhalende hooks) + Kids Diana Show (avontuur/emotie) + MrBeast (datagedreven viral-mechaniek)
- Doelgroep: hondenliefhebbers wereldwijd, vooral vrouwen (±18–45)
- **Taal:** alle publieksgerichte tekst (dialoog in de strip, titels, captions, hashtags, on-screen tekst) in het **Engels** voor internationaal bereik. De invoer van de maker mag Nederlands zijn; de agent vertaalt/werkt uit naar Engels.
- **Volledig getekende animatie:** de echte foto's/video's van de honden dienen **alleen als input/referentie** voor de AI. Ze verschijnen **nooit** in de uiteindelijke strip of video — alles is getekende cartoon.
- **Audio:** uitsluitend **rechtenvrije of platform-eigen** muziek/SFX (geen auteursrechtelijk beschermde of "trending" tracks), om Content-ID-claims en monetisatieproblemen te voorkomen.

---

## 🧰 GECORRIGEERDE TOOL-STACK

| Taak | Tool | Modelstring / Endpoint | Waarom |
|------|------|------------------------|--------|
| Stripscript + dialoog | **Claude** | `claude-sonnet-4-6` (default) / `claude-opus-4-8` (premium kwaliteit) | Beste tekst/redenering; jij hebt Claude Pro |
| Optimalisatie + zelfreflectie | **Claude** | `claude-sonnet-4-6` | Goedkoper, snel genoeg voor deze taak |
| Strippagina's renderen | **Google beeldmodel** | Gemini-beeldmodel / Imagen via Gemini API | Zit bij je Gemini-abonnement (geen DALL-E nodig) |
| Animated short (echte video) | **Veo** | `veo-3.1-generate-preview` via Gemini API (`generateVideos`, long-running → pollen) | Enige route naar een écht videobestand |
| Tekstballonnen / captions in beeld | **Overlay in post** (N8N/code) | n.v.t. | Beeldmodellen renderen tekst onbetrouwbaar |

> **Default = Sonnet 4.6** om binnen je dagelijkse tokenlimiet te blijven. Wissel alleen naar Opus 4.8 voor het stripscript als je merkt dat de verhaalkwaliteit omhoog moet. Verifieer de exacte modelstrings bij gebruik op `https://docs.claude.com/en/docs/about-claude/models/overview`.

> **Belangrijke nuance over de strip:** een beeldmodel kan **niet** vanzelf 10–20 pagina's met dezelfde hond + leesbare tekstballonnen maken. Daarom:
> - **Karakterconsistentie:** maak één keer een **referentiebeeld** van Wolfje en van Bella, gebaseerd op de **echte foto's** (zodat de cartoon dicht bij de werkelijkheid blijft), en geef dat steeds als *reference image* mee (image-to-image), zodat ze er over alle pagina's hetzelfde uitzien.
> - **Tekst:** laat het beeldmodel de panelen *zonder* tekst renderen; plak dialoog/ballonnen er daarna als overlay overheen (stap in N8N/compositing).
>
> **Tekenstijl — eenmalig vaststellen, daarna vergrendelen:**
> - Vóór dag 1 onderzoekt de agent **welke tekenmethode/stijl het beste past** (vertrekpunt: de voorbeeldtekeningen van de nicht van de maker). De agent mag daarvan afwijken en een eigen vormgeving voorstellen.
> - De maker keurt het **definitieve referentiebeeld + de stijl** goed.
> - Daarna is de stijl **vergrendeld (style-lock):** elke strip en elke short gebruikt exact dezelfde tekenstijl. Wijzigen mag alleen via een bewuste nieuwe goedkeuring door de maker.
> - Leg de vastgestelde stijl vast als **stijl-bijlage** (referentiebeelden + korte stijlbeschrijving) zodat elke render erop terugvalt.

---

## 🎨 PROMPT 1 — STRIPSCRIPT (Claude)

> Output van deze prompt = **script + per-paneel beeldprompt + dialoog**. Dit is géén plaatje; het voedt Prompt 1B (rendering) en de overlay-stap.

### Caching-opzet (correct):
Zet het **statische deel** (rol + bible + regels + outputformaat) in het **`system`-veld** met `cache_control` (ttl `1h` als je dagrun >5 min duurt). Het **dynamische deel** (de foto-omschrijving van vandaag) gaat kort in het `user`-bericht → "caveman". Dit bespaart binnen één dagrun; **niet** tussen dagen (cache leeft max 1 uur).

### Volledige prompt (system-veld, gecached):
```
ROL: Stripscenarist voor schattige, educatieve hondenverhalen.

PERSONAGES (gebruik consistent):
- Wolfje: Chihuahua-Pomeriaan, 1jr, bougie, gromt/bijt speels, blaft "WHOOOWHOOOWOO".
- Bella: Shih Tzu, stresskip, hoge doordringende blaf, graaft, beschermend.
TOON: Cocomelon + Kids Diana + lichte humor/drama, nooit zielig. Familievriendelijk.

TAAK: Schrijf een stripscript van 10–20 pagina's o.b.v. de aangeleverde foto/video.

REGELS:
1. 10–20 pagina's, GEEN opvulling — elke pagina brengt het verhaal verder.
2. Pagina = 2–4 panelen.
3. Dialoog: max 2–3 ballonnen p/pagina, simpele taal, IN HET ENGELS.
4. Pagina 1, paneel 1 = hook (schattig of grappig).
5. Midden = verhaal + 1 educatief moment.
6. Laatste paneel = emotionele beat of "aha".

EERST (vóór de pagina's) geven:
- Verhaalboog: max 5 zinnen
- Educatief moment: 1 zin
- Aantal pagina's + waarom dit aantal

OUTPUTFORMAT per pagina:
[PAGINA n]
BEELDPROMPT: <1–2 zinnen, Engels, voor het beeldmodel — verwijst naar de VERGRENDELDE tekenstijl + referentiebeeld, GEEN tekst in beeld>
PANEEL 1: <actie> | DIALOOG (Engels): "<tekst of geen>"
PANEEL 2: <actie> | DIALOOG (Engels): "<tekst of geen>"
(PANEEL 3/4 indien nodig)

VISUELE STIJL (voor elke beeldprompt): de vastgestelde, vergrendelde tekenstijl; cute, kleurrijk, kindvriendelijk, warme achtergrond. NOOIT eng/triest. GEEN tekst renderen.
```

### Dynamisch user-bericht (caveman, niet gecached):
```
FOTO/VIDEO: {beschrijving van vandaag}
SEIZOEN: {1 of 2} | DAG: {1–15}
EDUCATIEVE HOEK: {uit lookup-tabel}
Schrijf het script nu.
```

---

## 🖼️ PROMPT 1B — STRIPPAGINA RENDEREN (Google beeldmodel)

> Eén call per pagina, met het **referentiebeeld** van het juiste personage erbij. De `BEELDPROMPT` uit Prompt 1 vul je hier in.

```
Render één stripscène, chibi cartoonstijl, warme kleuren, kindvriendelijk.
SCÈNE: {BEELDPROMPT uit Prompt 1}
CONSISTENTIE: gebruik het meegeleverde referentiebeeld zodat het personage er identiek uitziet.
GEEN tekst, GEEN letters, GEEN tekstballonnen in het beeld (die komen later als overlay).
Verticale compositie (9:16) met ruimte bovenin voor een ballon.
```
**Daarna (N8N/compositing-stap):** plaats de `DIALOOG`-teksten als ballon-overlay op de gerenderde panelen.

---

## 🎬 PROMPT 2 — ANIMATED SHORT (Claude-storyboard → Veo-video)

> **Stap A** (Claude, tekst): maak storyboard + Veo-prompts. **Stap B** (Veo): genereer het echte videobestand.

### Stap A — storyboard (Claude, `claude-sonnet-4-6`):
```
ROL: Korte-video regisseur (TikTok/Reels/Shorts), verticaal 9:16.

INPUT: stripscript hieronder.
{STRIP_SCRIPT}

BEPAAL VIDEOLENGTE (15/30/45s) en motiveer:
- Simpel 2-scènes → 15s | meerdere scènes → 30–45s
- Sterke hook → mag langer; zwak → kort houden
- TikTok favoriet <30s; YouTube beloont langere kijktijd

STRUCTUUR:
0–2s hook (Wolfje's "WHOOOWHOOOWOO" of Bella in paniek)
2–5s setup → 5–18s verloop (humor/emotie) → climax → resolutie (punchline/emotie)

AUDIO: geen voice-over; kies muziek (whimsical / actie-anime / zachte piano / trending) + SFX (echte blaf, pootjes, comedy-SFX).

OUTPUT:
- Aanbevolen lengte + reden (1 zin)
- Per scène: tijdcode | beeld | audio | actie
- TEKST-OVERLAY: welke tekst, wanneer
- VEO-PROMPTS: 3–6 prompts (1 per shot) voor videogeneratie, elk: onderwerp, camera, beweging, sfeer, 9:16
```

### Stap B — Veo-call (per shot):
```
{VEO-PROMPT uit stap A}
Stijl: schattige cartoon, 9:16 verticaal, vloeiende beweging, warme kleuren.
```
> Veo draait als **long-running operation**: starten → status pollen tot `done` → videobestand downloaden. (Plan ~tientallen seconden per shot.)

---

## 🎯 PROMPT 3 — OPTIMALISATIE (Claude)

```
ROL: Viral-contentstrateeg voor hondenliefhebbers (vrouwen 18–45).
TAAK: titels, captions, hashtags en posttijden per platform.

CONTENT:
Strip: {STRIP_SAMENVATTING}
Video: {VIDEO_SAMENVATTING}

DATA VAN GISTEREN:
{METRICS}  (bv. TikTok 45K views/3.2K likes | IG 12K | YT 8K)
BESTE POSTTIJDEN: {POSTTIJDEN}

REGELS:
- 3 titels p/platform, 10–15 woorden, hook via nieuwsgierigheid/emotie/"eerste keer". Familievriendelijk, geen clickbait.
- Captions: TikTok ≤280 tekens (+1–2 hashtags); IG = verhaal + educatie + 15–20 hashtags; YT = volledige beschrijving + 20–30 hashtags.
- Hashtag-mix: 30% breed / 40% niche / 30% trending.
- Posttijd: binnen 2u van berekend optimum, nooit exact hetzelfde tijdstip elke dag.
- Engagement-hook + teaser voor de volgende aflevering.

OUTPUT per platform: 3 titels | caption | hashtags | posttijd. Plus: engagement-hook + teaser.
Sluit af met 3 korte redenen (titel/posttijd/hashtags) voor de zelfreflectie.
```

---

## 🧠 PROMPT 4 — ZELFREFLECTIE (Claude, max 5 zinnen)

```
ROL: AI-agent die z'n eigen keuzes onderbouwt.
INPUT: {GENOMEN_KEUZES} + {DATA_VAN_GISTEREN}

Geef EXACT 5 zinnen, één per punt:
1. Creatieve keuze + hoe het de seizoensboog dient.
2. Videolengte + posttijd, onderbouwd met data.
3. Welke titel/hook waarschijnlijk het best presteert + waarom.
4. Wat verbeterde t.o.v. gisteren + wat is aangepast.
5. Risico/zorg (bv. strip <8 pagina's) + wat te monitoren.

TOON: zakelijk, beknopt, datagedreven, bescheiden over voorspellingen.
```

---

## 🔄 CACHING — CORRECT TOEGEPAST

| Wat | Cachen? | Hoe |
|-----|---------|-----|
| Bible + regels + outputformat | ✅ Ja | In `system`-veld met `cache_control`; gebruik `ttl: "1h"` als de dagrun >5 min duurt |
| Foto-omschrijving van vandaag | ❌ Nee | Kort in `user`-bericht (caveman) |
| Tussen verschillende dagen | ❌ Onmogelijk | Cache leeft **max 1 uur** → de volgende dagrun is altijd een cache-miss |

**Realistische besparing:** binnen één dagrun delen Prompt 1, 3 en 4 dezelfde gecachte bible-prefix → cache-reads kosten ~10% van de inputprijs. Tussen dagen: geen winst. Minimale cachebare lengte is ±1024 tokens; korter wordt niet gecached. *(Geverifieerd via Anthropic docs, juni 2026.)*

---

## 🧩 INTEGRATIE-FLOW (SEQUENTIEEL — niet parallel)

```
Foto/video van gebruiker
   ↓
PROMPT 1  (Claude)      → stripscript + beeldprompts + dialoog
   ↓
PROMPT 1B (beeldmodel)  → gerenderde panelen  → overlay-stap zet dialoog erop
   ↓
PROMPT 2A (Claude)      → storyboard + Veo-prompts
PROMPT 2B (Veo)         → echt videobestand (pollen tot klaar)
   ↓
PROMPT 3  (Claude)      → titels/captions/hashtags/posttijden  (gebruikt 1+2)
   ↓
PROMPT 4  (Claude)      → zelfreflectie (5 zinnen)
   ↓
Naar jou ter goedkeuring → handmatige upload (eerste 14 dagen)
   ↓
Metrics ophalen → voeden Prompt 3 van de volgende dag
```
> Prompt 2 heeft 1 nodig, Prompt 3 heeft 1+2 nodig → ze kunnen dus **niet parallel** draaien.

---

## ✅ QUALITY GATES
1. Strip <8 pagina's → bericht naar jou: "stuur meer foto's/video's".
2. Vast outputformaat per prompt → minder hallucinaties.
3. Zelfreflectie max 5 zinnen → geen geleuter.
4. Referentiebeeld verplicht → karakterconsistentie.
5. Geen tekst-in-beeld → tekst altijd via overlay (leesbaar).

---

**Volgende:** Phase 2 v2 (N8N-workflow met echte render-/Veo-nodes, juiste auth & syntax).
