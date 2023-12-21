# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

prompt = "Raad mijn geheime getal\n"
geheim_getal = random.randint(1, 100)

def raad_het_nummer():
    aantal_pogingen = 0

    print("Welkom bij het spel 'Raad een nummertje'!")
    print("Ik heb een getal tussen 1 en 100 in gedachten. Raad welk getal het is.")

    while True:
        gok = int(input(prompt))
        
        aantal_pogingen += 1

        if gok == geheim_getal:
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden: {geheim_getal}")
            print(f"Het aantal pogingen: {aantal_pogingen}")
            break
        elif gok < geheim_getal:
            print("Het te raden getal is hoger. Probeer opnieuw.")
        else:
            print("Het te raden getal is lager. Probeer opnieuw.")

if __name__ == "__main__":
    raad_het_nummer()




