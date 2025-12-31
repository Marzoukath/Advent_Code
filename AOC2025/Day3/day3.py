import sys
def solutionn(chaine): 
    liste = []
    taille = len(chaine)
    for i in range(taille):
        liste.append(int(chaine[i]))
    

    first = max(liste[:-1])
    position = liste.index(first)
    last = max(liste[position+1:])
    return int(str(first)+str(last))

somme = 0


for line in sys.stdin:
    try:
        somme += solutionn(line.strip())
    except ValueError:
        pass
print(somme)