

szo1 = input("Adj meg egy szót: ")
szo2 = input("Adj meg egy masik szót: ")
szo1Hossza = len(szo1)
szo2Hossza = len(szo2)

if (szo1>szo2):
    print(f"A hosszabb szo: {szo1}")
elif (szo2>szo1):
    print(f"A hosszabb szo: {szo2}")
else:
    print("A két szó egyenlő!")
    

