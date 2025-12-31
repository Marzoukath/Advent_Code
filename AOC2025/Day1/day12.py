import sys
current = 50
cpt = 0
for line in sys.stdin:
    try:
        position = line[0]
        pas = int(line[1:])

        for i in range(pas):
            if position == "R":
                current = (current + 1) % 100
            else:
                current = (current - 1) % 100
            if current == 0:
                cpt += 1


    
    except ValueError:
        pass

print(cpt)

