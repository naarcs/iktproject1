

import random

rSzam = random.randrange(1,17)

bekertSzam = int(input("Adj meg egy számot!"))
if (bekertSzam < rSzam):
    print(f"A gép nagyobb számra gondolt: {rSzam}")
elif (bekertSzam > rSzam):
    print(f"A gép kisebb számra gondolt: {rSzam}")
else:
    print(f"Eltaláltad a gép által gondolt számot! {rSzam}")



