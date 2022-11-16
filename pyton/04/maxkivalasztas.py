import random

szamok = []

for i in range(1000):
    gSzam = random.randrange(10000)
    szamok.append(gSzam)

print(max(szamok))

"""
maxSzam = 0
for aktSzam in szamok:               #nemjo
    if (i > maxSzam):
        maxSzam = aktSzam
"""

maxSzam = szamok[0]
for i in range(1,len(szamok)):
    if (szamok[i]>maxSzam):              #MAX kiválasztás tétele 
        maxSzam = szamok[i]

print(maxSzam)
