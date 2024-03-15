from pythonfiler.oppg7 import  *
from pythonfiler.oppg3 import *
from pythonfiler.oppg4 import *
from pythonfiler.oppg5 import *
from utils import *
from pythonfiler.oppg6 import *

velkommen_melding()

#oppgave 1, 2 og 3 kjøres på forhånd med instruksjon fra readme-fil 
list_opp_forestillinger()
svar = input("a")
finn_ledige_rader("2024-02-03", "18:30:00", "Storst av alt er kjaerligheten", 9)


#oppgave 4:
melding = "Hvilken dato ønsker du å sjekke antall solgte billetter til alle forestillingene som vises denne dagen? Svar på formatet: (YYYY-MM-DD): "
dato = input(melding)
while not validate_date(dato):
    print("Ikke en gyldig dato")
    dato = input(melding)
finn_forestillinger(dato)

#oppgave 5
melding = "Ønsker du å se oppgave5 (Y/N)?: "
svar5 = input(melding).upper()
svar5 = validate_input(svar5, melding )
if svar5 == "Y":
    finn_navn_skuespillere()
else:
    print("Det var synd, vi har jobbet masse med den :(")

#oppgave 6
melding = "Ønsker du å se oppgave6 (Y/N)?: "
svar6 = input(melding).upper()
svar6 = validate_input(svar6, melding)
if svar6 == "Y":
    finn_billetter_solgt()
else:
    print("Hæ? Anbefaler å se den!")

#oppgave 7
melding = "Ønsker du å se oppgave7 (Y/N)?: "
svar7 = input(melding).upper()
svar7 = validate_input(svar7, melding)
if svar7 == "Y":
    skuespiller = input("Yes! Hvilken skuespiller vil du se ALLE skuespillerkollegaene til? ")
    find_colleagues(skuespiller)
    print("NB: Ser du en tom tabell har du antageligvis skrevet deres FULLE(!) navn feil")
else:
    print("Det er vår beste oppgave!")  
































