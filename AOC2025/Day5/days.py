import sys

plage = []
ingredients = []    

in_ingredient = False  
for line in sys.stdin:
    line = line.strip()
    if line == "":
        in_ingredient = True
        continue
    if not in_ingredient:
        plage.append(line)
    else:     
        ingredients.append(line)


intervals = []
for p in plage:
    a, b = map(int, p.split("-"))
    intervals.append((a, b))

intervals.sort()

merged = []
start, end = intervals[0]

for s, e in intervals[1:]:
    if s <= end + 1:       
        end = max(end, e)  
    else:
        merged.append((start, end))
        start, end = s, e


merged.append((start, end))


resultat = sum(e - s + 1 for s, e in merged)

print(resultat)
