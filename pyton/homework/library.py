

class Book:

    def __init__(self, ISBNszam = 0, Szerzo = '', Cim = '', Megjelenes = 0, Nyelv = '', KiadasSzama = 0, Tiltott = True) -> None:
        self.ISBNszam = ISBNszam
        self.Szerzo = Szerzo
        self.Cim = Cim
        self.Megjelenes = Megjelenes
        self.Nyelv = Nyelv
        self.KiadasSzama = KiadasSzama
        self.Tiltott = Tiltott

    def __str__(self) -> str:
        return f"ISBNszám: {self.ISBNszam}\tSzerző: {self.Szerzo}\tCím: {self.Cim}\tMegjelenési év: {self.Megjelenes}\tNyelv: {self.Nyelv}\tKiadás száma: {self.KiadasSzama}\tTiltott mű-e: {self.Tiltott}"


class Library:

    def __init__(self, Konyvtar = []) -> None:
        self.Konyvtar = Konyvtar

    def __str__(self) -> str:
        return ''

    def KonyvAdd(self, konyv):
        self.Konyvtar.append(konyv)


konyv1 = Book(1234567891, 'Fekete Istvan', 'Vuk', 1980, 'Magyar', 10000, False)
konyv2 = Book(1234567892, 'Petőfi Sándor', 'Anyám tyukja', 1950, 'Magyar', 15000, False)

konyvek = [konyv1, konyv2]

Konyvtar = Library()
Konyvtar.KonyvAdd(konyvek)
print(Konyvtar)

fajl = open("homework\konytar.txt", "w", encoding="utf-8")
fajl.write()
fajl.close()
