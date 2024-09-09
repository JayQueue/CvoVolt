"""
Auteur: Jonathan Quartier
Datum: 9/9/2024
Workshop 1: Opdracht 1
GitHub: https://github.com/JayQueue/CvoVolt/blob/main/Workshop_1/opdracht_1.py 
"""
def make_profile(vnaam: str, naam: str, minimum_extra_info=3, **extra_info):
    # Maakt nieuw profiel aan met standaard voornaam en naam
    # en minimum 3 extra informatievelden
    if len(extra_info) >= minimum_extra_info:
        return {
            'voornaam': vnaam,
            'naam': naam,
            **extra_info
        }
        #profile.update(extra_info)
        #return profile
    else:
        return f"Geef minstens {minimum_extra_info} andere gegevens."

def write_file(filename: str, data: str):
    with open(filename, 'a') as file:
        file.write(str(data) + '\n')

# Ok profiel
profile = make_profile('Jonathan', 'Quartier', leeftijd=46, woonplaats='Kortrijk', beroep="Data miner")
# Nok profiel
#profile = make_profile('Jonathan', 'Quartier', leeftijd=45, woonplaats='Kortrijk')

print(profile)
write_file('opdracht_1_profiel.txt', profile)
