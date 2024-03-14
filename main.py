from Pythonfiler.oppg7 import  *
from Pythonfiler.finn_forerstillinger_fra_dato import *
from Pythonfiler.finn_navn_skuespillere import *
from Pythonfiler.billetter_solgt import *
from Pythonfiler.utils import *


bredde = 56
bredde2 = 15
tegn = "-"
print("-" *bredde)
print(f"{tegn*bredde2}VELKOMMEN TIL VÅRT TEATER!{tegn*bredde2}")
print("-"*bredde)


#oppgave 1, 2 og 3 kjøres på forhånd med instruksjon fra readme-fil 

#oppgave 4:

dato = input("Hvilken dato ønsker du å sjekke antall solgte billetter til alle forestillingene som vises denne dagen? Svar på formatet: (YYYY-MM-DD): ")
finn_forestillinger(dato)

#oppgave 5
svar5 = input("Ønsker du å se oppgave5 (Y/N)?: ").upper()

if svar5 == "Y":
    finn_navn_skuespillere()
else:
    print("Det var synd, vi har jobbet masse med den :(")


#oppgave 6
svar6 = input("Ønsker du å se oppgave6 (Y/N)?: ").upper()

if svar6 == "Y":
    finn_billetter_solgt()
else:
    print("Hæ? Anbefaler å se den!")

#oppgave 7

svar7 = input("Ønsker du å se oppgave7 (Y/N)?: ").upper()

if svar7 == "Y":
    skuespiller = input("Yes! Hvilken skuespiller vil du se ALLE skuespillerkollegaene til? ")
    find_actor(skuespiller)
    print("NB: Ser du en tom tabell har du antageligvis skrevet deres FULLE(!) navn feil")
else:
    print("Det er vår beste oppgave!")  
































