
import random

def eredmeny(rSzam,bSzam):
    if (bSzam < rSzam):
        print(f"A gép nagyobb számra gondolt: {rSzam}")
    elif (bSzam > rSzam):
        print(f"A gép kisebb számra gondolt: {rSzam}")
    else:
        print(f"Eltaláltad a gép által gondolt számot! {rSzam}")


rSzam = random.randrange(1,17)
bSzam = int(input("Adj meg egy számot!"))

eredmeny(rSzam,bSzam)




