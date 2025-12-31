import sys
plage = []
ingredients = []    

in_ingredient = False  
for line in sys.stdin:
    try:
        line = line.strip()
        if line == "":
            in_ingredient = True
            continue
        if not in_ingredient:
            plage.append(line)
        else:     
            ingredients.append(line)
    except ValueError:
        pass


plages = []
resultat = 0
deja_compte = []
for p in plage:
    a, b = map(int, p.split("-"))
    plages.append((a, b))

for pl in plages:
        for i in range(pl[0], pl[1]+1):
            if i not in deja_compte:
                deja_compte.append(i)   

resultat = len(deja_compte)
            
print(resultat)
