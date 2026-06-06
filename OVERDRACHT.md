# Overdracht

Dit document helpt iemand die het project overneemt snel op weg. Automatisch gegenereerd uit de huidige projectstaat.

Laatst bijgewerkt: 2026-06-06

## Hoe draai je het project?

1. Open een terminal in de map `scripts`
2. Draai `python verwerk_facturen.py` (controleert facturen + bouwt dashboard)
3. Open `dashboard/index.html` in je browser
4. Draai `python genereer_docs.py` om deze documentatie bij te werken

## Huidige stand van zaken

Er zijn op dit moment **5 facturen** verwerkt:

- Goedgekeurd: 2
- Waarschuwing: 2
- Actie nodig: 1

## Bestanden in dit project

- `.github/workflows/update-docs.yml`
- `.gitignore`
- `NODE_DOCUMENTATIE.md`
- `OVERDRACHT.md`
- `README.md`
- `REVISIE_LOG.md`
- `dashboard/index.html`
- `data/facturen.json`
- `data/resultaat.json`
- `docs/automatische_documentatie.md`
- `docs/hoe_het_werkt.md`
- `n8n/README.md`
- `n8n/dashboard/README.md`
- `n8n/dashboard/v1_ai_agent.json`
- `n8n/dashboard/v2_gmail_dashboard.json`
- `n8n/dashboard/v3_webhook_dashboard.json`
- `n8n/dashboard/v4_webhook_werkend.json`
- `n8n/dashboard/v5_email_werkend.json`
- `n8n/dashboard/v6_webhook_kpi.json`
- `n8n/dashboard/v7_email_kpi.json`
- `n8n/dashboard/versiedocumentatie.docx`
- `n8n/dashboard/versiedocumentatie.md`
- `schemas/factuur_schema.json`
- `scripts/genereer_docs.py`
- `scripts/requirements.txt`
- `scripts/update.py`
- `scripts/verwerk_facturen.py`
- `wolfje-media-agentic/.gitignore`
- `wolfje-media-agentic/README.md`
- `wolfje-media-agentic/approved-content/README.md`
- `wolfje-media-agentic/approved-content/season-1/.gitkeep`
- `wolfje-media-agentic/approved-content/season-2/.gitkeep`
- `wolfje-media-agentic/approved-content/season-3/.gitkeep`
- `wolfje-media-agentic/phase-0-spec/character-design-iterations.md`
- `wolfje-media-agentic/phase-0-spec/character-generation-prompts.md`
- `wolfje-media-agentic/phase-0-spec/project_specification.md`
- `wolfje-media-agentic/phase-0-spec/reference-and-modelsheet-prompts.md`
- `wolfje-media-agentic/phase-0-spec/style-exploration-prompts.md`
- `wolfje-media-agentic/phase-0-spec/style-prompts-v2-met-fotos.md`
- `wolfje-media-agentic/phase-0-spec/style-results-log.md`
- `wolfje-media-agentic/phase-1-prompts/wolfje_media_agentic_phase1_prompts_v2.md`
- `wolfje-media-agentic/phase-2-workflow/wolfje_media_agentic_phase2_workflow_v2.md`
- `wolfje-media-agentic/phase-3-learning/wolfje_media_agentic_phase3_learning.md`
- `wolfje-media-agentic/phase-4-dashboard/wolfje_bella_dashboard.html`
- `wolfje-media-agentic/phase-5-metrics/wolfje_media_agentic_phase5_metrics.md`
- `wolfje-media-agentic/reference-material/README.md`
- `wolfje-media-agentic/reference-material/style-reference/niece_style_reference.jpeg`
- `wolfje-media-agentic/reference-material/style-results/round-2/3stage_3d_a.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/3stage_3d_b.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/3stage_D_celshaded.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/3stage_storybook.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/3stage_vector.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/single_A_3d.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/single_B_vector.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/single_C_storybook.png`
- `wolfje-media-agentic/reference-material/style-results/round-2/single_D_celshaded.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A1_3d.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A2_vector.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A3_storybook.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A3_storybook_sit.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A4_celshaded_a.png`
- `wolfje-media-agentic/reference-material/style-results/round-3/A4_celshaded_b_CHOSEN-direction.png`
