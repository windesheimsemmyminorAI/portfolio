# 🔄 WOLFJE & BELLA MEDIA AGENTIC — PHASE 2 (v2): N8N WORKFLOW

**Version:** 2.0 (corrected)
**Date:** 5 June 2026
**Status:** GitHub-ready

> **Wat is er gecorrigeerd t.o.v. v1?**
> 1. ✅ **Echte render-nodes toegevoegd** — v1 produceerde alleen tekst. Nu: een node die strippagina's rendert (Google beeldmodel) en een node die video maakt (Veo).
> 2. ✅ **Gemini auth-header gecorrigeerd:** `x-goog-api-key` (was foutief `x-api-key`).
> 3. ✅ **Veo als long-running operation:** starten → pollen → downloaden (kan niet in één call).
> 4. ✅ **Flow is sequentieel** (Prompt 2 hangt af van 1; Prompt 3 van 1+2) — "parallel" geschrapt.
> 5. ✅ **n8n-syntax gecorrigeerd:** JavaScript i.p.v. Jinja-filters; `$('Node')`-notatie; geen placeholders.
> 6. ✅ **Modelstrings actueel:** `claude-sonnet-4-6` / `claude-opus-4-8`.
> 7. ✅ **Metrics realistisch:** aparte cron-workflow die de DB bevraagt; API's met eerlijke drempels; handmatige fallback.

> **📌 Update n.a.v. vastgelegde keuzes (zie `phase-0-spec/project_specification.md`):**
> - Alle publieksgerichte output is **Engels**; volledige animatie (echte beelden alleen als input).
> - Het **schema is verschoven naar avond-generatie** en de **metrics zijn nu volledig geautomatiseerd** — die staan uitgewerkt in **Phase 5**; de "metrics realistisch / handmatige fallback" hieronder is daar vervangen door de automatische pijplijn (YouTube + Instagram automatisch, TikTok route A + C).
> - **Goedgekeurde bestanden** worden opgeslagen in de **GitHub-map** (`approved-content/`).
> - **Audio:** alleen rechtenvrije / platform-eigen tracks.

---

## 📋 OVERZICHT — DAGELIJKSE CYCLUS

```
09:00  Cron-trigger
  ↓
[Wacht op upload: foto/video + omschrijving + dag/seizoen]
  ↓
NODE 3  Haal metrics van gisteren uit DB
  ↓ (SEQUENTIEEL — elke stap heeft de vorige nodig)
NODE 4  Claude → stripscript + beeldprompts + dialoog
NODE 5  Beeldmodel → render panelen (1 call per pagina)
NODE 6  Overlay → zet dialoogballonnen op panelen
NODE 7  Claude → storyboard + Veo-prompts
NODE 8  Veo → start video → POLL tot klaar → download
NODE 9  Claude → titels/captions/hashtags/posttijden
NODE 10 Claude → zelfreflectie (5 zinnen)
  ↓
NODE 11 Bundel alles
NODE 12 Stuur ter goedkeuring (Slack/e-mail) → JIJ keurt goed
  ↓ approve
NODE 13 Sla op in DB (status: approved_pending_upload)
  ↓
[JIJ uploadt handmatig — eerste 14 dagen, niets zonder jouw toestemming]
  ↓
APARTE CRON-WORKFLOW (1×/dag): haal metrics op van content die ~24u geleden is gepost → DB
```

---

## 🛠️ NODES

### NODE 1 — Cron-trigger
```json
{
  "name": "Daily Trigger",
  "type": "n8n-nodes-base.scheduleTrigger",
  "parameters": {
    "rule": { "interval": [{ "field": "cronExpression", "expression": "0 9 * * *" }] }
  },
  "notes": "Tijdzone in n8n-instellingen op Europe/Amsterdam zetten."
}
```

