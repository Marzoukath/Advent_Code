import sys
current = 50
cpt = 0
for line in sys.stdin:
    try:
        position = line[0]
        pas = int(line[1:])
        
        
        if position == "R":
            current = (current + pas) % 100
        else:
            current = (current - pas) % 100
        if current == 0:
            cpt += 1

    
    except ValueError:
        pass

print(cpt)
