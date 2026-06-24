# Node-documentatie — Control Tower n8n-workflow

Diepgaand overzicht van de zeven nodes in de Control Tower-dashboardworkflow
(`v11_control_tower_email_overdracht.json`). Afgeleid uit de workflow-JSON zelf.

> **Let op:** dit bestand documenteert de **n8n-workflow-nodes**. De `NODE_DOCUMENTATIE.md`
> in de hoofdmap documenteert de losse Python-uitwerking (`scripts/verwerk_facturen.py`) en
> wordt automatisch gegenereerd. Dit bestand is handmatig en specifiek voor de n8n-workflow.

Voor de volledige context (waarom-keuzes, FAQ, openstaande actiepunten) zie het
[overdrachtsdocument](overdrachtsdocument.md), hoofdstuk 4.

## De keten in één oogopslag

```
Elke maandag 05:00 ─┐
                    ├──▶ Haal fouten op ──▶ Haal facturen op ──▶ Bereken KPI's ──▶ Bouw dashboard HTML ──▶ Stuur dashboard e-mail
Handmatig testen  ─┘
```

| # | Node | n8n-type | Rol |
|---|------|----------|-----|
| 1a | Elke maandag 05:00 | `scheduleTrigger` | Automatische start (ma 05:00, Europe/Amsterdam) |
| 1b | Handmatig testen | `manualTrigger` | Handmatige teststart |
| 2 | Haal fouten op | `googleSheets` | Leest tabblad "Validatiefouten" |
| 3 | Haal facturen op | `googleSheets` | Leest tabblad "Verwerkte facturen" |
| 4 | Bereken KPI's | `code` (JS) | Filtert op week + rekent KPI's/signalen uit |
| 5 | Bouw dashboard HTML | `code` (JS) | Bouwt de mail-veilige HTML |
| 6 | Stuur dashboard e-mail | `gmail` | Verstuurt de e-mail |

---

## 1a. Elke maandag 05:00 — `scheduleTrigger`

Automatische trigger op een wekelijks interval: maandag (`triggerAtDay = [1]`) om 05:00
(`triggerAtHour = 5`), tijdzone Europe/Amsterdam.

- **Input:** geen (beginpunt).
- **Output:** lege trigger → "Haal fouten op".
- **Faalt als:** de workflow op `active = false` staat — dan vuurt de trigger niet.

## 1b. Handmatig testen — `manualTrigger`

Knop in de n8n-editor om de hele keten direct te draaien, zonder configuratie.

- **Input:** geen.
- **Output:** lege trigger → "Haal fouten op".
- **Let op:** draaien verstuurt ook daadwerkelijk een e-mail.

## 2. Haal fouten op — `googleSheets`

Leest **alle** rijen uit tabblad "Validatiefouten".

- **documentId:** `1Mwl2_tiohh5s_vaXaL6cJjiZbHevHQeeU_qKIpFHttk`
- **sheetName:** `gid=754329244` ("Validatiefouten")
- **Credential:** Google Sheets OAuth2 API (`EXKuWy0KsFqaf0Ln`)
- **Faalt als:** de credential verloopt of het tabblad/gid wijzigt → de hele workflow stopt.

## 3. Haal facturen op — `googleSheets`

Leest **alle** rijen uit tabblad "Verwerkte facturen".

- **documentId:** `1Mwl2_tiohh5s_vaXaL6cJjiZbHevHQeeU_qKIpFHttk`
- **sheetName:** `gid=0` ("Verwerkte facturen")
- **Credential:** dezelfde Google Sheets OAuth2 API (`EXKuWy0KsFqaf0Ln`)
- **Node-volgorde:** bewust ná "Haal fouten op" gezet; "Bereken KPI's" haalt beide bij naam op
  (`haalOp()`), zodat een verwisseling geen KPI's op 0 zet. Zie overdrachtsdocument §4.4.

## 4. Bereken KPI's — `code` (JavaScript)

Het rekenhart. Filtert op de vorige kalenderweek en aggregeert alles tot één output-item.
Drempelwaarden staan hard in de code: `doelAutomatisch = 60`, `heatmapMax = 8`, top-5 (KPI 3),
top-10 (aandachtslijst).

