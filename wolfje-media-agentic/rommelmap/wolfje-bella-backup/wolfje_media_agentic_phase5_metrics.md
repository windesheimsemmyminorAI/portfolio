# 📡 WOLFJE & BELLA MEDIA AGENTIC — PHASE 5: AUTOMATED METRICS PIPELINE

**Version:** 1.0
**Date:** 5 June 2026
**Bouwt voort op:** Phase 2 v2 (workflow) + Phase 3 (learning loop) + Phase 4 (dashboard)
**Doel:** metrics worden **automatisch opgehaald, bijgewerkt en verwerkt** — geen handmatig typen.

---

## 0. PRINCIPE

Eén losstaande, doorlopende **metrics-pijplijn** die per platform de cijfers ophaalt, normaliseert, opslaat, verwerkt tot KPI's/trends en automatisch het LEERSIGNAAL voor de contentgeneratie én het dashboard voedt. De contentgeneratie hoeft niet te wachten op metrics — beide draaien ontkoppeld.

```
[Scheduler] → per platform ophalen → normaliseren → opslaan (DB)
            → verwerken (KPI's, trends, LEERSIGNAAL) → dashboard + volgende generatie
```

---

## 1. EERLIJKE REALITEIT PER PLATFORM

Volledig hands-off automatiseren is **direct mogelijk voor YouTube en Instagram**. TikTok is de bottleneck.

| Platform | Officiële API voor eigen analytics | Wat je krijgt | Setup | Kosten | Frictie |
|----------|-----------------------------------|---------------|-------|--------|---------|
| **YouTube** | Data API v3 + Analytics API | views, likes, comments, kijktijd, retentie | Google OAuth (1×) | gratis (quota) | **laag** ✅ |
| **Instagram** | Graph API (media insights) | reach, views, likes, comments, shares, saves | Business/Creator-account + Facebook-pagina + Meta-app | gratis | **middel** 🟠 |
| **TikTok** | API for Business / Research API | views, engagement, audience, video-level | app registreren + **goedkeuring aanvragen** (eligibility) | gratis, maar traag | **hoog** 🔴 |

> De TikTok **Display API** (`/v2/video/list`, `/v2/video/query`) geeft alleen videometadata, **geen analytics**. Voor echte cijfers heb je de Business-/Research-API nodig, en die toegang duurt. Verifieer scopes/endpoints altijd in de actuele docs — ze wijzigen vaak.

---

## 2. TIKTOK — DRIE ROUTES (jij kiest)

Omdat TikTok niet meteen automatisch kan, drie eerlijke opties:

**Route A — Officiële TikTok API for Business (gratis, traag)**
Vraag nu toegang aan; bouw de node alvast. Tot goedkeuring blijft TikTok leeg of gebruik je tijdelijk route C. *Voordeel:* gratis, officieel. *Nadeel:* goedkeuring kan weken duren en is niet gegarandeerd voor een nieuw account.

**Route B — Externe unified API (betaald, direct)**
Een dienst als Phyllo/Pentos wrapt TikTok-analytics en levert het via één API. *Voordeel:* direct automatisch, ook YouTube/Instagram in één klap. *Nadeel:* extra abonnement (±$25+/maand) — buiten je huidige stack.

**Route C — Vision-ingest als tijdelijke brug (bijna gratis, semi-automatisch)**
Je dropt de TikTok-analytics-screenshot in een vaste map (bv. de GitHub-map of Drive); een N8N-stap stuurt die naar een vision-model dat de getallen uitleest en in de DB schrijft. *Voordeel:* verwerking blijft automatisch, geen API-goedkeuring nodig. *Nadeel:* je maakt zelf nog 1 screenshot per dag (niet 100% hands-off).

> **Aanbeveling:** YouTube + Instagram nu volledig automatiseren (route voor TikTok = A aanvragen + C als brug). Zodra TikTok-toegang er is, schakel je C uit. Wil je vanaf dag 1 echt nul handelingen, dan is route B de enige garantie — maar dat is een betaalde dependency.

---

