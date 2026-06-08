# Sessie-logboek — Chat 01: "Media content creation workflow setup"

**Datum:** 6 juni 2026 (laatste update 10:36)
**Chat-link:** https://claude.ai/chat/1f36d59c-f6ee-4b33-a994-4ced4cbf5b9b
**Fase:** Phase 0 — fundament + stijlexploratie
**Rol Claude:** lead engineer / architect · **Beeldgeneratie:** Semmy (Gemini / Nano Banana)

> Dit logboek legt het denkproces en de beslissingen van deze chat vast als portfolio-bewijs.
> Het *dupliceert* de bestaande docs niet, maar verwijst ernaar.

---

## 1. Wat er in deze chat is gebeurd (chronologie)

1. **Briefing & discovery.** Semmy briefte het 4-fasen-systeem (strip-generatie, video, social upload, zelflerende agent). Via een uitgebreide vraag-en-antwoord-dialoog werden álle projectparameters vastgelegd vóór er gebouwd werd: Engelstalige publieksoutput met Nederlandse input, volledig geanimeerde cartoon-output (echte hondenfoto's alleen als AI-input, nooit in de eindoutput), drie seizoenen gekoppeld aan Wolfjes leeftijdsfasen, accounts vanaf nul, rechtenvrije audio, avond-generatieschema, goedgekeurde bestanden naar GitHub als portfolio-bewijs, en automatische metrics (YouTube + Instagram direct, TikTok via officiële API-aanvraag + vision-bridge).
2. **Zes deliverables gebouwd** in gestructureerde fasen:
   - **Phase 0** — `project_specification.md` (single source of truth)
   - **Phase 1 v2.1** — vier master-prompts (stripscript, animatie-short via Veo, optimalisatie, 5-zins zelfreflectie)
   - **Phase 2 v2** — N8N-workflow, 14 nodes, `x-goog-api-key`-auth, sequentieel i.p.v. schijn-parallel, Veo als long-running operation met polling, speech bubbles als tekst-overlay
   - **Phase 3** — zelflerende loop (content-tagging, metrics-feedback, A/B-cadans, guardrails, pacing-tracker ~47.600 views/dag)
   - **Phase 4** — standalone HTML approval-dashboard met SVG-grafieken + approve/reject-flow
   - **Phase 5** — automatische metrics-pijplijn + avond-generatieschema
3. **Phase 0-uitvoering: karakter-referentie verzameld.** Claude trok via `ffmpeg` frames uit geüploade foto's/video's en bouwde een gedetailleerde referentie van Wolfje.
4. **Stijlexploratie rondes 1–3** (zie sectie 3) → **cel-shaded gekozen als richting.**

## 2. Belangrijkste architectuur-correcties (vóór doorbouwen)

- **DALL-E verwijderd** — geen OpenAI-abonnement.
- **Veo** vervangt generieke Gemini-videogeneratie.
- **Prompt caching** gecorrigeerd naar binnen-run only (TTL max 1 uur, niet cross-day).
- **N8N-expressies** gecorrigeerd van Jinja naar JavaScript.

## 3. Stijlexploratie — beslissing (kern van deze chat)

Volledige redenering staat in `style-results-log.md`. Samengevat:

| Ronde | Aanpak | Uitkomst | Beelden |
|---|---|---|---|
| 1 | Alleen tekst, 4 stijlen | Te oranje over het hele lijf, generiek, geen gelijkenis | **Niet bewaard** (zie missing-checklist) |
| 2 | Met echte foto's + kleurcorrectie | Kleurverdeling beter, nog generiek | 9 beelden → `style-results/round-2/` |
| 3 | Eén hero-foto + exact identity-block | Duidelijk betere gelijkenis | 6 beelden → `style-results/round-3/` |

**Eindbeslissing ronde 3 — cel-shaded (`A4_celshaded_b_CHOSENdirection`) vergrendeld als richting.**
Bewuste trade-off: storybook/aquarel (A3) leek qua *zachtheid* het meest op de echte Wolfje, maar cel-shaded werd gekozen omdat het beter scoort op leesbaarheid op klein scherm, comedische expressiviteit en animatie-consistentie. Openstaand pijnpunt aan het einde van deze chat: **oren nog te oranje** → meegenomen naar de jongvolwassen-verfijning (chat 2).

## 4. Inzichten / leeruitkomsten

- Tekst-only prompts zijn onvoldoende voor gelijkenis → echte foto's als referentie meegeven.
- Te veel/gemengde referentiefoto's → rasdrift en generiek resultaat → één heldere hero-foto + exact identity-block werkt beter.
- Ogen werden te groot ("kawaii") → expliciet op natuurlijk formaat sturen.
- De gut-favoriet (storybook) werd bewust opzijgezet voor de technisch sterkere productiekeuze (cel-shaded) — gedocumenteerd als portfolio-bewijs van afweging.

## 5. Gekoppelde bestanden (deze chat)

- Specs/prompts: `project_specification.md`, `character-generation-prompts.md`, `character-design-iterations.md`, `style-prompts-v2-met-fotos.md`, `style-results-log.md`
- Fase-docs: `wolfje_media_agentic_phase1_prompts_v2.md`, `..._phase2_workflow_v2.md`, `..._phase3_learning.md`, `..._phase5_metrics.md`
- Dashboard: `wolfje_bella_dashboard.html`
- Beelden: zie `reference-material/IMAGE-CATALOG.md` (sectie Chat 01)
