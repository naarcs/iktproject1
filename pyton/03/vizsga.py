
def eredmeny (pSzam):
    if (pSzam >= 48):
        return True
    return False

nev = "valami"
while (nev != ""):
    nev = input("Add meg a vizsgázó nevét! ")
    if (len(nev) != 0):
        pSzam = int(input("Add meg a pontszámát! "))
        if (eredmeny(pSzam)):
            print(f"{nev} vizsgája sikeres.")
        else:
            print(f"{nev} vizsgája sikertelen.")
            