### NODE 2 — Upload van de dag (handmatige input via Form/Webhook)
```json
{
  "name": "User Input",
  "type": "n8n-nodes-base.formTrigger",
  "parameters": {
    "formFields": { "values": [
      { "fieldLabel": "media_file", "fieldType": "file", "requiredField": true },
      { "fieldLabel": "media_description", "fieldType": "textarea", "requiredField": true },
      { "fieldLabel": "day_number", "fieldType": "number", "requiredField": true },
      { "fieldLabel": "season_number", "fieldType": "number", "requiredField": true }
    ]}
  }
}
```

### NODE 3 — Metrics van gisteren (DB-read)
```json
{
  "name": "Fetch Yesterday Metrics",
  "type": "n8n-nodes-base.postgres",
  "parameters": {
    "operation": "executeQuery",
    "query": "SELECT * FROM daily_metrics WHERE content_date = CURRENT_DATE - INTERVAL '1 day' LIMIT 1;"
  },
  "notes": "Kan ook n8n built-in static data / Data Store zijn i.p.v. Postgres."
}
```

### NODE 4 — Stripscript (Claude)
```json
{
  "name": "Generate Strip Script",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.anthropic.com/v1/messages",
    "sendHeaders": true,
    "headerParameters": { "parameters": [
      { "name": "x-api-key", "value": "={{ $env.CLAUDE_API_KEY }}" },
      { "name": "anthropic-version", "value": "2023-06-01" },
      { "name": "content-type", "value": "application/json" }
    ]},
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={{ JSON.stringify({ model: 'claude-sonnet-4-6', max_tokens: 4000, system: [{ type: 'text', text: $env.STRIP_SYSTEM_PROMPT, cache_control: { type: 'ephemeral', ttl: '1h' } }], messages: [{ role: 'user', content: 'FOTO/VIDEO: ' + $('User Input').item.json.media_description + '\\nSEIZOEN: ' + $('User Input').item.json.season_number + ' | DAG: ' + $('User Input').item.json.day_number + '\\nSchrijf het script nu.' }] }) }}"
  },
  "notes": "STRIP_SYSTEM_PROMPT = het gecachte system-blok uit Phase 1 v2 (Prompt 1). Caveman user-bericht."
}
```

### NODE 5 — Render strippagina's (Google beeldmodel)
```json
{
  "name": "Render Strip Pages",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://generativelanguage.googleapis.com/v1beta/models/{IMAGE_MODEL}:generateContent",
    "headerParameters": { "parameters": [
      { "name": "x-goog-api-key", "value": "={{ $env.GEMINI_API_KEY }}" },
      { "name": "Content-Type", "value": "application/json" }
    ]},
    "notes": "Loop over de pagina's (Split In Batches). Geef per call de BEELDPROMPT + het referentiebeeld van Wolfje/Bella mee (image-to-image) voor consistentie. Verifieer de exacte image-modelnaam in de Gemini-docs."
  }
}
```
> ⚠️ **Header is `x-goog-api-key`** (niet `x-api-key`). Alternatief: `?key=` als query-param.

### NODE 6 — Tekstballon-overlay
```json
{
  "name": "Add Speech Bubbles",
  "type": "n8n-nodes-base.code",
  "parameters": {
    "language": "javaScript",
    "jsCode": "// Plak DIALOOG (uit Node 4) als ballon-overlay op de panelen (Node 5).\n// Gebruik bv. een image-lib of een HTML/CSS-naar-PNG render-service.\n// return [{ json: { pages_with_text: [...] } }];"
  },
  "notes": "Hier worden ballonnen toegevoegd omdat beeldmodellen tekst-in-beeld onbetrouwbaar renderen."
}
```

### NODE 7 — Storyboard + Veo-prompts (Claude)
```json
{
  "name": "Generate Storyboard",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.anthropic.com/v1/messages",
    "headerParameters": { "parameters": [
      { "name": "x-api-key", "value": "={{ $env.CLAUDE_API_KEY }}" },
      { "name": "anthropic-version", "value": "2023-06-01" }
    ]},
    "jsonBody": "={{ JSON.stringify({ model: 'claude-sonnet-4-6', max_tokens: 2500, messages: [{ role: 'user', content: $env.STORYBOARD_PROMPT + '\\n\\nSTRIP_SCRIPT:\\n' + $('Generate Strip Script').item.json.content[0].text }] }) }}"
  }
}
```

