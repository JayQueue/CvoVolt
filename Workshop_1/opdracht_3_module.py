"""
Auteur: Jonathan Quartier
Datum: 10/9/2024
Workshop 1: Opdracht 3
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_1/opdracht_3_module.py 
"""
def dupeletters(string1: str, string2: str):
    return len(set(string1).intersection(set(string2)))
