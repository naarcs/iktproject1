
bekertOra = int(input("Hány óra van most? "))

if (8 <= bekertOra < 16):
    print("A bolt nyitva van!")
    print(f"Ennyi orád van meg oda érni: {16 - bekertOra}")
else:
    print("Zárva")
