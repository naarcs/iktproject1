
kutya = []

print("Add mg 5 kutya nevét: ")
for i in range(1,6):
    kutya.append(input(f"{i} kutya neve: "))
print(kutya)


for egykutya in kutya:               #igy tudunk egy tombe keresni
    if (len(egykutya) == 2):
        print(egykutya)                






"""
for i in range(len(kutya)):          #ez is az 
    print(kutya[i])

i = 0                                 
while (i<len(kutya)):                  #ez is ugyan azt csinalja 
    print(kutya[i])
    i+=1
"""