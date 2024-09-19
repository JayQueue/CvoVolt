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

    def printMerkTypeBrandstof(self):
        print(f"{self.merk} {self.type} {self.brandstof}.")

    def isVerhuurd(self):
        if self.verhuurd:
            print("Deze auto is al verhuurd.")
        else:
            print("Deze auto is nog niet verhuurd.")

toyota = AutoVerhuur("Toyota", "Yaris", "Benzine", False)
toyota.printMerkTypeBrandstof()
toyota.isVerhuurd()

nissan = AutoVerhuur("Nissan", "VanEenBepaaldType", "LPG", True)
nissan.printMerkTypeBrandstof()
nissan.isVerhuurd()
