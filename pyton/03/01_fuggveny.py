
import random

def OsszeHasonlitas(rSzam,bSzam):
    if (bSzam < rSzam):
        return f"A gép nagyobb számra gondolt: {rSzam}"
    elif (bSzam > rSzam):
        return f"A gép kisebb számra gondolt: {rSzam}"
    else:
        return f"Eltaláltad a gép által gondolt számot! {rSzam}"


rSzam = random.randrange(1,17)
bSzam = int(input("Adj meg egy számot!"))

print(OsszeHasonlitas(rSzam,bSzam))

#Érték Tárolás

uzenet = OsszeHasonlitas(rSzam,bSzam)
print(uzenet)
for betu in uzenet:
    print(betu,end=" ")
print()



