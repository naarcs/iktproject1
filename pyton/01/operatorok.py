#operátorok
#értékadó operátorok - "="

szoveg1="Kutya"
szoveg2='Macska' #nem annyira jó!

valosSzam1=123.56
egeszSzam1=245

logikaiValtozo1=True
logikaiValtozo2=False

print(szoveg1, szoveg2, valosSzam1, egeszSzam1, logikaiValtozo1, logikaiValtozo2)


#Műveleti Operátorok - " +, -, *, /, %-mod, //-div, **-hatványozás"

eredmeny1=valosSzam1+egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1-egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1*egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1/egeszSzam1
print(eredmeny1)

eredmeny2=10/3
print(eredmeny2)
eredmeny2=10//3
print(eredmeny2)
eredmeny2=10%3
print(eredmeny2)

eredmeny3=2**8
print(eredmeny3)

szovegesEredmeny=szoveg1+szoveg2
print(szovegesEredmeny)
szovegesEredmeny2=szoveg1*5
print(szovegesEredmeny2)

# Értéknövelő operátorok

darab = 0 
print(darab)
darab += 1
print(darab)
darab -= 1
print(darab)


#Összehasonlito Operátorok - "<, >, <=, >=, !=, =="
#Egyszerű egyirányú elágazás

if (valosSzam1<1000):
    print("A valosSzam1 értéke kisebb mint 1000.")
    print("Vizsgálat vége.")

#Összetett két irányu elágazás

if (egeszSzam1>500):
    print("Az egeszSzam1 változó értéke nagyobb mint 500.")
else:
    print("Az egeszSzam1 vátozó értéke kisebb vagy egyenlő mint 500.")

#Összetett több irányú elágazás

if (egeszSzam1==245):
    print("Az egeszSzam1 értéke 245.")
elif (egeszSzam1>245):
    print("Az egeszSzam1 értéke nagyobb mint 245.")
else:
    print("Az egeszSzam1 értéke kisebb mint 245.")

if (szoveg1==szoveg2):
    print("Azonos")
else:
    print("Nem azonos")


#Logikai Opetátorok (and, or , not)

#  or 
#A B E
#0 0 0
#0 1 1
#1 0 1
#1 1 1

#  and 
#A B E
#0 0 0
#0 1 0
#1 0 0
#1 1 1

#  not 
#A E
#0 1
#1 0


egeszSzam2=246

if (egeszSzam1>=245 and egeszSzam2<=246):
    print("Ok")

if (szoveg1=="Kutya" or egeszSzam1>1000):
    print("Igaz")

if (logikaiValtozo1):
    print("Hello")

if (not logikaiValtozo2):
    print("Nem igaz")       