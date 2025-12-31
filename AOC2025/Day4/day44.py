import sys

mat = []
for line in sys.stdin:
    try:
        mat.append(list(line.strip()))
    except ValueError:
        pass

def is_adjacent(matrice):
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
                    matrice[i][j] = '.'
                    resultat += 1
    return resultat, matrice

ans = 0
while True:
    res, mat = is_adjacent(mat)
    if res == 0:
        break
    ans += res




print(ans)
