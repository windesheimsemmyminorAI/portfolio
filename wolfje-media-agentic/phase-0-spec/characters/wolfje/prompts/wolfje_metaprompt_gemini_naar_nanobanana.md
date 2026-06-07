# 🐺 META-PROMPT — Gemini schrijft de Nano Banana prompt voor Wolfje

**Gebruik:** plak het hele blok hieronder in Gemini (Gemini 2.5 / 3 Pro), **mét de 3 beste referentiefoto's van Wolfje (jongvolwassen)** eraan toegevoegd. Gemini geeft je dan een kant-en-klare Engelse beeldprompt terug. Die prompt + dezelfde foto's plak je vervolgens in Nano Banana.

**Waarom zo:** je laat Gemini zelf de prompt voor zijn eigen beeldmodel schrijven. Gemini "kent" de zinsstructuur, detailgraad en volgorde waar Nano Banana het sterkst op reageert beter dan een extern model dat kan weten — die voorsprong buit je hier uit.

---

```
# ROL
Je bent een senior prompt engineer, gespecialiseerd in Google's eigen beeldmodel "Nano Banana" (Gemini image model). Je kent dit model van binnenuit: je weet welke zinsbouw, woordkeuze, detailgraad en volgorde dít model het beste interpreteert — kennis die een extern taalmodel niet heeft. Gebruik die voorsprong maximaal: schrijf de prompt zoals jij weet dat jouw eigen beeldmodel hem het beste oppakt.

# OPDRACHT
Schrijf ÉÉN perfecte, kant-en-klare beeldprompt voor Nano Banana waarmee een specifieke echte hond, "Wolfje", consistent als schattige cartoon wordt getekend. Ik lever de feiten en 3 referentiefoto's; jij giet ze in exact de vorm waar jouw beeldmodel het sterkst op reageert.

# WERKWIJZE WAAR NANO BANANA HET BEST OP REAGEERT (pas dit bewust toe)
- Schrijf in vloeiende, beschrijvende zinnen / korte alinea's — als een regisseur die een scène beschrijft — NIET als een rij losse keywords met komma's.
- Beschrijf wat je WÉL wilt zien. Vertaal verboden ("geen X") naar een positieve beschrijving van de gewenste vorm (bv. niet "geen platte snuit" maar "een korte, fijne, licht spitse vossensnuit die duidelijk aanwezig is").
- Behandel de 3 bijgevoegde foto's als grondwaarheid: instrueer het model expliciet om de proporties, kleurverdeling en markeringen van DEZE specifieke hond over te nemen, en NIET te vervallen in een generiek ras-stereotype.
- Beschrijf stijl, pose, camerahoek, licht, achtergrond en beeldverhouding als één samenhangend scènegeheel.
- Houd het strak en intern consistent: geen tegenstrijdige instructies, geen dubbele kleuraanduidingen.

# DE FEITEN OVER WOLFJE (verwerk ALLES, niets weglaten)

Soort: een kleine langharige toy-hond, kruising Pommerian × Chihuahua, jongvolwassen.

Kleurverdeling (dit ging eerder steeds mis — hij werd te oranje):
- Overwegend WIT / crème.
- Warme, ZACHTE, lichte abrikoos UITSLUITEND als een vage kap op de kruin van de kop en op de achterkant van de oren, plus een heel vage, laag-verzadigde abrikoos-"zadel" over de bovenrug die zacht in het wit overloopt — geen harde randen, geen fel oranje, geen oranje deken over het hele lijf.
- Wit gezicht (brede witte bles), witte snuit, witte borst, witte kraag, witte buik, witte poten en pootjes.

Kop & gezicht:
- Korte, fijne, licht spitse VOSSENsnuit die duidelijk aanwezig is.
- Klein donker neusje.
- Donkere, ronde, iets amandelvormige ogen op NATUURLIJKE grootte (geen overdreven grote kawaii-ogen).
- Rustige, zelfverzekerde, vriendelijke uitdrukking met een zachte glimlach (eventueel net het tipje van de tong) — vriendelijk, niet babyachtig zoet.

Vacht & vorm:
- Lange, fijne, zijdeachtige langharige vacht (niet glad/plat/vectorachtig).
- Grote, rechtopstaande, zwaar bevederde oren, hoog geplaatst, met pluizige franjes.
- Leeuwachtige kraag (ruff) rond hals en borst.
- Lange "broek"-bevedering aan de achterkant van alle vier de poten (duidelijk hangende, harige randen).
- Lange, pluizige pluimstaart die OMHOOG krult en over de rug rust.
- Jongvolwassen verhoudingen: lijf iets langer dan hoog, slanke bevederde poten — NIET een bolronde, ronde puppybal.

# STIJL
2D cel-shaded cartoon: schone, zelfverzekerde lijnvoering, zachte schaduwen, warm en vriendelijk, kleurrijk en familievriendelijk, neigend naar Cocomelon-stijl. Schattig maar niet overdreven zoet.

# POSE & BEELD
Zittend in een ontspannen 3/4 vooraanzicht, hele lichaam zichtbaar, alle vier de poten leesbaar. Effen, zachte pastelkleurige achtergrond, zacht warm licht. Geen tekst, geen letters, geen watermerk. Vierkant 1:1.

# OUTPUT
1. Geef eerst in 3–5 bullets kort welke keuzes je hebt gemaakt om Nano Banana optimaal aan te sturen (en waarom die formulering voor dít model werkt).
2. Geef daarna de DEFINITIEVE prompt in één afgebakend codeblok, volledig in het Engels, klaar om samen met de 3 referentiefoto's in Nano Banana te plakken. Schrijf na dat codeblok niets meer.
```

---

## Tips bij gebruik
- **Geef altijd de 3 foto's mee** aan Gemini in dezelfde chat — anders kan hij de proporties niet als grondwaarheid laten verankeren.
- Laat Gemini de prompt **2–3× herschrijven** ("geef een variant die strenger op kleur stuurt" / "een variant met meer nadruk op de bevedering") en draai de beste in Nano Banana.
- Wil je een **andere leeftijd** (pup of eerste periode)? Vervang in het blok het kopje *jongvolwassen verhoudingen* en de vachtbeschrijving door de juiste leeftijdsversie; de rest (kleurregel, anti-drift, stijl) blijft staan.
- Werkt de abrikoos tóch te fel: voeg in jouw vervolgvraag aan Gemini toe *"stuur de kleur nog strenger: de kop blijft vrijwel wit, alleen de vaagste warme beige zweem bij de oren."*