- **Input:** data van node 2 + 3 (via `haalOp(naam)`).
- **Output:** één item met alle tellingen, gemiddelden, percentages en lijsten.
- **Faalt stilletjes als:** kolomnamen in de Sheets-log wijzigen → kengetallen blijven op 0
  zonder foutmelding. Zie de kolomreferentie hieronder.

## 5. Bouw dashboard HTML — `code` (JavaScript)

Zet het KPI-item om in mail-veilige HTML (tabel-layout, inline styling). Bevat de lege-weekmodus
(`legeWeek`), de voetnoten bij afgekapte lijsten en de KPI 1-balkkleurlogica.

- **Input:** het ene item van "Bereken KPI's".
- **Output:** één item met `html`, `subject`, `periodeLabel`.
- **Faalt als:** een veldnaam in "Bereken KPI's" wijzigt zonder dat deze node meegaat.

## 6. Stuur dashboard e-mail — `gmail`

Verstuurt de HTML-e-mail.

- **sendTo:** `indy@bajo-bouw.nl`
- **subject:** `={{ $json.subject }}` (expressie!)
- **message:** `={{ $json.html }}` (expressie!)
- **Credential:** Gmail OAuth2 API - indy@bajo-bouw.nl — **nog aan te maken**
  (placeholder `VERVANG_MET_NIEUW_CREDENTIAL_ID`, zie overdrachtsdocument §8.1).
- **Faalt als:** de credential ontbreekt/verloopt → alleen deze stap faalt, de berekeningen zijn al klaar.

---

## Verwachte Sheets-kolommen (kolomreferentie)

"Bereken KPI's" verwacht exact deze kolomnamen. Wijzigen de kolommen in de inkoopfacturatie-automatisering,
dan moet de Code-node mee — anders blijven kengetallen stilletjes op 0 staan.

### Tabblad "Verwerkte facturen" (gid=0)

| Kolom | Gebruikt voor |
|-------|---------------|
| `verwerktOp` | Weekfilter (welke facturen vallen in de vorige kalenderweek) |
| `factuurnummer` | Aandachtslijst (compound key met leveranciernaam) |
| `leveranciernaam` | Leveranciers-set, heatmap (KPI 2), aandachtslijst |
| `validatieResultaat` | PASS/REVIEW/FATAL-verdeling, KPI 1 |
| `totaalbedrag` | Totaal incl. btw, aandachtslijst-sortering |
| `btwbedrag` | BTW-totaal |
| `betaalbaarBedrag` | Betaalbaar totaal |
| `aantalRegels` | Aantal factuurregels |
| `ibanAfwijking` | Risicosignaal IBAN-afwijking (bool) |
| `nieuweOnbekendeLeverancier` | Risicosignaal nieuwe leverancier (bool) |
| `betrouwbaarheidIsLaag` | Risicosignaal lage betrouwbaarheid (bool) |
| `technischResultaat` | KPI 4 (UBL PASS/REVIEW/FATAL) |
| `aantalTechnischeFouten` | KPI 4 totaal technische fouten |
| `documentConfidence` | Gem. OCR-betrouwbaarheid |
| `leverancierConfidence` | Gem. leveranciersmatch, heatmap (KPI 2) |
| `leverancierUniekGematcht` | % uniek gematcht (bool) |
| `leverancierMatchMethode` | Matchmethode-samenvatting (btw/kvk/iban/naam/geen) |
| `percentageRegelsZonderGl` | Gem. % regels zonder grootboekcode |
| `aantalOmgerekend` | Eenheden omgerekend |
| `aantalGeflagd` | Regels ter review |
| `aantalNietVanToepassing` | Geen omrekening |

### Tabblad "Validatiefouten" (gid=754329244)

| Kolom | Gebruikt voor |
|-------|---------------|
| `verwerktOp` / `foutdatum` / `datum` | Weekfilter (een van de drie volstaat) |
| `foutcode` | Groepering top-5 (KPI 3) |
| `severity` | Ernst (FATAL/REVIEW/ONBEKEND), zwaarste wordt bijgehouden |
| `omschrijving` | Voorbeeldtekst bij de foutcode |
