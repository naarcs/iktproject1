


import random

def OsszeHasonlitas(rSzam,bSzam):
    try:
        bSzam = int(bSzam)
        if (bSzam < rSzam):
            return f"A gép nagyobb számra gondolt: {rSzam}"
        elif (bSzam > rSzam):
            return f"A gép kisebb számra gondolt: {rSzam}"
        else:
            return f"Eltaláltad a gép által gondolt számot! {rSzam}"
    except:
        return "Nem számot adtál meg!"
    finally:                                #Mindig lefut
        print("Csicska")


rSzam = random.randrange(1,17)
bSzam = input("Adj meg egy számot! ")

#Érték Tárolás

uzenet = OsszeHasonlitas(rSzam,bSzam)
print(uzenet)


