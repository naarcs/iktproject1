class JelAdat:

    def __init__(self,Ora=0,Perc=0,Masodperc=0,X=0,Y=0):
        self.Ora=Ora
        self.Perc=Perc
        self.MasodPerc=Masodperc
        self.X=X
        self.Y=Y


    

    def __str__(self):
        return f"Óra: {self.Ora}\nPerc: {self.Perc}\nMáosdperc: {self.Masodperc}\nX: {self.X}\nY: {self.Y}"

jelAdatok=[]
fajl=open("06Eloadas\jel.txt","r",encoding="utf-8")
for item in fajl:
    mezok=item.strip().split(" ")
    egyJelAdat=JelAdat()
    egyJelAdat.Ora=int(mezok[0])
    egyJelAdat.Perc=int(mezok[1])
    egyJelAdat.Masodperc=int(mezok[2])
    egyJelAdat.X=int(mezok[3])
    egyJelAdat.Y=int(mezok[4])
    jelAdatok.append(egyJelAdat)
fajl.close()
fajl=open("06Eloadas\Kimenet.txt","w",encoding="utf-8")
for item in jelAdatok:
    fajl.write(str(item)+"\n")
fajl.close()