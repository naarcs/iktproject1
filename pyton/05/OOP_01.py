

class JelAdat:

    def __init__(self, Ora = 0, Perc = 0, MasodPerc = 0, X = 0, Y = 0):
        self.Ora = Ora
        self.Perc = Perc
        self.MasodPerc = MasodPerc
        self.X = X
        self.Y = Y

    def __str__(self) -> str:
        return f"Óra: {self.Ora}\nPerc: {self.Perc}\nMásodperc: {self.MasodPerc}\nX: {self.X}\nY: {self.Y}"

elsoJelAdat = JelAdat(3,13,37,234,675)

masodikAdat = JelAdat()
masodikAdat.Ora = 2
masodikAdat.Perc = 22
masodikAdat.MasodPerc = 31
masodikAdat.X = 123
masodikAdat.Y = 432

print(elsoJelAdat)
print(masodikAdat)

        



