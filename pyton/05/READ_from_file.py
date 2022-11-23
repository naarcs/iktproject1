

fajl = open("05\jel.txt", "r", encoding="utf-8")
jelAdatok = []

for sor in fajl:
    #print(sor.strip())
    mezok = sor.strip().split(" ")
    jelAdatok.append(mezok)

fajl.close()
#print(jelAdatok)

#Érték szerinti keresés és tárolás 
max_X = int(jelAdatok[0][3])
min_X = max_X
max_Y = int(jelAdatok[0][4])
min_Y = max_Y
#print(max_X)
for i in range(1,len(jelAdatok)):
    if (int(jelAdatok[i][3]) > max_X):
        max_X = int(jelAdatok[i][3])
    if (int(jelAdatok[i][3]) < min_X):
        min_X = int(jelAdatok[i][3])
    if (int(jelAdatok[i][4]) > max_Y):
        max_Y = int(jelAdatok[i][4])
    if (int(jelAdatok[i][4]) < min_Y):
        min_Y = int(jelAdatok[i][4])
print(max_X, min_Y)
print(min_X, max_Y)

#Érték szerinti keresés és index szerinti tárolas
max_X_index=min_X_index=max_Y_index=min_Y_index = 0
for i in range(1,len(jelAdatok)):
    if int(jelAdatok[i][3]) > int(jelAdatok[max_X_index][3]):
        max_X_index = i
    if int(jelAdatok[i][3]) < int(jelAdatok[min_X_index][3]):
        min_X_index = i
    if int(jelAdatok[i][4]) > int(jelAdatok[max_Y_index][4]):
        max_Y_index = i
    if int(jelAdatok[i][4]) < int(jelAdatok[min_Y_index][4]):
        min_Y_index = i
print(jelAdatok[max_X_index][3], jelAdatok[min_Y_index][4])
print(jelAdatok[min_X_index][3], jelAdatok[max_Y_index][4])
print(jelAdatok[max_X_index][0], jelAdatok[max_X_index][1], jelAdatok[max_X_index][2])



