
def feladat1():
    print("Első feledat!")
    tomb = []
    for i in range(3):
        tomb.append(int(input("Kérek egy számot: ")))
    print(f"A legkissebb szám: {min(tomb)}")

#feladat1()

def feladat2():
    print("Második feledat!")
    tomb1 = [] 
    for i in range(3):
        tomb1.append(int(input("Kérek egy számot: "))) 
    tomb1.sort(reverse=True)
    print(f"A legnagyobb szám: {tomb1[0]}")

#feladat2()

def feladat3():
    print("Harmadik feledat!")
    pontSzam = int(input("Add meg a pontszámod: "))
    if pontSzam < 50:
        print("A jegyed: 1")
    if 50 <= pontSzam < 60:
        print("A jegyed: 2")
    if 60 <= pontSzam < 70:
        print("A jegyed: 3")
    if 70 <= pontSzam < 85:
        print("A jegyed: 4")
    if pontSzam >= 85:
        print("A jegyed: 5")

#feladat3()

def feladat4():
    print("Negyedik feledat!")
    oszthato = False
    eSzam = int(input("Adj meg egy egész számot: "))
    if eSzam % 3 == 0 or eSzam % 5 == 0:
        oszthato = True
    if oszthato == True:
        print("Igen")
    else:
        print("Nem")
    
#feladat4()

def feledat5():
    print("Ötedik feladat!")
    print("Adj meg 3 számot!")
    a = int(input("Első szám: "))
    b = int(input("Második szám: "))
    c = int(input("Harmadik szám: "))
    van = False
    if (a + b) == c:
        van = True
    if (a + c) == b:
        van = True
    if (c + b) == a:
        van = True
    print(van)

#feledat5()

def feladat6():
    print("Hatodik feladat!")
    print("Adj meg 3 számot!")
    a = int(input("Első szám: "))
    b = int(input("Második szám: "))
    c = int(input("Harmadik szám: "))
    van = False
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        van = True
    
    if van:
        print("IGEN")
    else:
        print("NEM")

#feladat6()

def feladat7():
    print("Hetedik feladat!")
    szavak = []
    szavak.append(input("Első szó: "))
    szavak.append(input("Második szó: "))
    abc_szavak = sorted(szavak)
    print(abc_szavak)

feladat7()