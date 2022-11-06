
import random

input("Nyomj enter-t az induláshoz!")

print()

jatekos1_pont = 0
jatekos2_pont = 0
kor = 1

for i in range(10):
    jatekos1_dobas = random.randint(1, 6)
    jatekos2_dobas = random.randint(1, 6)

    print(f"{kor}. Kör")
    kor = kor + 1

    print("Játékos 1 dobása:", jatekos1_dobas)
    print("Játékos 2 dobása:", jatekos2_dobas)

    if jatekos1_dobas > jatekos2_dobas:
        print("Játékos 1 győzött.")
        jatekos1_pont = jatekos1_pont + 1 
    elif jatekos2_dobas > jatekos1_dobas:
        print("Játékos 2 győzött")
        jatekos2_pont = jatekos2_pont + 1
    else:
        print("Döntetlen!")

    input("Nyomt enter-t a továbblépéshez!") 

    print()

print("---> Vége! <---")
print("Játékos 1 pontjai:", jatekos1_pont)
print("Játékos 2 pontjai:", jatekos2_pont)

print()

if (jatekos1_pont > jatekos2_pont):
    print("Játékos 1 nyert!")
elif (jatekos1_pont < jatekos2_pont):
    print("Játékos 2 nyert!")
else:
    print("Döntetlen!")