### NODE 8 — Video genereren (Veo, long-running)
```json
{
  "name": "Generate Video (Veo)",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-generate-preview:predictLongRunning",
    "headerParameters": { "parameters": [
      { "name": "x-goog-api-key", "value": "={{ $env.GEMINI_API_KEY }}" }
    ]}
  },
  "notes": "Veo geeft een operation terug. Daarna: NODE 8b (Wait ~15s) → NODE 8c (GET operation status) → IF done? nee: terug naar Wait | ja: download video. Verifieer exacte Veo-modelnaam in de Gemini-docs."
}
```
```
NODE 8b  Wait (15s)
NODE 8c  HTTP GET operation-status → IF (.done == true) ? download : terug naar 8b
```

### NODE 9 — Optimalisatie (Claude)
```json
{
  "name": "Optimize Posts",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.anthropic.com/v1/messages",
    "jsonBody": "={{ JSON.stringify({ model: 'claude-sonnet-4-6', max_tokens: 2000, messages: [{ role: 'user', content: $env.OPTIMIZE_PROMPT + '\\nSTRIP: ' + $('Generate Strip Script').item.json.content[0].text.substring(0, 600) + '\\nVIDEO: ' + $('Generate Storyboard').item.json.content[0].text.substring(0, 400) + '\\nMETRICS: ' + JSON.stringify($('Fetch Yesterday Metrics').item.json) }] }) }}"
  },
  "notes": "Let op: JavaScript .substring(0, N) — NIET het Jinja-filter '| substring'."
}
```

### NODE 10 — Zelfreflectie (Claude)
```json
{
  "name": "Self Reflection",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.anthropic.com/v1/messages",
    "jsonBody": "={{ JSON.stringify({ model: 'claude-sonnet-4-6', max_tokens: 500, messages: [{ role: 'user', content: $env.REFLECTION_PROMPT + '\\nKEUZES: video ' + $('Generate Storyboard').item.json.content[0].text.substring(0,200) + ' | posttijden+titels uit optimize' }] }) }}"
  }
}
```

### NODE 11 — Bundelen (Code)
```json
{
  "name": "Compile Assets",
  "type": "n8n-nodes-base.code",
  "parameters": {
    "language": "javaScript",
    "jsCode": "const day = $('User Input').item.json.day_number;\nconst season = $('User Input').item.json.season_number;\nreturn [{ json: {\n  day_number: day,\n  season: season,\n  created_at: new Date().toISOString(),\n  strip_script: $('Generate Strip Script').item.json.content[0].text,\n  storyboard: $('Generate Storyboard').item.json.content[0].text,\n  optimization: $('Optimize Posts').item.json.content[0].text,\n  reflection: $('Self Reflection').item.json.content[0].text\n}}];"
  },
  "notes": "Geen placeholders meer; echte JS die de velden samenvoegt."
}
```

### NODE 12 — Goedkeuring vragen
```json
{
  "name": "Send for Approval",
  "type": "n8n-nodes-base.slack",
  "parameters": {
    "resource": "message",
    "operation": "post",
    "text": "=📋 Dag {{ $('User Input').item.json.day_number }} klaar.\\n\\n🧠 Reflectie:\\n{{ $('Self Reflection').item.json.content[0].text }}\\n\\n📢 Optimalisatie:\\n{{ $('Optimize Posts').item.json.content[0].text }}\\n\\nKeur goed in n8n om op te slaan. (Upload doe je zelf — niets gaat live zonder jouw toestemming.)"
  },
  "notes": "Eerste 14 dagen: handmatige goedkeuring + handmatige upload. Daarna evalueren."
}
```

