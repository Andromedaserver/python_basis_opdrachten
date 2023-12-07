# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

try:
   
   A = float(input("Geef de lengte van de eerste zijde \n "))
   B = float(input("Geef de lengte van de tweede zijde \n "))

   mid = B**2 + A**2
   C = math.sqrt(mid)

   print (C)
except ValueError:
   print("Hey dat is geen getal!")

