# 📦 Wolfje & Bella — Chat-import & documentatie

> ✅ **Import voltooid & gereorganiseerd (historisch document).** De beelden en docs
> uit dit bundel zijn inmiddels opgenomen en verplaatst naar hun definitieve plek
> onder `wolfje-media-agentic/` (vooral `phase-0-spec/characters/wolfje/` en
> `reference-material/`). De mappenstructuur hieronder beschrijft de **oorspronkelijke
> importbundel**, niet de huidige repo-indeling. Actuele locaties: zie
> `wolfje-media-agentic/README.md` en `reference-material/IMAGE-CATALOG.md`.
> De `docs/session-logs/` en `docs/tool-knowledge/` staan nog op hun plek.

Deze map bundelt de waardevolle informatie en beelden uit de vijf Claude-projectchats, klaar om **additief** in de GitHub-repo te worden opgenomen (niets overschrijven).

## Wat zit hierin

```
reference-material/
  style-results/round-2/   9 stijl-test-beelden (chat 1)
  style-results/round-3/   6 hero-renders, incl. gekozen cel-shaded richting (chat 1)
  style-results/round-5/   geanalyseerde v2-output (chat 2)
  style-reference/         de inkttekening-stijlbasis
  source-photos/           12 echte referentiefoto's (chat 1)
  source-photos/rear-reference/  4 achter/front-foto's uit de Gemini-app (chat 3)
  canon-candidates/        1 cel-shaded kandidaat-render (chat 3)
  IMAGE-CATALOG.md         ⭐ centrale beeldcatalogus — elk beeld met betekenis + status
docs/
  session-logs/            sessie-logboek per chat (1 t/m 5)
  tool-knowledge/          de Pillow-beeldverwerkingspijplijn (chat 4)
  MISSING-IMAGES-CHECKLIST.md  ⭐ wat je nog handmatig moet exporteren
  CLAUDE-CODE-IMPORT-PROMPT.md  de prompt om dit veilig in GitHub te zetten
```

## Twee documenten om mee te beginnen

1. **`docs/MISSING-IMAGES-CHECKLIST.md`** — de beelden die alleen in chats/GitHub leven en die je (na controle) handmatig exporteert. De chat-3-items hebben de hoogste prioriteit.
2. **`reference-material/IMAGE-CATALOG.md`** — de volledige catalogus die elk beeld traceerbaar maakt.

## Hoe naar GitHub

Gebruik `docs/CLAUDE-CODE-IMPORT-PROMPT.md` als prompt voor Claude Code. Die zet alles op een **aparte branch** met een PR, zodat bestaand werk gegarandeerd niet verloren gaat en jij het kunt reviewen vóór de merge.

## Belangrijke bevinding

De projectkennis bevat vooral het chat-1/2-tijdperk. Het canon-werk (de vergrendelde `wolfje-jongvolwassen-CANON.png`, turnaround-cellen 01–05, de canon-docs) is destijds direct naar GitHub gepusht en zit níet in deze import. Controleer daarom je huidige repo vóór je de checklist afwerkt — veel staat er waarschijnlijk al.
