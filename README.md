# Databaseprosjekt V2024 Gruppe 40

## Introduksjon

Dette er vårt prosjekt i TDT4145 Databaser og datamodellering Det følgende er antagelser vi har vært nødt til å gjøre ettersom det ikke var spesifisert godt nok i oppgave beskrivelsen:

- Vi har antatt at Størst av alt har én akt, som vi har kalt _hovedakt_, der alle skuespillere spiller i akten.
- Vi har antatt at alle skuespillere i "Størst av alt er kjærligheten" spiller seg selv
- Etc

## Virkemåte

Vi har valgt å kjøre alle python-filer fra en main-fil som heter main.py. Alle SQL-queries kan bli funnet i _SQLfiler/sql_query.sql_.

Videre har vi satt inn setene som har blitt solgt, og de tilhørende billettene, i _stoler.py_

Resten av innholdet i databasen blir satt inn ved hjelp av _sql_sqript_insert.sql_.

## Komme i gang

For å initialisere databasen kan man kjøre init.bat i terminalen dersom man er på Windows, eller init.sh dersom man er på Linux. Dette scriptet setter in SQL-skjemaet og dataen inn i databasen. I tillegg kjører den stoler.py som leser fra tekstfilene som inneholder hvilke seter som har blitt solgt, og setter inn dataen.

Alternativt kan man selv initialisere databasen ved å kjøre SQL-scriptene:

- sql-sqript-setup.sql
- sql-sqript-insert.sql

Og til slutt python-filen:

- stoler.py