## 3. ARCHITECTUUR — DE METRICS-PIJPLIJN (aparte N8N-workflow)

```
NODE M1  Scheduler (meerdere keren/dag — zie §5)
NODE M2  Haal te-meten posts op uit DB (approved_content waar status=posted)
   ↓ (per platform, parallel mag hier WEL — onafhankelijke bronnen)
NODE M3a YouTube: Data API + Analytics API   (OAuth)
NODE M3b Instagram: Graph API media insights (Meta-app token)
NODE M3c TikTok: Business API  | of vision-ingest (route C)
   ↓
NODE M4  Normaliseren → uniform schema (zelfde veldnamen per platform)
NODE M5  Opslaan/upserten in daily_metrics (idempotent: zelfde post = update, geen duplicaat)
NODE M6  Verwerken: engagement rate, deltas, rolling trends, content-type-performance
NODE M7  LEERSIGNAAL genereren (Claude, goedkoop) → opslaan
NODE M8  Dashboard verversen (push naar data-bestand/endpoint dat het dashboard leest)
```

---

## 4. NODE-DETAILS (kern)

**M3a — YouTube**
```
GET https://www.googleapis.com/youtube/v3/videos?part=statistics&id={videoId}
GET https://youtubeanalytics.googleapis.com/v2/reports?metrics=views,estimatedMinutesWatched,averageViewPercentage&ids=channel==MINE&...
Auth: OAuth2 (refresh token in $env). Gratis binnen dagquota.
```

**M3b — Instagram**
```
GET https://graph.facebook.com/v21.0/{ig-media-id}/insights?metric=reach,views,likes,comments,shares,saved
Auth: long-lived token van de Meta-app (Business/Creator-account gekoppeld aan FB-pagina).
```

**M3c — TikTok (route A)**
```
TikTok API for Business → video analytics endpoint (na goedkeuring).
Tot dan: route C → vision-stap die screenshot uitleest.
```

**M4 — Normaliseren (Code-node, uniform schema)**
```js
return items.map(p => ({ json: {
  content_id: p.content_id,
  platform: p.platform,            // youtube | instagram | tiktok
  collected_at: new Date().toISOString(),
  posted_at: p.posted_at,
  hours_since_post: hoursBetween(p.posted_at, Date.now()),
  views: p.views ?? 0,
  watch_through_pct: p.watch_through_pct ?? null,
  likes: p.likes ?? 0,
  comments: p.comments ?? 0,
  shares: p.shares ?? 0,
  follows: p.follows ?? 0,
  engagement_rate: (p.likes + p.comments + p.shares) / Math.max(p.views, 1)
}}));
```

**M5 — Upsert (idempotent)**
```sql
INSERT INTO daily_metrics (...) VALUES (...)
ON CONFLICT (content_id, platform, snapshot_label) DO UPDATE SET ...;
```
> `snapshot_label` = `early` of `mature` (zie §5) zodat je per post meerdere meetmomenten bewaart zonder dubbels.

---

## 5. SCHEMA-HERONTWERP VAN DE TIJDLIJN (antwoord op je wens om het schema te laten passen bij de optimale uploadtijd)

**Probleem in de oude opzet:** generatie 09:00 + post 's avonds + metrics 24u later → "vandaag" gebruikte data van ~38u oud.

**Nieuwe, ontkoppelde cadans:**

| Wanneer | Wat |
|---------|-----|
| **'s Avonds (bv. 20:00)** | Genereer de content voor de **volgende** dag → jij keurt 's avonds goed → assets klaar |
| **Volgende dag, optimale tijden** | Jij uploadt (TikTok ~19:30, IG ~18:00, YT ~12:00) |
| **Metrics 3×/dag** (bv. 09:00 / 15:00 / 23:00) | Pijplijn vult de DB continu: `early`-snapshot (eerste uren = vroege viral-signaal) + `mature`-snapshot (24u+) |

Doordat de DB **altijd vers** is, leest de avond-generatie simpelweg "laatst beschikbare metrics" — geen wachttijd, geen verouderde data. Tijdstippen zijn instelbaar; de agent stelt ze bij op basis van wat het beste presteert.

