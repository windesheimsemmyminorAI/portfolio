# 🎓 Overzicht voor de beoordelaar

Dit is het portfolio van **Semmy el Kramti** voor de minor **Digitale Transformatie & Generatieve AI** (Hogeschool Windesheim). Deze repository bundelt meerdere projecten. Dit document is de **leeswijzer**: het wijst je naar de onderdelen, de belangrijkste bewijsstukken en de versiehistorie.

> Laatst bijgewerkt: 23-06-2026

---

## 📂 De drie onderdelen

| # | Onderdeel | Map | Korte omschrijving |
|---|-----------|-----|--------------------|
| 1 | **Inkoopfacturatie-dashboard** | `scripts/`, `dashboard/`, `data/`, `schemas/` | Python-validatie van facturen + automatisch gegenereerd HTML-dashboard |
| 2 | **N8N-workflows** | `n8n/` | De dashboard-workflow voor Bajo Bouw in N8N, iteratie v1 t/m v14, met versiedocumentatie en definitieve overdrachtsversie |
| 3 | **Wolfje & Bella — Media Agentic** | `wolfje-media-agentic/` | AI-contentpijplijn voor een getekende stripserie; incl. de geproduceerde Episode 1 "The Lookout" |

Elk onderdeel heeft een eigen `README.md` met uitleg.

---

## 1. Inkoopfacturatie-dashboard

- **Start:** `README.md` (root) — wat het doet en hoe je het draait.
- **Code:** `scripts/verwerk_facturen.py` (validatie in 5 regels) + `scripts/genereer_docs.py` (auto-documentatie).
- **Automatische documentatie:** `OVERDRACHT.md`, `REVISIE_LOG.md`, `NODE_DOCUMENTATIE.md` worden **automatisch** door GitHub Actions gegenereerd bij elke push naar `main` (zie `.github/workflows/update-docs.yml` en `docs/automatische_documentatie.md`). Niet met de hand bijwerken.
- **Uitleg techniek:** `docs/hoe_het_werkt.md`.

## 2. N8N-workflows

- **Start:** `n8n/README.md` → `n8n/dashboard/README.md`.
- **Ontwikkellijn (bewijs van iteratief werken):** `n8n/dashboard/versiedocumentatie.md` (én `.docx` voor het portfolio) beschrijft **iteratie 1 t/m 14** — van AI-agent, via een te complex e-maildashboard, naar het werkende KPI-dashboard, het wekelijkse weekrapport, de koppeling aan de nieuwe databron en vier gerichte bugfixes.
- **Workflows:** `v1_…` t/m `v11_…`. Huidige versies: **v6** (webpagina) en **v11 overdrachtsversie** (inhoudelijk v14 — definitief wekelijks e-mailrapport naar `indy@bajo-bouw.nl`).

## 3. Wolfje & Bella — Media Agentic

- **Start:** `wolfje-media-agentic/README.md` (concept, fases 0–5, projectstructuur).
- **Single source of truth:** `phase-0-spec/project_specification.md`.
- **Karakterontwerp & iteraties:** `phase-0-spec/characters/wolfje/` (canon, model-sheets, prompts, renders, logs) en `reference-material/` + `reference-material/IMAGE-CATALOG.md` (elk beeld met betekenis/status).
- **Geproduceerde aflevering:** `approved-content/season-1/episode-01-the-lookout/` — de afgemaakte strip (HTML), video's en de bronpanelen (`panels/`), met een eigen `README.md` die de verhaalvolgorde en de **gekozen** panelen vs. varianten documenteert.
- **Eindterm-prompt:** `wolfje-media-agentic/docs/wolfje-eindterm-verslag-prompt.md`.
- **`_archief/`:** bewust bewaarde **oudere iteraties/duplicaten** (bewijs van het ontwerpproces); niet de actieve versies.
- **Chat-import (historisch):** `README-IMPORT.md`, `docs/session-logs/`, `docs/MISSING-IMAGES-CHECKLIST.md`.

---

## 🧾 Versiehistorie als bewijs (Pull Requests)

De ontwikkeling is per onderwerp via Pull Requests gemerged naar `main` — die blijven op GitHub zichtbaar als bewijs van het proces:

| PR | Onderwerp |
|----|-----------|
| [#10](https://github.com/windesheimsemmyminorAI/portfolio/pull/10) | n8n v9 + v10 (oude/nieuwe koppeling) workflows + versiedocumentatie bijgewerkt |
| [#9](https://github.com/windesheimsemmyminorAI/portfolio/pull/9) | Leeswijzer voor beoordelaar (BEOORDELAAR.md) |
| [#8](https://github.com/windesheimsemmyminorAI/portfolio/pull/8) | Documentatie-audit: n8n v8 + wolfje episode-1 + README-synchronisatie |
| [#7](https://github.com/windesheimsemmyminorAI/portfolio/pull/7) | Wolfje turnaround sheet v2 / rommelmap opgeruimd + Episode 1 gestructureerd |
| [#6](https://github.com/windesheimsemmyminorAI/portfolio/pull/6) | Import wolfje chat-documentatie |
| [#5](https://github.com/windesheimsemmyminorAI/portfolio/pull/5) | Import chat-historie, beeldcatalogus en sessie-logboeken |

De volledige, automatisch bijgewerkte wijzigingsgeschiedenis staat in **`REVISIE_LOG.md`**.

---

## ▶️ Snel zelf draaien

```bash
# Factuur-dashboard (onderdeel 1)
cd scripts
python verwerk_facturen.py      # valideert facturen + bouwt dashboard/index.html

# N8N-workflows (onderdeel 2): importeer een v*.json in N8N (Import from File)
# Wolfje strip (onderdeel 3): open
#   wolfje-media-agentic/approved-content/season-1/episode-01-the-lookout/wolfje-bella-s1e01-the-lookout-strip.html
```
