from pythonfiler.oppg3 import *
from pythonfiler.oppg4 import *
from pythonfiler.oppg5 import *
from pythonfiler.oppg6 import *
from pythonfiler.oppg7 import *
from utils import *
velkommen_melding()

#oppgave 1, 2 og 3 kjøres på forhånd med instruksjon fra readme-fil
teaterstykke = input("Hvilket stykke ønsker du å se (K/S)? ")
teaterstykke, scene = convert_input(teaterstykke)
print(f"Her er en oversikt over dato og tidspunkt vi viser {teaterstykke}")
list_opp_forestillinger(teaterstykke)

dato= input("Hvilken dato? ")
while not validate_date(dato):
    print("Ugyldig dato, prøv igjen.")
    dato= input("Hvilken dato? ")
    

tid = input("Hvilken tid? ")
while not validate_time(tid):
    print("Ugyldig tid, prøv igjen.")
    tid= input("Hvilken tid? ")

antall = int(input("Hvor mange billetter vil du kjøpe? "))

print(f"Her er en oversikt over hvilke rader som har {antall} ledige seter.")
finn_ledige_rader(dato, tid, teaterstykke, antall)

svar10 = input("Hvilket område hvil du sitte i? ")
while not verify_omraade(scene, svar10):
    print("Område finnes ikke i salen du har valgt, prøv igjen.")
    svar10 = input("Hvilket område hvil du sitte i? ")
    
svar9 = input("Hvilken rad vil du sitte i? ")
mobilnr = int(input("Angi mobilnummeret ditt: "))
if sjekk_om_kundeprofil_eksisterer(mobilnr) == False:
    print("Vi ser at du er en ny kunde.")
    navn = input("Vennligst oppgi navnet ditt? ")
    adresse = input("Vennligst oppgi din adresse? ")
    lag_kundeprofil(mobilnr, navn, adresse)
kjop_billetter(svar9, antall, svar10, scene, mobilnr)
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
        
    
        
































