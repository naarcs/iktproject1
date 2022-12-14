

def halHossz(sz, h, m):
    
    cm3 = sz * h * m
    cm = cm3 / 1000
    return cm
    
sz = int(input('Kérem, adja meg az akvárium szélességét egész centiméterben: '))
h = int(input('Kérem, adja meg az akvárium hosszúságát egész centiméterben: '))
m = int(input('Kérem, adja meg az akvárium magasságát egész centiméterben: '))
print(f'Az akváriumban összesen {halHossz(sz, h, m)} cm hal lehet.')

for i in range(30,51,5):
    halakHossza = halHossz(50, 70, i)
    halakSzama = halakHossza / 3
    print(f'Ha a magasság: {i} cm, akkor {round(halakSzama)} db hal telepíthető.')

i = 1
tovabb = True
while (tovabb):
    if (halHossz(i ,80, 35) >= 160):
        tovabb = False
        print(f'A szélességnek minimum {i} cm-nek kell lennie')
    i += 1
