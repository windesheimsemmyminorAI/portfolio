# 🐺 Wolfje &amp; Bella — Media Agentic

> Een AI-gestuurde contentpijplijn die dagelijks een educatief, schattig **volledig getekend** stripverhaal én een korte animatievideo genereert over het leven van twee hondjes — Wolfje en zijn grote zus Bella — en die optimaliseert voor TikTok, Instagram en YouTube Shorts.

**Doel:** samen **1.000.000 views** over de drie platforms binnen **21 dagen** (drie "seizoenen" van 7 dagen: eerste periode → pup → jongvolwassen). Elke view telt.
**Taal:** invoer Nederlands, **publieksgerichte output Engels** (internationaal bereik).
**Beeld:** volledig getekende animatie — echte hondenbeelden zijn alleen AI-input, nooit output.
**Stack:** Claude · Gemini (incl. Veo) · N8N — geen extra abonnementen nodig.
**Mens in de loop:** de eerste 14 dagen keurt de maker alles handmatig goed; niets gaat live zonder toestemming.
**Scope:** echt kanaal (later monetiseren); de eerste 2 seizoenen onderbouwen het portfolio. Vanaf dag 1 geen auteursrechtproblemen (alleen rechtenvrije/platform-eigen audio).

> 👉 **Alle vastgestelde keuzes staan in `phase-0-spec/project_specification.md` (single source of truth).**

---

## 📖 Het concept

| | |
|---|---|
| **Hoofdpersoon** | **Wolfje** — Chihuahua × Pomeriaan, 1 jaar, bougie, blaft "WHOOOWHOOOWOO" |
| **Bijrol** | **Bella** — Shih Tzu, prikkelgevoelig, gravend, beschermend; rustiger in een rustige omgeving |
| **Toon** | Cocomelon (schattig) + Kids Diana Show (avontuur/emotie) + MrBeast (datagedreven viral-mechaniek) |
| **Doelgroep** | Hondenliefhebbers, vooral vrouwen (±18–45) |
| **Seizoen 1** | Wolfje's "eerste keren" (eerste keer vasthouden, eerste keer thuis, eerste keer uitlaten, eerste ontmoeting met Bella…) |
| **Seizoen 2** | Hoe Wolfje en Bella bonden, elkaar beschermen en geruststellen |
| **Kaders** | Altijd educatief, schattig, grappig én familievriendelijk |

---

## 🧱 De fases

### Phase 0 — Project Specification
De single source of truth: alle vastgestelde keuzes (taal, animatie, accounts, stijl-lock, audio, schema, metrics, scope) in één beslissingenlog.
📄 `phase-0-spec/project_specification.md`

### Phase 1 — Master Prompts
De vier herbruikbare prompts die de pijplijn aansturen:
1. **Stripscript** (Claude) → script + per-paneel beeldprompts + dialoog (Engels)
2. **Animated short** (Claude-storyboard → Veo-video)
3. **Optimalisatie** (Claude) → titels, captions, hashtags, posttijden per platform (Engels)
4. **Zelfreflectie** (Claude) → onderbouwing in max 5 zinnen

Inclusief karakter-bible, stijl-lock, caveman-varianten en een correcte caching-opzet.
📄 `phase-1-prompts/wolfje_media_agentic_phase1_prompts_v2.md`

### Phase 2 — N8N Workflow
De dagelijkse orchestratie in nodes: input → metrics ophalen → script → strip renderen → tekstoverlay → storyboard → video (Veo) → optimalisatie → reflectie → bundelen → goedkeuring → opslaan. Met een aparte workflow die 1×/dag de metrics ophaalt.
📄 `phase-2-workflow/wolfje_media_agentic_phase2_workflow_v2.md`

### Phase 3 — Self-Learning Loop
Hoe de agent leert: elke post wordt getagd, echte cijfers worden dagelijks geanalyseerd, en bijsturen mag alleen op een **bewezen trend** (niet op ruis). Optimaliseert op kijktijd en shares, met harde guardrails die kwaliteit, educatie en verhaal boven views zetten.
📄 `phase-3-learning/wolfje_media_agentic_phase3_learning.md`

### Phase 4 — Approval Dashboard
Een zelfstandig, interactief dashboard (één HTML-bestand) waarin de maker dagelijks de content beoordeelt, de 1M-pacing volgt, metrics bekijkt en goedkeurt/afkeurt. Werkt offline; grafieken zijn in SVG getekend.
📄 `phase-4-dashboard/wolfje_bella_dashboard.html`

### Phase 5 — Automated Metrics Pipeline
Een ontkoppelde pijplijn die metrics **automatisch** ophaalt, bijwerkt en verwerkt tot KPI's, trends en een kant-en-klaar leersignaal. YouTube + Instagram volledig automatisch; TikTok via route A (officiële API aangevraagd) + route C (vision-ingest) als brug. Bevat het herontworpen avond-schema.
📄 `phase-5-metrics/wolfje_media_agentic_phase5_metrics.md`

---

## 🔧 Tool-stack

