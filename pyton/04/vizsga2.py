import random

def pontSzamGenerator(maxPontSzam):
    return random.randrange(0, maxPontSzam + 1)


def ertekeles(pontSzam):
    if (pontSzam < 48):
        return 1
    if (pontSzam <= 66):
        return 2
    if (pontSzam <= 84):
        return 3
    if (pontSzam <= 102):
        return 4
    return 5


diakok = ["Csaba", "Berta", "Zsolt", "Kristof", "Attila", "Bence", "Laci", "Adri", "Tímea", "Istvan", "Anett", "Judit", "Zsombor", "Gabi"]

pontSzamok = []
for i in range(len(diakok)):
    pontSzamok.append(pontSzamGenerator(120))

szum = 0
for i in range(len(diakok)):
    erdemjegy = ertekeles(pontSzamok[i])
    print(f"{diakok[i]}: {erdemjegy}")
    szum += erdemjegy
print(f"Osztály átlag: {round(szum/len(diakok), 2)}")


