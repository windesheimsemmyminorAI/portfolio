# Checklist ingebruikname — Control Tower dashboard

Afvinkbare versie van de openstaande actiepunten uit het
[overdrachtsdocument](overdrachtsdocument.md) (hoofdstuk 8). Loop deze in volgorde af
voordat het dashboard productie draait.

## Direct na overdracht

- [ ] **Gmail-credential aanmaken** in n8n (Credentials → nieuwe "Gmail OAuth2 API").
- [ ] **Inloggen** met het Google-account van `indy@bajo-bouw.nl`.
- [ ] **Credential koppelen** aan de node "Stuur dashboard e-mail" (vervangt de placeholder
      `VERVANG_MET_NIEUW_CREDENTIAL_ID`).
- [ ] **Testen** via de trigger "Handmatig testen" — controleer of de e-mail aankomt (let op spam).
- [ ] **Workflow op "active" zetten** (schakelaar rechtsboven in de editor) zodra de test slaagt.

## Optioneel: opruimen

- [ ] **n8n-tag bijwerken** van `v11` naar `v14` (of een notitie toevoegen die naar
      `versiedocumentatie.md` verwijst), zodat de versienaam in n8n overeenkomt met de inhoud.

## Na enkele weken productiedraaien

- [ ] **`doelAutomatisch`** (nu 60) in "Bereken KPI's" herzien op basis van echte data.
- [ ] **`confKleur`-grenzen** (groen vanaf 90%, oranje vanaf 75%) in "Bouw dashboard HTML" kalibreren.
- [ ] **`heatmapMax`** (nu 8 leveranciers) en de aandachtslijst-limiet (nu 10) afstemmen op de
      omvang van het werkelijke leveranciersbestand.

## Organisatorisch

- [ ] **Beheerder aanwijzen** voor toekomstig onderhoud van de Code-nodes (vereist JavaScript-kennis).
- [ ] **Toegang borgen:** n8n-omgeving, het Google-account achter de Sheets-credential, en het
      account achter de Gmail-credential.
