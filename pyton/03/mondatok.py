import random


def nevelo(szo):
    maganhangzok = 'aáeéiíoóöőuúüű'
    if szo[0].lower() in maganhangzok:
        return "Az"
    else:
        return "A"


def jelzo():
    return random.choice(['piros.', 'nagy.', 'könnyed.'])


print("Adj meg három fönevet!")
szo = input("1. főnév: ")
print(nevelo(szo),szo,jelzo())
szo = input("2. főnév: ")
print(nevelo(szo),szo,jelzo())
szo = input("3. főnév: ")
print(nevelo(szo),szo,jelzo())
