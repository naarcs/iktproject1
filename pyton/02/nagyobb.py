szam1 = int(input("Adj meg egy szamot: "))
szam2 = int(input("Adj meg egy masik szamot: "))
if (szam1>szam2):
    print("A nagyobb érték", szam1)
    print("A nagyobb érték " + str(szam1))
    print("A nagyobb érték {0}".format(szam1))
    print(f"A nagyobb érték {szam1}")
elif (szam2>szam1):
    print(f"A nagyobb érték {szam2}")
else:
    print("A két szám egyenlő")
    