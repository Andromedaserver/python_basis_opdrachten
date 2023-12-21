# Opdracht 1 while-loops
# Naam student:
# Groep:

# Vraag 1
antwoord1 = input("Wat vind je van de huidige regering? ")

# Vraag 2
antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")

# Vraag 3
antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")

print("\nBedankt voor het beantwoorden van de vragen!")
print("Resultaten:")
print(f"1. Wat vind je van de huidige regering? {antwoord1}")
print(f"2. Wat vind je van de Python-lessen tot nu toe? {antwoord2}")
print(f"3. Wat vind jij de mooiste stad van Nederland? {antwoord3}")

bestandsnaam = "enquete_resultaten.txt"
with open(bestandsnaam, "w") as bestand:
    bestand.write(f"1. Wat vind je van de huidige regering? {antwoord1}\n")
    bestand.write(f"2. Wat vind je van de Python-lessen tot nu toe? {antwoord2}\n")
    bestand.write(f"3. Wat vind jij de mooiste stad van Nederland? {antwoord3}\n")

print(f"\nResultaten zijn opgeslagen in {bestandsnaam}")
