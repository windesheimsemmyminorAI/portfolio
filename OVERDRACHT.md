# Overdracht

Dit document helpt iemand die het project overneemt snel op weg. Automatisch gegenereerd uit de huidige projectstaat.

Laatst bijgewerkt: 2026-06-07

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
- `claude-github-bridge.js`
- `dashboard/index.html`
- `data/facturen.json`
- `data/resultaat.json`
- `docs/automatische_documentatie.md`
- `docs/hoe_het_werkt.md`
- `n8n/README.md`
- `n8n/dashboard/GITHUB_UPDATE.md`
- `n8n/dashboard/README.md`
- `n8n/dashboard/v1_ai_agent.json`
- `n8n/dashboard/v2_gmail_dashboard.json`
- `n8n/dashboard/v3_webhook_dashboard.json`
- `n8n/dashboard/v4_webhook_werkend.json`
- `n8n/dashboard/v5_email_werkend.json`
- `n8n/dashboard/v6_webhook_kpi.json`
- `n8n/dashboard/v7_email_kpi.json`
- `n8n/dashboard/v8_email_weekrapport.json`
- `n8n/dashboard/versiedocumentatie.docx`
- `n8n/dashboard/versiedocumentatie.md`
- `schemas/factuur_schema.json`
- `scripts/REVISIE_LOG.md`
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
- `wolfje-media-agentic/phase-0-spec/ONTBREKENDE-BEELDEN-phase-0.md`
- `wolfje-media-agentic/phase-0-spec/character-design-iterations.md`
- `wolfje-media-agentic/phase-0-spec/character-generation-prompts.md`
- `wolfje-media-agentic/phase-0-spec/project_specification.md`
- `wolfje-media-agentic/phase-0-spec/reference-and-modelsheet-prompts.md`
- `wolfje-media-agentic/phase-0-spec/style-exploration-prompts.md`
- `wolfje-media-agentic/phase-0-spec/style-prompts-v2-met-fotos.md`
- `wolfje-media-agentic/phase-0-spec/style-results-log.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20250801_164033.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260324_010146.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260501_140420.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260501_140724.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260501_140725.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260518_194034.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260518_194125.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260518_194132.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260601_000746.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/20260605_170508.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/3stage_3d_a.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/3stage_3d_b.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/3stage_D_celshaded.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/3stage_storybook.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/3stage_vector.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A1_3d.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A2_vector.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A3_storybook.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A3_storybook_sit.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A4_celshaded_a.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/A4_celshaded_b_CHOSENdirection.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/CANON-selectie-log.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/CANON-wolfje-jongvolwassen.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/CHANGELOG.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Gemini_Generated_Image_75x9mw75x9mw75x9.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Gemini_Generated_Image_e1y0yde1y0yde1y0.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Gemini_Generated_Image_jihli4jihli4jihl.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Gemini_Generated_Image_pkev1vpkev1vpkev.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Gemini_Generated_Image_zct55azct55azct5.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/HANDOFF-naar-nieuwe-chat.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/PROGRESS-LOG.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/README.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/README__3_.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/Snapchat398132089.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/character-design-iterations.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/character-generation-prompts.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/download__1_`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/download__2_`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/model-sheets/wolfje-jongvolwassen-turnaround-prompts.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/niece_style_reference.jpeg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/output_v2_celshaded_jongvolwassen.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/project_specification.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/raw-gemini-variant1-yellow.txt`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/raw-gemini-variant2-lavender.txt`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/raw-gemini-variant3-mint.txt`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/raw-gemini-variant4-peach.txt`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/raw-gemini-variant5-blue.txt`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/wolfje-jongvolwassen-gemini-prompts-v2-defluffed.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/prompts-gemini-output/wolfje-jongvolwassen-gemini-prompts.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-and-modelsheet-prompts.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-inputs-canon/wolfje-ref-gezicht-bijgesneden.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-inputs-canon/wolfje-ref-hero-bijgesneden.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-inputs-canon/wolfje-ref-vacht-bijgesneden.jpg`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/CHANGELOG.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/PROGRESS-LOG-entry_2026-06-07.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/candidates/wolfje-jv-turn-01-front_kandidaat-A.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/candidates/wolfje-jv-turn-01-front_kandidaat-B.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/candidates/wolfje-jv-turn-01-front_kandidaat-C.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/candidates/wolfje-jv-turn-01-front_kandidaat-C2.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/candidates/wolfje-jv-turn-01-front_kandidaat-D_hires.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/wolfje-jv-turn-01-front.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/wolfje-jv-turn-02-driekwart-front.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/wolfje-jv-turn-03-zij.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/wolfje-jv-turn-04-driekwart-achter.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/reference-material/character-sheets/wolfje-jv-turn-05-achter.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/single_A_3d.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/single_B_vector.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/single_C_storybook.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/single_D_celshaded.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/style-prompts-v2-met-fotos.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/style-results-log.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje-jongvolwassen-CANON.png`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje-jongvolwassen-analyse-en-4-prompts.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje-jongvolwassen-prompt-v3.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_bella_dashboard.html`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_media_agentic_phase1_prompts_v2.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_media_agentic_phase2_workflow_v2.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_media_agentic_phase3_learning.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_media_agentic_phase5_metrics.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_metaprompt_gemini_naar_nanobanana.md`
- `wolfje-media-agentic/phase-0-spec/wolfje-bella-backup/wolfje_voor.jpg`
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
