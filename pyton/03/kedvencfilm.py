

def oraperc(perc):
    ora = perc // 60
    sec = perc % 60
    return f"{ora} óra {sec} perc"

for i in range(3):
    filmCim = input("Addmeg egy film címét! ")
    perc = int(input("Hány perces a film! "))
    print(f"A(z) {filmCim} című film {oraperc(perc)} hosszú.")

