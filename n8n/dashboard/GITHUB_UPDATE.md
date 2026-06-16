# GitHub-update — Iteratie 8 (weekrapport e-mail)

> ✅ **Toegepast.** Deze instructies zijn uitgevoerd: `v8_email_weekrapport.json`
> staat in de repo, en `README.md` + `versiedocumentatie.md` zijn bijgewerkt met
> iteratie 8. Dit bestand blijft als historisch overdrachtsdocument staan.

Deze update voegt iteratie 8 van het dashboard toe aan je repo.

## 1. Bestand plaatsen

Kopieer `v8_email_weekrapport.json` naar je dashboard-map:

```
portfolio/n8n/dashboard/v8_email_weekrapport.json
```

(Naast je bestaande `v1_...` t/m `v7_email_kpi.json`.)

## 2. Regel toevoegen aan `dashboard/README.md`

Voeg in de bestandentabel deze regel toe, onder de v7-regel:

```
| `v8_email_weekrapport.json` | 8 | Verbreed KPI-dashboard, wekelijks (ma 05:00), samengevat per factuurdatum-week |
```

En werk, als die er staat, de zin over "de twee huidige versies" bij: de huidige e-mailversie is nu **v8**.

## 3. Sectie toevoegen aan `dashboard/versiedocumentatie.md`

Plak dit blok onderaan, na iteratie 7:

```markdown
## Iteratie 8 — Weekrapport met verbrede KPI's

**Bestand:** `v8_email_weekrapport.json`

**Wat het is:** De e-mailversie is fors verbreed en omgezet naar een wekelijks
rapport. Het dashboard leest nog steeds de twee tabbladen "Verwerkte facturen"
en "Validatiefouten", maar gebruikt nu het rijkere schema van de nieuwe
inkoopfacturatie-workflow (Mistral-extractie).

**Wat er nieuw is:**
- Risicosignalen-blok (IBAN-afwijking, nieuwe/onbekende leverancier, lage
  AI-betrouwbaarheid, technische UBL-fouten) — vervangt de weggevallen risicoscore.
- KPI 4 — Technische factuurkwaliteit (UBL): percentage technisch valide facturen.
- Kwaliteitsrij: gemiddelde OCR-betrouwbaarheid, gemiddelde leveranciersmatch,
  percentage uniek gematcht, percentage regels zonder grootboekrekening,
  eenheidsnormalisatie en een samenvatting van de matchmethode.
- KPI 2 toont nu ook de gemiddelde matchbetrouwbaarheid per leverancier;
  KPI 3 toont het type fout (FATAL/REVIEW); een lijst "Facturen die aandacht vragen".

**Wekelijks rapport:** De handmatige trigger is vervangen door een Schedule
Trigger die elke maandag om 05:00 (Europe/Amsterdam) draait. Het dashboard vat
de vorige kalenderweek (maandag t/m zondag) samen, gefilterd op **factuurdatum**.
De validatiefouten worden via het factuurnummer aan diezelfde set facturen
gekoppeld. De periode staat in de header en in het e-mailonderwerp. Een
handmatige test-trigger blijft beschikbaar.

**Waarom deze aanpak:** De opdrachtgever wil één wekelijks overzicht in plaats
van een losse weergave. Filteren op factuurdatum sluit aan op hoe de
administratie naar een week kijkt (de facturen van die week), niet op het
toevallige moment van verwerken.

**Aandachtspunt:** Bij weinig facturen in een week worden percentages in KPI 2
en de gemiddelde-confidence-cijfers grof (bij één factuur 0% of 100%). De
absolute aantallen ernaast houden het interpreteerbaar.
```

## 4. Committen en pushen

### GitHub Desktop
1. Open GitHub Desktop — je ziet de gewijzigde/nieuwe bestanden links.
2. Summary: `Iteratie 8 — wekelijks weekrapport-dashboard op factuurdatum`
3. Description (optioneel):
   ```
   - v8_email_weekrapport.json toegevoegd
   - Schedule trigger maandag 05:00, samenvatting vorige kalenderweek
   - Filter op factuurdatum, fouten gekoppeld via factuurnummer
   - Verbrede KPI's: risicosignalen, technische kwaliteit, datakwaliteit
   - README en versiedocumentatie bijgewerkt
   ```
4. **Commit to main** → **Push origin**

### Of via de terminal
```
cd portfolio
git add n8n/dashboard/v8_email_weekrapport.json n8n/dashboard/README.md n8n/dashboard/versiedocumentatie.md
git commit -m "Iteratie 8 — wekelijks weekrapport-dashboard op factuurdatum"
git push
```

## 5. In n8n
Importeer `v8_email_weekrapport.json` (drie puntjes → Import from File) en zet de
workflow op **Active**, anders vuurt de maandag-trigger niet. Test eventueel
eerst via de knop "Handmatig testen".