| Taak | Tool | Model / Endpoint |
|------|------|------------------|
| Script, optimalisatie, reflectie, analyse | Claude | `claude-sonnet-4-6` (default) · `claude-opus-4-8` (premium) |
| Strippagina's renderen | Google beeldmodel (Gemini API) | image-model · met referentiebeeld voor consistentie |
| Video genereren | Veo (Gemini API) | `veo-3.1-generate-preview` (long-running → pollen) |
| Tekstballonnen / overlay | N8N / code | beeldcompositie ná rendering |
| Orchestratie & opslag | N8N Pro | workflows + database |

> Modelnamen wijzigen snel — verifieer ze bij het bouwen in de officiële docs van Anthropic en Google.

---

## 🔄 Dagelijkse flow

```
's Avonds: foto's/video's van de maker (input, NL)
   ↓
Stripscript (Claude, EN) → panelen renderen (beeldmodel + vaste stijl) → dialoog-overlay
   ↓
Storyboard (Claude) → video (Veo)  — agent kiest welk stripdeel de short wordt
   ↓
Optimalisatie (Claude, EN) → zelfreflectie (Claude)
   ↓
Dashboard → maker keurt goed → opslaan in GitHub-map
   ↓
Volgende dag: handmatige upload op optimale tijden (eerste 14 dagen)
   ↓
Automatische metrics-pijplijn (Phase 5) → voedt continu de volgende generatie
```

---

## 🛡️ Guardrails

- Kwaliteit, educatie en verhaalcontinuïteit gaan **boven** views.
- Geen clickbait of rage-bait; altijd familievriendelijk.
- Eén contenttype wordt nooit meer dan ±60% van de output (geen monocultuur).
- Niet bijsturen op één virale hit of flop — alleen op stabiele trends.
- De eerste 14 dagen: mens in de loop, niets live zonder toestemming.

---

## 📁 Projectstructuur

```
wolfje-media-agentic/
├── README.md
├── phase-0-spec/
│   ├── project_specification.md          ← single source of truth
│   └── characters/wolfje/                ← canon, input-photos, model-sheets,
│       └── …                                prompts, renders, logs
├── phase-1-prompts/   wolfje_media_agentic_phase1_prompts_v2.md
├── phase-2-workflow/  wolfje_media_agentic_phase2_workflow_v2.md
├── phase-3-learning/  wolfje_media_agentic_phase3_learning.md
├── phase-4-dashboard/ wolfje_bella_dashboard.html
├── phase-5-metrics/   wolfje_media_agentic_phase5_metrics.md
├── reference-material/                   ← stijl-referenties + style-results
├── docs/
│   └── wolfje-eindterm-verslag-prompt.md ← systeem-prompt eindtermverslag
├── approved-content/                     ← goedgekeurde strips/video's (portfolio-bewijs)
│   └── season-1/
│       └── episode-01-the-lookout/       ← strip-HTML, video's, panels/ + README
└── _archief/                             ← oude iteraties/duplicaten (historie, niet actief)
```

> **Episode 1 — "The Lookout"** is de eerste uitgewerkte aflevering: de afgemaakte
> strip (HTML), twee video's en de bronpanelen staan in
> `approved-content/season-1/episode-01-the-lookout/`, met een eigen README die de
> verhaalvolgorde en de gekozen panelen documenteert.

---

## ⚠️ Eerlijke kanttekeningen

- **1M views in 21 dagen vanaf nul is ambitieus** en hangt sterk af van of één video doorbreekt. Het dashboard rapporteert eerlijk of het doel in zicht is — ook als dat niet zo is.
- **"A/B-testen" is bij 1 post/dag in de praktijk sequentieel testen** over dagen, plus 3 platforms als 3 datapunten. Geen gelijktijdige varianten op één platform.
- **Metrics: YouTube + Instagram zijn volledig te automatiseren**; TikTok-analytics vereist goedgekeurde API-toegang (aangevraagd, route A) met een vision-ingest als tijdelijke brug (route C).
- **Beeldmodellen renderen tekst-in-beeld onbetrouwbaar** → dialoog wordt als overlay toegevoegd, en een referentiebeeld zorgt voor karakterconsistentie.
- **Tekenstijl wordt eenmalig vastgesteld en daarna vergrendeld** zodat alle content dezelfde look houdt.

---

## 📌 Status

Alle fases (0–5) zijn uitgewerkt, op fouten gecontroleerd en met de vastgestelde keuzes geïntegreerd. Het canon-referentiebeeld en de cel-shaded tekenstijl zijn vergrendeld, en de eerste aflevering — **Episode 1 "The Lookout"** — is geproduceerd (strip + video's, zie `approved-content/season-1/episode-01-the-lookout/`). Volgende stap: accounts aanmaken, API's koppelen en de pijplijn testen met nieuwe afleveringen.

> **Versiebeheer / project-hygiëne (07-06-2026):** een audit van Phase 0 wees uit dat het beslisproces volledig is gedocumenteerd, maar dat niet alle afgewezen beelden als bestand zijn bewaard. Zie `phase-0-spec/ONTBREKENDE-BEELDEN-phase-0.md` (known gaps + reflectie), de bijbehorende GitHub-issues #1–#4, en `phase-0-spec/characters/wolfje/logs/CHANGELOG.md` (Sessie J/K) voor de volledige analyse en leerpunten.

---

*Project voor de minor AI — Windesheim.*
