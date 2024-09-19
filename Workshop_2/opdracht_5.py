"""
Auteur: Jonathan Quartier
Datum: 19/9/2024
Workshop 2: Opdracht 5
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_2/opdracht_5.py 
"""
class MyClassJonathanQuartier:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        
    def print_boodschap(self, boodschap=None):
        if boodschap:
            print(boodschap)
        elif self.x is None and self.y is None:
            print("\tGeen waarden gegeven voor x & y.\n")
        elif self.x is not None and self.y is not None:
            print(f"\tX: {self.x}, Y: {self.y}\n")

def main():
    while True:
        try:
            x = int(input("Geef een geheel getal voor x: ") or 0) or None
            y = int(input("Geef een geheel getal voor y: ") or 0) or None
            jq = MyClassJonathanQuartier(x, y)
            if x is not None and x > 10 and y is not None and y > 10:
                jq.print_boodschap("\tx & y zijn groter dan 10. Quitting.\n")
                break
            elif x is not None and x > 10:
                jq.print_boodschap("\tx is groter dan 10. Quitting.\n")
                break
            elif y is not None and y > 10:
                jq.print_boodschap("\ty is groter dan 10. Quitting.\n")
                break
            jq.print_boodschap()
        except ValueError:
            print("Voer een geheel getal in.")
            
if __name__ == "__main__":
    main()
