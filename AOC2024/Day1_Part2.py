import sys
from collections import Counter

sys.stdin = open("data.in", "r")


liste1 = []
liste2 = []


for line in sys.stdin:
    a, b = map(int, line.split())
    liste1.append(a)
    liste2.append(b)

compteur_liste2 = Counter(liste2)

similarity_score = 0
for num in liste1:
    if num in compteur_liste2:
        similarity_score += num * compteur_liste2[num]

# Afficher le score de similarité
print(similarity_score)
