
import random

egyesek = ['nulla', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
tizesek = ['', 'tizen', 'huszon', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']

fajl = open("05\szamok.txt", "w", encoding="utf-8")
fajl.write(f"1 - egy\n")
fajl.write(f"2 - kettő\n")
fajl.write(f"3 - három\n")

for i in range(1000):
    veletlenSzam = str(random.randrange(100,1000))
    szovegesSzam = f"{egyesek[int(veletlenSzam[0])]}száz"
    if (veletlenSzam[1] + veletlenSzam[2] == "10"):
        szovegesSzam += 'tíz'
        continue
    if (veletlenSzam[1] + veletlenSzam[2] == "20"):
        szovegesSzam += 'húsz'
        continue
    szovegesSzam += tizesek[int(veletlenSzam[1])]
    if (veletlenSzam[2] != "0"):
        szovegesSzam += egyesek[int(veletlenSzam[2])]

    #print(f"{veletlenSzam} - {szovegesSzam} \n")
    fajl.write(f"{veletlenSzam} - {szovegesSzam} \n")

fajl.close()

