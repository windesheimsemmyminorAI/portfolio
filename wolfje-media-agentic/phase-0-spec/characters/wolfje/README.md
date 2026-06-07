# 🐺 Wolfje — character workspace (Phase 0)

Alle character-design van **Wolfje** (jongvolwassen = canon; pup + eerste periode volgen). Bella krijgt
later een eigen map naast deze: `phase-0-spec/characters/bella/`.

> Deze map is op 2026-06-07 gereorganiseerd uit de oude `wolfje-bella-backup/`. Verouderde dubbele
> documenten en lege stub-bestanden zijn verwijderd; de inhoud daarvan staat onder de juiste namen in
> `phase-0-spec/` (de design-prompts) en de top-level fase-mappen.

## Structuur

| Map | Inhoud |
|-----|--------|
| `canon/` | Het vergrendelde canon-beeld (`wolfje-jongvolwassen-CANON.png`) + canon-beschrijving + selectielog. `canon/reference-inputs/` = de bijgesneden foto's waarmee de canon is gemaakt. |
| `input-photos/` | De echte foto's van Wolfje (AI-input, nooit output). |
| `model-sheets/` | Turnaround-prompts + de 5 goedgekeurde turnaround-cellen (`character-sheets/`). |
| `prompts/` | Karakter-prompts (analyse + 4 prompts, prompt-v3, meta-prompt) + `gemini-output/` (ruwe Gemini-prompts). |
| `renders/` | Gegenereerde beelden per ronde (zie onder). |
| `logs/` | `CHANGELOG.md`, `PROGRESS-LOG.md`, `HANDOFF…` — het doorlopende werklogboek. |
| `style-reference/` | Backup-kopie van de stijlreferentie (canoniek staat in `reference-material/style-reference/`). |

## `renders/` — per ronde

| Map | Status |
|-----|--------|
| `round-1/` | ⚠️ Beelden **niet bewaard** (vroege test). Zie README in de map. |
| `round-2/` · `round-3/` | Bewaard. Dit zijn **backup-kopieën**; de canonieke set staat in `wolfje-media-agentic/reference-material/style-results/`. |
| `canon-neck-edit/` | ⚠️ Alleen Render 3 (= de canon) bewaard; Renders 1/2/4 ontbreken. |
| `prompttest-abcd/` | ⚠️ Deels bewaard (Gemini-varianten + 1 v2-output). |
| `rejected/` | Afgewezen renders die wél bewaard zijn (de front-turnaround-kandidaten). |

> Volledige analyse van wat ontbreekt: `../../ONTBREKENDE-BEELDEN-phase-0.md`.
