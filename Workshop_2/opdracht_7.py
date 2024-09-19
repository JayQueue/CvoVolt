"""
Auteur: Jonathan Quartier
Datum: 19/9/2024
Workshop 2: Opdracht 7
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_2/opdracht_7.py 
"""
class Leden:
    def __init__(self, voornaam, naam, categorie):
        self.naam = naam
        self.voornaam = voornaam
        self.categorie = categorie
        if categorie == 1:
            self.lidgeld = 10
        else:
            self.lidgeld = 20

    def toon_gegevens(self):
        print(f"Naam: {self.voornaam} {self.naam}")
        print(f"Categorie: {self.categorie}")
        print(f"Lidgeld: {self.lidgeld}")

    def begroet(self):
        # Op 2 lijnen want lijnlengte is anders > 80
        print(
            f"Welkom {self.voornaam} {self.naam}. " 
            f"Je lidgeld bedraagt {self.lidgeld} euro.\n"
        )
        
jq = Leden("Jonathan", "Quartier" , 1)
jq.toon_gegevens()
jq.begroet()
ss = Leden("Sofie", "Similon", 2)
ss.toon_gegevens()
ss.begroet()
