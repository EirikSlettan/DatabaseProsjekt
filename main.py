from pythonfiler.oppg7 import  *
from pythonfiler.oppg3 import *
from pythonfiler.oppg4 import *
from pythonfiler.oppg5 import *
from utils import *
from pythonfiler.oppg6 import *
velkommen_melding()

#oppgave 1, 2 og 3 kjøres på forhånd med instruksjon fra readme-fil
svar3 = input("Hvilket stykke ønsker du å se (Kongsemnene/Størst av alt er kjærligheten)? ") 
print(f"Her er en oversikt over dato og tidspunkt vi viser {svar3}")
list_opp_forestillinger(svar3)
svar4= input("Hvilken dato? ")
svar5 = input("Hvilken tid? ")
svar6 = int(input("Hvor mange billetter vil du kjøpe? "))
print(f"Her er en oversikt over hvilke rader som har {svar6} ledige seter.")
finn_ledige_rader(svar4, svar5, svar3, svar6)
svar10 = input("Hvilket område hvil du sitte i? ")
svar9 = input("Hvilken rad vil du sitte i? ")
kjop_billetter(svar9, svar6, svar10, "Hovedscenen", 47519574)
print("Billetter er kjøpt!")

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
































