
class Ronk:

    def __init__(self, azon=0, fajta='', terfogat=0, ar=0, kategoria='') -> None:
        self.azon = azon
        self.fajta = fajta
        self.terfogat = terfogat
        self.ar = ar
        self.kategoria = kategoria

    def tomeg(self):
        if (self.kategoria == 'keményfa'):
            return self.terfogat * 800
        else:
            return self.terfogat * 500


ronk1 = Ronk(1, 'tölgy', 0.9, 55000, 'keményfa')
ronk2 = Ronk(2, 'bükk', 1.2, 85000, 'keményfa')
ronk3 = Ronk(3, 'fenyő', 0.6, 38000, 'puhafa')
ronk4 = Ronk(4, 'tölgy', 0.55, 32000, 'keményfa')
ronk5 = Ronk()
ronk5.azon = int(input('Kérem az azonosítót: '))
ronk5.fajta = (input('Kérem a fajt: '))
ronk5.terfogat = float(input('Kérem a térfogatát: '))
ronk5.ar = int(input('Kérem a árát: '))
ronk5.kategoria = (input('Kérem a kategóriát: '))

ronkok = [ronk1, ronk2, ronk3, ronk4, ronk5]
bevetel = 0
for egyRonk in ronkok:
    bevetel += egyRonk.ar
print(f'Az erdészet bevétele {bevetel} Ft.')

azon = int(input('Kérem adja meg egy rönk azonositojat: '))
i = 0 
tovabb = True
while(tovabb):
    if (ronkok[i].azon == azon):
        print(f'A(z) {azon} azonosítójú rönk tömege: {ronkok[i].tomeg()} kg.')
        tovabb = False
    i += i 

index = 0
for i in range(1, len(ronkok)):
    if (ronkok[index].ar > ronkok[i].ar):
        index = 1
print(f'A legolcsóbb rönk fafaja: {ronkok[index].fajta}')

fajl = open('07/tolgy.txt', 'w', encoding='utf-8')
for egyRonk in ronkok:
    if (egyRonk.fajta == 'tölgy'):
        fajl.write(f'{egyRonk.azon}\t{egyRonk.terfogat}\t{egyRonk.ar}\n')
fajl.close()