### NODE 13 — Opslaan na goedkeuring
```json
{
  "name": "Save Approved Content",
  "type": "n8n-nodes-base.postgres",
  "parameters": {
    "operation": "insert",
    "table": "approved_content",
    "columns": "day_number, season, created_at, status, payload",
    "notes": "status = 'approved_pending_upload'. payload = JSON uit Node 11."
  }
}
```

---

## 📊 APARTE WORKFLOW — METRICS OPHALEN (1×/dag)

```
Cron (1×/dag)
  ↓
Query DB: welke content is ~24u geleden gepost?
  ↓
Per platform metrics ophalen (API of handmatige fallback)
  ↓
Schrijf naar tabel daily_metrics  → gebruikt door hoofdworkflow Node 3 (volgende dag)
```

> **Eerlijk over de API-drempels:**
> - **TikTok:** analytics vereist goedgekeurde developer-toegang — niet zomaar gratis voor individuen.
> - **Instagram:** vereist een Business/Creator-account gekoppeld aan een Facebook-pagina + app review (Graph API).
> - **YouTube:** YouTube Analytics API via OAuth.
> - **Fallback:** omdat je de eerste 14 dagen tóch handmatig uploadt, kun je de metrics ook handmatig in een formulier/Sheet zetten. De automatisering is dus "nice to have", geen blocker.

---

## 🔐 QUALITY GATES & ERROR HANDLING

```json
[
  { "gate": "Strip < 8 pagina's", "node": "IF na Node 4", "actie": "Slack-bericht: 'stuur meer foto's/video's'; workflow stoppen" },
  { "gate": "API-fout (Claude/Gemini/Veo)", "node": "HTTP-retry", "actie": "3× retry, dan alert naar jou" },
  { "gate": "Veo niet klaar na X polls", "node": "teller in 8c", "actie": "alert + sla overige assets toch op" },
  { "gate": "Dagelijkse tokenlimiet", "node": "Code-check", "actie": "som tokens; bij naderen limiet → pauzeer + alert" }
]
```

---

## 🔌 ENV-VARIABELEN

```env
CLAUDE_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...           # zelfde key werkt voor beeldmodel én Veo
STRIP_SYSTEM_PROMPT=...          # gecachte system-blok (Phase 1 v2, Prompt 1)
STORYBOARD_PROMPT=...            # Phase 1 v2, Prompt 2A
OPTIMIZE_PROMPT=...              # Phase 1 v2, Prompt 3
REFLECTION_PROMPT=...            # Phase 1 v2, Prompt 4
SLACK_CHANNEL=...
# Optioneel (metrics):
YOUTUBE_OAUTH=... / IG_GRAPH_TOKEN=... / TIKTOK_DEV_TOKEN=...
```

---

## ✅ CORRECTIE-CHECKLIST (v1 → v2)

- [x] Render-node voor strip (beeldmodel) toegevoegd
- [x] Echte video via Veo (long-running + polling)
- [x] DALL-E verwijderd (geen OpenAI-abonnement nodig)
- [x] Gemini-header `x-goog-api-key`
- [x] Sequentiële flow (geen valse "parallel")
- [x] n8n-syntax: `$('Node').item.json`, JS `.substring()`, geen placeholders
- [x] Actuele modelstrings
- [x] Caching alleen binnen dagrun (ttl 1h), niet tussen dagen
- [x] Tekst-overlay-node i.p.v. tekst-in-beeld
- [x] Eerlijke metrics-aanpak met handmatige fallback
- [x] Handmatige upload eerste 14 dagen geborgd

---

> ⚠️ De JSON-snippets hierboven zijn **leesbare configuraties per node**, geschikt om te begrijpen en in GitHub te documenteren. Een direct-importeerbaar `.json`-export bouw je in n8n zelf op (sleep de nodes, plak deze parameters). Verifieer bij het bouwen de exacte image-/Veo-modelnamen in de Gemini-docs, want die wijzigen snel.

**Volgende:** Phase 3 — Self-Learning Loop (bovenop dit gecorrigeerde fundament).
