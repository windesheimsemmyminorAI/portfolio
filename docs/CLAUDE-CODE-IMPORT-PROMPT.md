# 🤖 Claude Code-prompt — veilige import naar GitHub

Plak onderstaande prompt in Claude Code, in de map van je lokale repo. Pas eerst de twee paden bovenaan aan.

---

```
Je gaat de inhoud van een import-map ADDITIEF toevoegen aan deze Git-repo. Het allerbelangrijkste: bestaand werk mag NIET verloren gaan of overschreven worden.

PADEN (pas aan):
- REPO   = . (de huidige repo-map waarin je staat)
- IMPORT = /pad/naar/uitgepakte/wolfje-import   ← pas dit aan naar waar je de zip hebt uitgepakt

HARDE REGELS:
- Werk NOOIT op main/master. Maak een nieuwe branch.
- Overschrijf of verwijder GEEN enkel bestaand bestand. Kopieer alleen bestanden die nog niet bestaan.
- Geen force-push, geen history rewrite.
- Stop en rapporteer bij twijfel; voer geen merge naar main uit.

STAPPEN:

1. Veiligheidscheck. Run `git status`. Als de working tree NIET schoon is, stop en meld dit — ik wil eerst zelf committen/stashen.

2. Branch. Maak en check uit: `git checkout -b import/wolfje-chat-documentatie`.

3. Inventariseer botsingen. Loop door alle bestanden onder IMPORT (recursief). Voor elk bestand met hetzelfde relatieve pad in REPO:
   - Bestaat het al in REPO? Zet het op een COLLISIONS-lijst en kopieer het NIET.
   - Bestaat het nog niet? Kopieer het naar REPO op exact hetzelfde relatieve pad.
   Gebruik bijvoorbeeld `cp -rn` (no-clobber) en bouw daarnaast expliciet de COLLISIONS-lijst op door per bestand te checken of het doel al bestaat.

4. Toon overzicht VÓÓR commit:
   - Lijst van NIEUW gekopieerde bestanden (aantal + paden).
   - COLLISIONS-lijst (bestanden die al bestonden en dus zijn overgeslagen) — zodat ik die handmatig kan vergelijken.
   - Run `git add -A` en daarna `git status` zodat ik de staged wijzigingen zie.

5. Wacht op mijn bevestiging. Toon het overzicht en VRAAG of je mag committen + pushen. Doe NIETS onomkeerbaars voordat ik "ja" zeg.

6. Na mijn "ja":
   - Commit met meerdere logische commits of één duidelijke:
     `git commit -m "docs+assets: import chat-historie, beeldcatalogus en sessie-logboeken (chats 1-5)"`
   - Push de branch: `git push -u origin import/wolfje-chat-documentatie`
   - Als de GitHub CLI beschikbaar is, open een DRAFT pull request:
     `gh pr create --draft --title "Import chat-historie & beeldcatalogus (chats 1-5)" --body "Additieve import van sessie-logboeken, IMAGE-CATALOG, tool-knowledge en de beelden uit projectkennis. Geen bestaande bestanden overschreven. Zie docs/MISSING-IMAGES-CHECKLIST.md voor wat nog handmatig geexporteerd moet worden."`
   - Merge NIET zelf naar main; dat doe ik via de PR-review.

7. Eindrapport. Geef een korte samenvatting: branch-naam, aantal toegevoegde bestanden, de COLLISIONS-lijst, en de PR-URL. Verwijs me naar docs/MISSING-IMAGES-CHECKLIST.md voor de resterende handmatige exports.

OPTIONEEL (alleen als ik erom vraag, niet automatisch):
- De repo-README.md bevat een verouderde kleur-spec ("abrikoos op kop/oren + zadel op rug"). De huidige canon is "vage abrikoos alleen op de achterkant van de oren, geen zadel". Stel een correctie voor als losse diff, maar pas niets aan zonder mijn akkoord.
```

---

## Waarom deze opzet veilig is

- **Aparte branch + draft PR** → niets raakt `main` voordat jij het reviewt.
- **No-clobber + collisions-lijst** → bestaande bestanden blijven onaangeroerd; je ziet precies wat al bestond.
- **Bevestiging vóór push** → een checkpoint waarop jij kunt ingrijpen.
- **Stale README als losse, optionele stap** → de inhoudelijke correctie wordt voorgesteld, niet stilletjes doorgevoerd.

## Nadat de PR binnen is

Werk daarna `docs/MISSING-IMAGES-CHECKLIST.md` af: controleer eerst wat al in de repo staat, exporteer dan gericht alleen de ontbrekende beelden (chat-3-canon en turnaround-cellen eerst), en plaats ze op de aangegeven paden.
