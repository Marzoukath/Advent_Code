import sys
def solutionn(chaine): 
    liste = []
    taille = len(chaine)
    for i in range(taille):
        liste.append(int(chaine[i]))

    chr = ""
    position = -1
    maxi = 0


    for j in range (-11, 0): 
        maxi = max(liste[position+1:j])
        
        chr += str(maxi)

        position = liste.index(maxi, position + 1)
        
    
     
    last = max(liste[position+1:])  
    chr += str(last)
    return int(chr)
    

somme = 0


for line in sys.stdin:
    try:
        somme += solutionn(line.strip())
    except ValueError:
        pass
print(somme)