> **Bonus:** de `early`-snapshot (snelheid in de eerste uren) is vaak een béter voorspeller van een hit dan de 24u-views, en voedt zo direct de keuzes van de volgende avond.

---

## 6. VERWERKING & LEERSIGNAAL (automatisch)

Node M6/M7 berekent en schrijft elke run:
- **Per post:** engagement rate, views-delta t.o.v. vorige snapshot, beste platform.
- **Rollend (laatste 3–5 dagen):** welke contenttypes/hooks/lengtes/posttijden boven de mediaan zitten.
- **LEERSIGNAAL-blok** (zoals in Phase 3) → automatisch klaargezet voor de volgende generatie én getoond op het dashboard.
- **Pacing naar 1M:** cumulatief vs. lineair doel, benodigd daggemiddelde resterende dagen.

Geen handmatige analyse: de cijfers stromen door tot een kant-en-klare aanbeveling.

---

## 7. KOPPELING MET HET DASHBOARD (Phase 4)

Het dashboard wordt nu nog gevuld met voorbeelddata. Voor live gebruik:
- N8N schrijft na elke metrics-run een klein **`dashboard_data.json`** (of een read-endpoint) weg.
- Het dashboard haalt dat bestand op bij laden/refresh en vult de grafieken, KPI's en het LEERSIGNAAL automatisch.
- Zo zie je realtime de actuele stand zonder iets in te typen.

> Je had aangegeven dat de N8N-dashboardkoppeling geen harde eis is. Dit JSON-bestand is de simpelste, gratis koppeling die binnen je stack past; een zwaardere database-koppeling kan later.

---

## 8. SETUP-CHECKLIST (wat heeft actie nodig?)

- [ ] **YouTube:** Google Cloud-project + OAuth-consent + Data/Analytics API aanzetten → refresh token opslaan. *(automatiseerbaar, gratis)*
- [ ] **Instagram:** account omzetten naar Business/Creator, koppelen aan een Facebook-pagina, Meta-app maken, long-lived token. *(automatiseerbaar, gratis, fiddly)*
- [ ] **TikTok:** developer-account + app + **toegang aanvragen** voor API for Business (nu starten i.v.m. doorlooptijd). Tijdelijke brug: vision-ingest (route C).
- [ ] **DB-tabel `daily_metrics`** uitbreiden met `snapshot_label`, `posted_at`, `hours_since_post`.
- [ ] **Metrics-workflow** 3×/dag inplannen; **generatie** naar de avond verschuiven.
- [ ] **`dashboard_data.json`**-export toevoegen aan het einde van de metrics-run.

---

## 9. EERLIJKE KANTTEKENINGEN

- **TikTok is en blijft de zwakke schakel** voor nieuwe accounts. Reken op een overgangsperiode met de vision-brug (route C) of accepteer een betaalde aggregator (route B) als je dag 1 al volledig hands-off wilt.
- **Nieuwe accounts hebben in het begin weinig data** → de eerste dagen is het LEERSIGNAAL dun en onbetrouwbaar (cold start uit Phase 3 blijft gelden).
- **API-quota & rate limits** bestaan; vandaar dat we per post upserten en niet eindeloos pollen.
- **Privacy/ToS:** gebruik alleen officiële API's of je eigen geëxporteerde data — geen scraping (dat is tegen de voorwaarden en risicovol).

---

## ✅ SAMENVATTING

Een ontkoppelde metrics-pijplijn houdt de DB doorlopend vers, verwerkt cijfers automatisch tot KPI's, trends en een kant-en-klaar LEERSIGNAAL, en voedt zowel het dashboard als de volgende contentgeneratie — zonder handmatig typen. YouTube en Instagram zijn meteen volledig te automatiseren; voor TikTok kies je route A (+C als brug) of B. Het schema verschuift naar avond-generatie zodat de data altijd vers is bij gebruik.

**Open beslissing:** welke TikTok-route (A, B of C) wil je?
