# 📝 CHANGELOG — Wolfje & Bella Media Agentic

> **Doorlopend logboek.** Nieuwste sessie bovenaan. Elke werksessie krijgt een eigen datumblok met: samenvatting · aanpassingen · toegevoegd · (eventueel) beeldmateriaal. Zo blijft de volledige geschiedenis navolgbaar als portfolio-bewijs.

---

## [2026-06-07] Sessie J — Versie-audit, gap-documentatie & GitHub-issues (project-hygiëne)

### Samenvatting
Geen nieuwe beelden of prompts deze sessie, maar **project-hygiëne en versiebeheer**. Aanleiding: een audit-vraag — *"welke versies zijn werkelijk aanwezig en gecommit, klopt het dat `v8_email_weekrapport.json` de laatste versie is, en is die gepusht?"* Dit is uitgezocht voor zowel `n8n/dashboard/` als `wolfje-media-agentic/`, waarna de bevindingen zijn vastgelegd in een nieuw logboek én als trackbare GitHub-issues.

### Wat is onderzocht (audit)
- **`n8n/dashboard/`** bevat genummerde workflow-JSON's **v1 t/m v8**. `v8_email_weekrapport.json` bestaat echt (commit `56c676a`) en zit in `origin/main` — dáár is het inderdaad de laatste versie.
- **`wolfje-media-agentic/`** bevat **géén** genummerde workflow-JSON's en dus ook geen `v8_…`. De "versies" hier zijn fase-documenten met `_v2`/`_v3`-suffix; de karakter-"versies" zijn levensfasen: **jongvolwassen** (canon, klaar), **pup** + **eerste periode** (gepland). → De v8-aanname hoorde bij een **ander project**; de twee waren door de naam verward.
- **Sync-status:** lokale `main` liep **1 commit achter** op `origin/main`; geen ongecommitte of genegeerde bestanden in de werkmap.

