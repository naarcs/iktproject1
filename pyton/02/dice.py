
import random

input("Nyomj egy tetszőleges billenytyüt az induláshoz!")

jatekos1_pont = 0
jatekos2_pont = 0

for i in range(10):
    jatekos1_dobas = random.randint(1, 6)
    jatekos2_dobas = random.randint(1, 6)

    print("Játékos 1 dobása: ", jatekos1_dobas)
    print("Játékos 2 dobása: ", jatekos2_dobas)

    if jatekos1_dobas > jatekos2_dobas:
        print("Játékos 1 győzött.")
        jatekos1_pont = jatekos1_pont + 1 
    elif jatekos2_dobas > jatekos1_dobas:
        print("Játékos 2 győzött")
        jatekos2_pont = jatekos2_pont + 1
    else:
        print("Döntetlen!")

    input("Nyomt enter-t a továbblépéshez!") 

print("---> Vége! <---")
print("Játékos 1 pontjai:", jatekos1_pont)
print("Játékos 2 pontjai:", jatekos2_pont)


