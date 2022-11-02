

vissza = int(input("Hány órás visszaszámlálást tervezünk? "))
kesleltetes = 0

for i in range(vissza):
    print(f"Visszaszámlálás: {vissza - i} Óra")
    felfug = input("Felkell fuggeszteni a visszaszamlálast? (i/n)")
    if (felfug.upper() == "I"):
        kesleltetes += 1
print(f"Rakéta indulás: {vissza + kesleltetes} Óra")



