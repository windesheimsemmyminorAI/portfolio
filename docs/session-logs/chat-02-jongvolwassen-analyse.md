# Sessie-logboek — Chat 02: "Analyse geslachtskenmerken Wolfje afbeeldingen"

**Datum:** 6 juni 2026 (laatste update 11:28)
**Chat-link:** https://claude.ai/chat/d475a45f-2e0d-4011-ac93-ce57a50d75ce
**Fase:** Phase 0 — jongvolwassen-verfijning · **Ronde:** 5 (vervolg op de geplande canon-ronde 4)
**Beeldgeneratie:** Semmy (Gemini / Nano Banana)

> Vervolg op chat 1. Hier wordt de cel-shaded richting bijgestuurd richting een canon-waardig jongvolwassen-beeld.

---

## 1. Aanleiding

De recente renders lazen te **"kawaii"/vrouwelijk**: te grote ogen, te bolrond lijf, en een bijna-witte vacht waarin Wolfjes abrikoos-aftekening verdween. Semmy vroeg expliciet om **eerst de echte foto's grondig te analyseren** vóór er nieuwe prompts geschreven werden.

## 2. Fotoanalyse (vastgelegd in `wolfje-jongvolwassen-analyse-en-4-prompts.md`)

Gedetailleerde beschrijving van gezicht (overwegend wit, brede witte bles, zachte bleke abrikoos uitsluitend op kruin + achterkant/punten van de oren, donkere ogen op natuurlijk formaat, korte fijne vosachtige snuit) en lichaam (fijn gebouwd, crème/wit, warme abrikoos-"zadel" over rug, witte borst/poten, leeuwachtige kraag, "broek"-bevedering, pluimstaart over de rug, slankere jongvolwassen bouw).

**Vier oorzaken van het "te vrouwelijke":** ogen te groot/rond · silhouet te bolrond · vacht bijna helemaal wit (zadel weg) · blik te zoet.

## 3. Vier test-prompts (zelfde stijl, andere formulering)

Met identieke cel-shaded stijlregel, maar elk een andere strategie om Wolfjes kenmerken te beschrijven:
- **A — Anatomisch-precies** (kleur strikt per lichaamszone)
- **B — Negatieve sturing** (expliciet wegsturen van kawaii/te zoet)
- **C — Holistisch** (silhouet + karakter i.p.v. micro-details)
- **D — Referentie-verankerd** (verhoudingen als ground truth tegen rasdrift)

Doel: via vergelijking de best wérkende formulering vinden → basis voor het canon-beeld.

## 4. Analyse van de v2-output → prompt v3

Semmy deelde een gegenereerde cartoon-output (`output_v2_celshaded_jongvolwassen.png`) en merkte op dat de kwaliteit overall leek te regresseren terwijl details verbeterden. Claude analyseerde tegen de echte foto's:

**Wat GOED ging (behouden):** ogen op natuurlijk formaat · rustige zelfverzekerde gesloten-bek-glimlach · slankere jongvolwassen bouw · witte bles/borst/poten · vosachtige snuit + klein donker neusje · consistente cel-shaded stijl.

**Wat FOUT ging (gecorrigeerd in v3):**
1. Abrikoos te uitgebreid/verzadigd — vrijwel een abrikoos-"deken" over kop én rug i.p.v. overwegend wit.
2. Pluimstaart hangt laag aan de zijkant i.p.v. omhoog over de rug (Wolfjes signatuur).
3. Beenbevedering ("broek") verdwenen — poten te glad/vlak.
4. Vacht te plat/vector-achtig i.p.v. zachte gevederde langharige cel-shading.

**Vermoedelijke oorzaak:** de vorige prompt stuurde te sterk op "lean / not fluffy / natural eyes" en **overcorrigeerde** zo de vacht. v3 herstelt de balans met expliciete **KEEP**- en **FIX**-blokken + noodgrepen voor hardnekkige afwijkingen (volledige prompt in `wolfje-jongvolwassen-prompt-v3.md`).

## 5. Inzichten / leeruitkomsten

- **Eerst analyseren, dan prompten:** de fotoanalyse vóór het schrijven voorkwam giswerk.
- **Overcorrectie is een reëel risico:** een fix voor het ene probleem (te bolrond) brak een ander (vacht/staart). KEEP/FIX-annotaties maken expliciet wat behouden moet blijven.
- **Abrikoos blijft het hardnekkigste punt** — strak begrenzen (alleen oor-achterkant + lichte kruin), met noodgreep "faintest warm beige hint".

## 6. Gekoppelde bestanden (deze chat)

- `wolfje-jongvolwassen-analyse-en-4-prompts.md` (fotoanalyse + 4 prompts)
- `wolfje-jongvolwassen-prompt-v3.md` (gecorrigeerde v3 met KEEP/FIX + noodgrepen)
- Beeld: `reference-material/style-results/round-5/output_v2_celshaded_jongvolwassen.png` (de geanalyseerde output)
- Referentie: 4-foto-subset uit `reference-material/source-photos/` (front + profiel-closeup + lichaamsfoto + jongere vergelijkingsfoto)
