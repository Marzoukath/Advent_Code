import sys

matrice = []
for line in sys.stdin:
    try:
        matrice.append(list(line.strip()))
    except ValueError:
        pass


ligne = len(matrice)
colonne = len(matrice[0])
resultat = 0
for i in range(ligne):
    for j in range(colonne):
        if matrice[i][j] == '@':

            som_adjacent = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    ni = i + x
                    nj = j + y
                    if 0 <= ni < ligne and 0 <= nj < colonne:
                        if matrice[ni][nj] == '@':
                            som_adjacent += 1
            if som_adjacent < 4: 
                resultat += 1
print(resultat)

            
