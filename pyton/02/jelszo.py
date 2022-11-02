


from time import sleep


jelszo = "Kando"


marad = 3 
while(marad > 0):
    bekertjelszo = input("Kérem a jelszót: ")
    if (bekertjelszo == jelszo):
        print("Sikeres bejelentkezés")
        marad = 0 
    if (marad == 1):
        print("10perc várakozás...")
        sleep(10)
        marad = 4
    marad -= 1
print("Dolgozhat!")

    