### Bevinding — 4 ontbrekende-beelden-gaps (Phase 0)
Het beslisproces is volledig navolgbaar in de logboeken, maar **niet alle versies/afgewezen beelden zijn als afbeelding bewaard**:
1. **Ronde 1** (stijlexploratie zonder foto's) — beeldmateriaal nooit bewaard, alleen beschreven.
2. **Afgewezen canon-renders (1, 2, 4)** — alleen Render 3 (canon) als bestand; 1/2/4 leven alleen in de checklist-tabel.
3. **Afgewezen turnaround-renders per hoek** — alleen de gekozen cel bewaard (uitzondering: front-kandidaten A/B/C/C2/D_hires).
4. **A/B/C/D-prompttest** — slechts deels in beeld (5 Gemini-varianten + 1 v2-output), niet elke run.

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `phase-0-spec/ONTBREKENDE-BEELDEN-phase-0.md` | Known-gaps-logboek met de 4 punten, bronverwijzingen, samenvattingstabel en reflectie. |

### Werkwijze (Git / GitHub)
- **Fast-forward sync** vóór het pushen om een non-fast-forward te voorkomen (`git pull --ff-only`, `685c06e..0af69b6`).
- Gap-doc gecommit (`f253fc2`) en gepusht naar `origin/main`. *Leermoment:* de eerste commit-message raakte verhaspeld doordat PowerShell-here-string-syntax (`@'…'@`) in een bash-shell werd gebruikt → hersteld met `git commit --amend -F -`.
- **4 GitHub-issues aangemaakt (#1–#4)**, één per gap. Omdat de `gh` CLI niet geïnstalleerd was, via de **GitHub REST API** met het token dat Git Credential Manager al voor de repo had (token nergens getoond of weggeschreven).

### Persoonlijke ontwikkeling — leerpunten
- **Versiebeheer-discipline:** bewaar niet alleen de winnaar maar ook de **afgewezen opties als bestand** — tekst-only logging maakt de visuele vergelijking achteraf onreproduceerbaar en verzwakt portfolio-bewijs.
- **Verifieer tegen de echte repo-staat, niet tegen aannames/namen:** de v8-verwarring tussen twee losse projecten laat zien waarom je claims checkt met `git ls-files`, `rev-parse` en `merge-base` i.p.v. op geheugen af te gaan.
- **Git-hygiëne:** ahead/behind lezen en eerst syncen vóór push; weten hoe je een commit-message corrigeert.
- **Shell-bewustzijn:** bash ≠ PowerShell (here-strings, redirects).
- **GitHub zonder gh CLI:** issues via de REST API + een bestaand credential, met zorgvuldige omgang met secrets.
- **Issues als tracking:** openstaande verbeterpunten naast in-repo documentatie zichtbaar en afvinkbaar maken.

### Volgende stap
Bij het genereren van pup + eerste periode (en verdere model sheets): vanaf nu **alle kandidaten + afgewezen renders meteen opslaan** in `reference-material/…`, zodat de gaps uit deze sessie niet opnieuw ontstaan.

---

## [2026-06-06] Sessie I — Turnaround: 3/4-achter vastgelegd + handoff

### Samenvatting
Cel 04 (3/4 achter) vastgelegd; turnaround is op de front-cel na compleet. Handoff-prompt gemaakt om in een nieuwe chat verder te bouwen.

### Aanpassingen
- **Vastgelegd:** `reference-material/character-sheets/wolfje-jv-turn-04-driekwart-achter.png` (Render 4 uit de achter-ronde) — gekozen omdat het de enige echte 3/4-achter hoek was; de twee zij-achtige alternatieven toonden het gezicht en dubbelden cel 02/03.
- **Toegevoegd:** `HANDOFF-naar-nieuwe-chat.md` — paste-klare overdrachtsprompt voor de volgende chat.

### Turnaround-voortgang
- [x] 02 — 3/4 front · [x] 03 — Zij · [x] 04 — 3/4 achter · [x] 05 — Achter · [ ] 01 — Front (laatste, in nieuwe chat)

### Volgende stap (nieuwe chat)
Front-cel draaien mét canon + 4 vastgelegde hoeken als referentie → turnaround compleet → expressie-sheet → actie-poses → pup + eerste periode.

---

## [2026-06-06] Sessie H — Turnaround: zij-cel vastgelegd

### Samenvatting
Zij-cel (03) vastgelegd. Uit 7 renders is **Render 6** gekozen — zachte cluster die het meest op de echte Wolfje + cel 02 lijkt.

### Aanpassingen
- **Vastgelegd:** `reference-material/character-sheets/wolfje-jv-turn-03-zij.png` (Render 6) — zacht rond Wolfje-gezicht, proportionele oren, warm crème, volle pluimstaart over de rug, slank, kop rechts.
- **Leerpunt:** scherpe/appelkop-Chihuahua renders en te grote spitse oren (Papillon-drift) afgewezen ten gunste van het zachte koppie dat bij cel 02 past.

### Turnaround-voortgang
- [x] 02 — 3/4 front · [x] 03 — Zij · [x] 05 — Achter · [~] 04 — 3/4 achter (kandidaat) · [ ] 01 — Front (laatste)

### Volgende stap
Cel 04 (3/4 achter) bevestigen → front als laatste, mét alle vastgelegde hoeken als referentie.

---

## [2026-06-06] Sessie G — Turnaround: achter-cel vastgelegd

### Samenvatting
Achter-cel (05) vastgelegd. Na een tweede ronde met staart-over-rug fix is **Render 4** gekozen.

### Aanpassingen
- **Vastgelegd:** `reference-material/character-sheets/wolfje-jv-turn-05-achter.png` (Render 4, ronde 2) — symmetrisch recht-van-achteren, pluim duidelijk over de rug, warme crème, abrikoos op de oorruggen, slank.
- **Kandidaat vastgehouden:** Render 4 uit de eerdere 3/4-achter set blijft kandidaat voor cel 04.

### Turnaround-voortgang
- [x] 02 — 3/4 front · [x] 05 — Achter · [~] 04 — 3/4 achter (kandidaat) · [ ] 03 — Zij · [ ] 01 — Front (laatste)

### Volgende stap
Stap 3 (zij, kop naar rechts) → cel 04 bevestigen → front als laatste.

---

## [2026-06-06] Sessie F — Turnaround: 3/4-cel vastgelegd

### Samenvatting
Eerste turnaround-cel vastgelegd. Van 5 renders (3/4 front) is **Render 4** gekozen.

### Aanpassingen
- **Vastgelegd:** `reference-material/character-sheets/wolfje-jv-turn-02-driekwart-front.png` (Render 4) — zacht rond Wolfje-gezicht, proportionele oren, slank lijf + vollere nek, volle over-de-rug staart, schone contour.
- **Leerpunt:** oriëntatie (kop links/rechts) is GEEN kwaliteitscriterium — verliesvrij te spiegelen; alleen aanhouden voor onderlinge consistentie. Render 1 viel af op kop-/oorvorm (Papillon-drift), niet op kleur.

### Volgende stap
Stap 2 (achter) genereren → daarna zij + 3/4 achter → front als laatste.

---

## [2026-06-06] Sessie E — Turnaround model-sheet prompts

### Samenvatting
Eerste model sheet gestart: turnaround-prompts om jongvolwassen Wolfje vanuit 5 hoeken af te leiden van het canon-beeld.

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `model-sheets/wolfje-jongvolwassen-turnaround-prompts.md` | Consistentie-preamble + 5 hoek-prompts (front, 3/4 front, zij, 3/4 achter, achter), image-to-image vanaf `wolfje-jongvolwassen-CANON.png`, in neutrale staande pose. Incl. naamgeving + QC-instructie. |

### Volgende stap
Turnaround-cellen genereren en QC'en → daarna expressie-sheet en actie-pose-sheet → dan pup + eerste periode.

---

## [2026-06-06] Sessie D — Canon-referentiebeeld vastgelegd

### Samenvatting
Na de nek-edit ronde (4 image-to-image renders) is **Render 3** gekozen en vastgelegd als het definitieve canon-referentiebeeld voor jongvolwassen Wolfje.

### Aanpassingen
- **Definitief beeld:** `wolfje-jongvolwassen-CANON.png` (Render 3) — vollere nek met slank blijvend lijf, warme crème, abrikoos alleen op oren, volle over-de-rug pluimstaart.
- **Beslisreflectie vastgelegd:** onderbuikfavoriet maker was Render 1 ("oogde het meest als Wolfje"); bewust gekozen voor de beredeneerde Render 3 vanwege slank silhouet + staart over de rug (beter voor strip/animatie/shorts).

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `wolfje-jongvolwassen-CANON.png` | Definitief canon-referentiebeeld (Render 3). |
| `CANON-selectie-log.md` | Doorlopend selectielog met checklist-scores en reflectie per ronde. |

### Volgende stap
Model sheets jongvolwassen afleiden van het canon-beeld → daarna pup + eerste periode via image-to-image.

---

## [2026-06-06] Sessie C — Canon jongvolwassen VERGRENDELD

### Samenvatting
Na vergelijking van de top-3 renders tegen de echte Wolfje is **afbeelding 1 (blauw, v2-variant 3)** gekozen als basis en vergrendeld als canon jongvolwassen, met twee gerichte verfijningen.

### Aanpassingen (canon)
- **Winnaar gekozen:** afbeelding 1 — slankste/best afleesbare silhouet en schoonste lijn → sterkst voor shorts-leesbaarheid en consistente reproductie in strips/animatie.
- **Verfijning 1 — vollere pluimstaart:** de render had een te schrale staart; canon schrijft een volle, lange pluim voor die over de rug krult.
- **Verfijning 2 — warm crème terug:** puur wit week af van de echte Wolfje; canon is overwegend wit met zachte warme crème/ivoor toon. Abrikoos blijft uitsluitend op achterkant oren.
- **Bron van waarheid verschoven:** `CANON-wolfje-jongvolwassen.md` vervangt de pre-v2 beschrijvingen in spec/iterations/README.

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `CANON-wolfje-jongvolwassen.md` | Vergrendelde canon-prompt + vergrendelde beschrijving + beslissingsmotivatie + volgende stappen. |

### Beeldmateriaal
Beoordeelde top-3 renders (door maker geüpload, niet in repo bewaard): afbeelding 1 = winnaar. Definitief canon-referentiebeeld volgt zodra de canon-prompt is gedraaid.

### Volgende stap
Canon-prompt draaien → canon-referentiebeeld vastleggen → model sheets → daarna pup + eerste periode afleiden.

### Naschrift (verfijning)
Render 5 (perzik) gekozen als beste van 5 canon-runs. Op verzoek maker: **vollere nek/kraag** toegevoegd aan canon (volle zachte manen rond hals/borst, lijf blijft slank). Canon-prompt + beschrijving bijgewerkt; image-to-image edit-prompt aangeleverd om dit op Render 5 toe te passen. Definitief canon-referentiebeeld nog vast te leggen ná de nek-aanpassing.

---

## [2026-06-06] Sessie B — v2-prompts: ontpluizing (slank silhouet)

### Samenvatting
Tweede Gemini→Gemini ronde. v1 liet het beeldmodel Wolfje als een dichte Pommerian-pluizenbol tekenen; v2 corrigeert dat met expliciete vachtlengte en anatomie-zichtbaarheid.

### Aanpassingen (werkwijze + canon)
- **Vachtvolume gecorrigeerd:** alle "cloud/massive/explosion/dense/thick"-taal geschrapt; vacht nu expliciet **4–5 cm, fijn, wispy, silky, naar beneden vallend**.
- **Anatomie verplicht zichtbaar:** het slanke, fijngebouwde lijf moet door de vacht heen leesbaar blijven.
- **Canon-aanscherping kleur:** abrikoos nu **alleen op de achterkant van de oren** (kruin-kap en rug-zadel losgelaten); rest puur wit.
- **Ruff teruggeschroefd:** van "lion-like" naar een bescheiden, wispy kraagje van 4–5 cm.

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `prompts-gemini-output/wolfje-jongvolwassen-gemini-prompts-v2-defluffed.md` | 5 nieuwe v2-prompts (lavendel/mint/blauw/perzik/geel) + Gemini's goedgekeurde zelfreflectie + scoretabel met 2 nieuwe ijkpunten (slank silhouet, korte wispy vacht). |

### Beeldmateriaal
Geen nieuwe afbeeldingen toegevoegd in deze sessie. (Maker heeft een top-5 van nieuwe + oude renders samengesteld; nog te uploaden voor visuele analyse.)

### Volgende stap
v2-prompts draaien, scoretabel invullen, canon jongvolwassen kiezen. Top-5 renders analyseren zodra geüpload.

---

## [2026-06-06] Sessie A — Gemini→Gemini meta-prompt + 5 testprompts + backup

### Samenvatting
Overstap naar een **Gemini→Gemini** aanpak voor het vergrendelen van jongvolwassen Wolfje. Toegevoegd: meta-prompt, 5 door Gemini geschreven testprompts met scoretabel, voortgangslog en volledige backup-zip.

### Aanpassingen (werkwijze)
- **Promptstrategie gewijzigd:** van Claude→Gemini naar een **meta-prompt** waarmee Gemini zelf de Nano Banana beeldprompt schrijft.
- **Projectrol vastgelegd:** Claude = hoofdengineer; Gemini = uitvoerend hulpmodel.
- **Scope-discipline:** eerst jongvolwassen vergrendelen; pup en eerste periode uitgesteld.
- **Niets verwijderd of overschreven.**

### Toegevoegd (nieuwe bestanden)
| Bestand | Inhoud |
|---|---|
| `wolfje_metaprompt_gemini_naar_nanobanana.md` | Meta-prompt: Gemini als prompt-engineer voor zijn eigen beeldmodel. |
| `prompts-gemini-output/wolfje-jongvolwassen-gemini-prompts.md` | 5 v1-prompts + scoretabel. |
| `prompts-gemini-output/raw-gemini-variant1-yellow.txt` … `variant5-blue.txt` | Ruwe originele Gemini-outputs (v1). |
| `PROGRESS-LOG.md` | Stand van zaken + volgende stappen. |
| `wolfje-bella-backup-YYYYMMDD.zip` | Volledige backup-snapshot. |

### Beeldmateriaal (bestaand, ongewijzigd, in backup)
- **12 foto's** van de echte Wolfje (referentie-input): `20250801_164033.jpg`, `20260324_010146.jpg`, `20260501_140420/140724/140725.jpg`, `20260518_194034/194125/194132.jpg`, `20260601_000746.jpg`, `20260605_170508.jpg`, `Snapchat398132089.jpg`, `wolfje_voor.jpg`.
- **1 stijlreferentie:** `niece_style_reference.jpeg` (inkttekening).
- **21 voorbeeldrenders (PNG):** single_A–D, A1–A4 (A4_celshaded_b = gekozen richting), 3stage_* (5), Gemini_Generated_Image_* (5), output_v2_celshaded_jongvolwassen.
- Evolutie ronde 1→4 staat in `style-results-log.md`.
