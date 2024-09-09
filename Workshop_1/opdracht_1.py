"""
Auteur: Jonathan Quartier
Datum: 9/9/2024
Workshop 1: Opdracht 1
"""
def make_profile(vnaam: str, naam: str, minimum_extra_info=3, **extra_info):
    if len(extra_info) >= minimum_extra_info:
        profile = {
            'voornaam': vnaam,
            'naam': naam
        }
        profile.update(extra_info)
        return profile
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
