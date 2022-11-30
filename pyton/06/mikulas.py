import random


class Edesseg:

    def __init__(self, Gyarto="", Nev="", Tomeg=0, Ar=0, KakaoTartalom=0, Diabetikus=False) -> None:
        self.Gyarto = Gyarto
        self.Nev = Nev
        self.Tomeg = Tomeg
        self.Ar = Ar
        self.KakaoTartalom = KakaoTartalom
        self.Diabetikus = Diabetikus

    def __str__(self) -> str:
        return f"Gyártó: {self.Gyarto}\tNév: {self.Nev}\tTömeg: {self.Tomeg} g\tÁr: {self.Ar} Ft\tKakaótartalom: {self.KakaoTartalom} %\tDiabetikus: {self.Diabetikus}"


class MikulasCsomag:

    def __init__(self, GyerekNev="", Tartalom=[]) -> None:
        self.GyerekNev = GyerekNev
        self.Tartalom = Tartalom

    def __str__(self) -> str:
        print(f"Csomag tulajdonosa: {self.GyerekNev}")
        print("Csomag tartalma: ")
        for egyEdesseg in self.Tartalom:
            print(egyEdesseg)
        return ""

    def EdessegAdd(self, edesseg):
        self.Tartalom.append(edesseg)


edesseg1 = Edesseg("Boci", "Buborékos", 80, 399, 42, False)
edesseg2 = Edesseg("Milka", "Epres", 300, 1299, 12, False)
edesseg3 = Edesseg("Boci", "Étcsoki", 90, 499, 80, True)
edesseg4 = Edesseg("Milka", "Joghurtos", 70, 699, 42, False)
edesseg5 = Edesseg("Snikers", "Mogyorós", 40, 399, 42, False)
#print(f"{edesseg1}\n{edesseg2}\n{edesseg3}\n{edesseg4}\n{edesseg5}\n")

edessegek = [edesseg1, edesseg2, edesseg3, edesseg4, edesseg5]
gyerekek = ["Csaba", "Berta", "Zsolt", "Kristof", "Attila", "Bence", "Laci", "Adri", "Tímea", "Istvan", "Anett", "Judit", "Zsombor", "Gabi"]


egyMikulasCsomag = MikulasCsomag(gyerekek[1])
#egyMikulasCsomag.Tartalom.append(edesseg3)
for i in range(10):
    egyMikulasCsomag.EdessegAdd(edessegek[random.randrange(len(edessegek))])
print(egyMikulasCsomag)