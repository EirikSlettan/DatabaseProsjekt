# Databaseprosjekt V2024 Gruppe 40

## Introduksjon

Dette er vårt prosjekt i TDT4145 Databaser og datamodellering Det følgende er antagelser vi har vært nødt til å gjøre ettersom det ikke var spesifisert godt nok i oppgave beskrivelsen:

- Vi har antatt at Størst av alt er kjærligheten har én akt, som vi har kalt _hovedakt_, der alle skuespillere spiller i akten.
- Vi har antatt at alle skuespillere i "Størst av alt er kjærligheten" spiller seg selv.
- Vi har gjort om Billettkjop til en svak klasse til kundeprofil.
- Vi har gjort om Billettgruppe til en svak klasse til teaterstykke.
- Vi har lagt til alle skuespillere fra Trøndelag Teater sin nettside. Videre har vi lagt inn aktene med roller etter tabellen nederst i oppgavebeskrivelsen slik at alle skuespillere og roller ikke nødvendigvis vil dukke opp i spørringer. F.eks i oppgave 5 vil Fabian mangle.
- Vi har lagt inn alle spørringer i _sqlfiler/queries.sql_ for at du kan se de. Vi bruker ikke denne filen direkt, men har lagt spørringene inn i python-kode.
- Vi velger å kun gjøre det mulig å kjøpe billetter 3. febraur slik oppgaven spør om. Kan enkelt legge til videre funksjonalitet for å kjøpe andre dager også. Siden oppgaven ikke ber om det, dropper vi det.

## Virkemåte

Vi har valgt å kjøre alle python-filer fra en main-fil som heter main.py. Alle sql-queries kan bli funnet i _sqlfiler/queries.sql_.

Videre har vi satt inn setene som har blitt solgt, og de tilhørende billettene, i _lese_fra_fil.py_

Resten av innholdet i databasen blir satt inn ved hjelp av _insert_known_values.sql_.

## Komme i gang

For å initialisere databasen kan man kjøre init.bat i terminalen dersom man er på Windows, eller init.sh dersom man er på Linux. Dette scriptet setter in sql-skjemaet og dataen inn i databasen. I tillegg kjører den stoler.py som leser fra tekstfilene som inneholder hvilke seter som har blitt solgt, og setter inn dataen.

Alternativt kan man selv initialisere databasen ved å kjøre sql-scriptene:

- schema.sql
- insert_known_values.sql

Og til slutt python-filen:

- lese_fra_fil.py

## Gå gjennom oppgavene

NB: Her har vi lagt ved output du vil få ved å svare slik det står oppgitt i oppgavene.

Etter å ha gjort "Komme i gang", kjører du main.py. Denne gjør følgende:

- Etter å ha initialisert databasen er oppgave 1 og 2 fullført.

- Du vil få en rekke spørsmål knyttet til billettkjøp. Skriv inn ønskede dater.

- Du vil først få spørsmål om du ønsker å se billetter solgt på en valgt dato. Dette er oppgave 4.

- Deretter vil du får spørsmål om å se oppgave 5. Her vil du få ut en tabell med teaterstykke, skuespiller og rolle skuespiller har.

- Deretter vil du får spørsmål om å se oppgave 6. Her vil du få en tabell med alle forestillinger rangert fra den som har solgt mest til minst.

- Til slutt vil du få spørsmål om du ønsker å se oppgave 7. Skriv inn den skuespilleren du ønsker å se alle skuespillerkollegaene til, og du får deretter opp det.