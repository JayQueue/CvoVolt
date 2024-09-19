"""
Auteur: Jonathan Quartier
Datum: 19/9/2024
Workshop 2: Opdracht 6
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_1/opdracht_3.py 
"""
class AutoVerhuur:
    def __init__(self, merk: str, type: str, brandstof: str, verhuurd: bool):
        self.merk = merk
        self.type = type
        self.brandstof = brandstof
        self.verhuurd = verhuurd

    def print_info(self):
        print(f"{self.merk} {self.type} {self.brandstof}.")

    def is_verhuurd(self):
        if self.verhuurd:
            print("Deze auto is al verhuurd.")
        else:
            print("Deze auto is nog niet verhuurd.")

toyota = AutoVerhuur("Toyota", "Yaris", "Benzine", False)
toyota.print_info()
toyota.is_verhuurd()

nissan = AutoVerhuur("Nissan", "VanEenBepaaldType", "LPG", True)
nissan.print_info()
nissan.is_verhuurd()

bmw = AutoVerhuur("BMW", "Ik ken daar niet van", "Diesel", False)
bmw.print_info()
bmw.is_verhuurd()

citroen = AutoVerhuur("Citroen", "WeetIkVeel", "Benzine", True)
citroen.print_info()
citroen.is_verhuurd()

