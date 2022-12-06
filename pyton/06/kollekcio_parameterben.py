
def eljaras(kapottkollekcio):
    tmpKollekcio = []
    for item in kapottkollekcio:
        tmpKollekcio.append(item)
    tmpNev = tmpKollekcio[2]
    tmpKollekcio[2] = tmpKollekcio[3]
    tmpKollekcio[3] = tmpNev
    print(tmpKollekcio)


kollekcio = ["Csaba", "Berta", "Zsolt", "Kristof"]
print(kollekcio)
eljaras(kollekcio)
print(kollekcio)


