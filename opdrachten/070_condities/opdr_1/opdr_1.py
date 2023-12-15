# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....


my_list = []
hoger = []

for num in range(1, 11):
    my_list.append(num)

for getal in my_list:
    if getal > 4:
        hoger.append(getal)
print(hoger)