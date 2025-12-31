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
for p in plage:
    a, b = map(int, p.split("-"))
    plages.append((a, b))

for ingr in ingredients:
    ingr = int(ingr)
    for pl in plages:
        
        if pl[0] <= ingr <= pl[1]:
            resultat += 1
            break
    
print(resultat)
