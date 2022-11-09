

def bejelentkezes(nev, jelszo):
    if (nev == "bori99" and jelszo == "Szivecske<3"):
        return True
    print("Belépés megtagadva!")
    return False


sikeresBelepes = False
while (not sikeresBelepes):
    nev = input("Adja meg a felhasználó nevét! ")
    jelszo = input("Adja meg a jelszavát! ")
    sikeresBelepes = bejelentkezes(nev,jelszo)
print("Sikeres bejelentkezés")

