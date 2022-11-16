import random

szamok = []

for i in range(1000):
    gSzam = random.randrange(10000)
    szamok.append(gSzam)

print(min(szamok))

minSzam = szamok[0]
for i in range(1,len(szamok)):
    if (szamok[i] < minSzam):              #MiN kiválasztás tétele 
        minSzam = szamok[i]

print(minSzam)


