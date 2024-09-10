"""
Auteur: Jonathan Quartier
Datum: 10/9/2024
Workshop 1: Opdracht 3
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_1/opdracht_3.py 
"""
from opdracht_3_module import dupeletters 

str1 = input('Geef een eerste woord:\n')
str2 = input('Geef een tweede woord:\n')

print (f'Er zijn {dupeletters(str1, str2)} tekens hetzelfde tussen {str1} en {str2}')
