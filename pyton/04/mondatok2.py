import random

def nevelo(szo):
    maganhangzok = 'aáeéiíoóöőuúüű'
    if szo[0].lower() in maganhangzok:
        return "Az"
    else:
        return "A"


def jelzo():
    return random.choice(['piros', 'nagy', 'könnyed'])


print("Adj meg három fönevet!")
for i in range(1,4):
    szo = input(f"{i}. fönév: ")
    print(f"{nevelo(szo)} {szo} {jelzo()}.")
