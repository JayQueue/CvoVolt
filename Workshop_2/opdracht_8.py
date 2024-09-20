"""
Auteur: Jonathan Quartier
Datum: 19/9/2024
Workshop 2: Opdracht 8
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_2/opdracht_8.py 
"""
class Cursus:
    def __init__(self, naam_cursus, type_cursus) -> None:
        self.naam_cursus = naam_cursus
        self.type_cursus = type_cursus
        self.aantal_inschrijvingen = 0

    def print_info(self):
        print(f"De cursus {self.naam_cursus} is een {self.type_cursus} cursus.")

    def verhoog_inschrijvingen(self):
        if self.aantal_inschrijvingen < 18:
            self.aantal_inschrijvingen += 1
            print(f"Aantal inschrijvingen: {self.aantal_inschrijvingen}")
        else:
            print(f"De cursus {self.naam_cursus} zit vol. Je komt op de wachtlijst.")

cursus1 = Cursus("Engels", "taal")
cursus2 = Cursus("Python", "computer wetenschap")
cursus3 = Cursus("Wiskunde", "wetenschap")

cursus1.print_info()
cursus2.print_info()
cursus3.print_info()

for _ in range(20):  # Probeer 20 keer in te schrijven
    cursus1.verhoog_inschrijvingen() 
