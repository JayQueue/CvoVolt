"""
Auteur: Jonathan Quartier
Datum: 10/9/2024
Workshop 1: Opdracht 4
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_1/opdracht_4.py 
"""
import opdracht_4_module as geometrie

menu = [
    "1. Oppervlakte van een rechthoek",
    "2. Omtrek van een rechthoek",
    "3. Omtrek van een cirkel",
    "4. Oppervlakte van een vierkant"
]

def toon_menu():
    for menuitem in menu:
        print(menuitem)

def main():
    while True:
        toon_menu()
        keuze = int(input("\nWelke actie wil je uitvoeren? "))
 
        match keuze:
            case 1:
                lengte = float(input("Voer de lengte van de rechthoek in: "))
                breedte = float(input("Voer de breedte van de rechthoek in: "))
                resultaat = geometrie.oppervlakte_rechthoek(lengte, breedte)
                print(f"De oppervlakte van de rechthoek is: {resultaat}")

            case 2:
                lengte = float(input("Voer de lengte van de rechthoek in: "))
                breedte = float(input("Voer de breedte van de rechthoek in: "))
                resultaat = geometrie.omtrek_rechthoek(lengte, breedte)
                print(f"De omtrek van de rechthoek is: {resultaat}")

            case 3:
                straal = float(input("Voer de straal van de cirkel in: "))
                resultaat = geometrie.omtrek_cirkel(straal)
                print(f"De omtrek van de cirkel is: {resultaat}")

            case 4:
                zijde = float(input("Voer de zijde van het vierkant in: "))
                resultaat = geometrie.oppervlakte_vierkant(zijde)
                print(f"De oppervlakte van het vierkant is: {resultaat}")

            case 5:
                print("Programma wordt afgesloten.")
                break

            case _:
                print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    main()
