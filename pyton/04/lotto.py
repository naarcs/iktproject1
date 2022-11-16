import random

maxSzam = 90
hanyasLotto = 5

sajatSzam = []
print("Add meg a saját szamaidat!")
for i in range(5):
    szam = int(input(f"{i+1}. szám: "))
    sajatSzam.append(szam)


sorsoltSzamok = []
while(len(sorsoltSzamok) <= hanyasLotto):
    sorsoltSzam = random.randrange(1,maxSzam+1)
    if (sorsoltSzam not in sorsoltSzamok):
        sorsoltSzamok.append(sorsoltSzam)
print(sorsoltSzamok)

talalatokSzama = 0
for egySajatSzam in sajatSzam:
    if (egySajatSzam in sorsoltSzamok):
        talalatokSzama+=1
print(f"Találat száma: {talalatokSzama}")