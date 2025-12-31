#!/usr/bin/env python3
import sys
import math

def prod(iterable):
    # compatibilité si math.prod n'existe pas
    try:
        return math.prod(iterable)
    except AttributeError:
        p = 1
        for x in iterable:
            p *= x
        return p

def main():
    # Lecture des lignes en conservant les espaces (on enlève juste le \n)
    lines = [ln.rstrip('\n') for ln in sys.stdin.readlines()]
    if not lines:
        print(0)
        return

    # Normaliser la largeur (pad avec des espaces)
    width = max(len(ln) for ln in lines)
    lines = [ln.ljust(width, ' ') for ln in lines]

    height = len(lines)

    # Détecter colonnes complètement vides (séparatrices)
    empty_col = [all(lines[r][c] == ' ' for r in range(height)) for c in range(width)]

    # Trouver intervalles contigus de colonnes non vides -> blocs
    blocks = []
    c = 0
    while c < width:
        if empty_col[c]:
            c += 1
            continue
        start = c
        while c < width and not empty_col[c]:
            c += 1
        end = c - 1
        blocks.append((start, end))

    grand_total = 0

    for start, end in blocks:
        # Pour chaque bloc, recueillir les chaînes non vides par ligne (en enlevant les espaces autour)
        items = []
        for r in range(height):
            snippet = lines[r][start:end+1]
            s = snippet.strip()
            if s != '':
                items.append(s)

        if not items:
            # bloc vide (sécurité)
            continue

        # L'opérateur attendu est la dernière chaîne
        op = items[-1]
        numbers = items[:-1]

        # Si pour une raison quelconque on a l'opérateur plus haut (ex : lignes vides après),
        # essayer de récupérer l'opérateur comme dernier caractère non-chiffre
        if op not in ('+', '*'):
            # tenter de trouver parmi les items lequel est opérateur
            found_op = None
            for i in range(len(items)-1, -1, -1):
                if items[i] in ('+', '*'):
                    found_op = items[i]
                    numbers = items[:i]
                    break
            if found_op is None:
                raise ValueError(f"Impossible de trouver l'opérateur dans le bloc {start}-{end}. Contenu: {items}")
            op = found_op

        # Convertir les nombres en entiers (ignorer les lignes vides déjà filtrées)
        ints = [int(x) for x in numbers]

        if op == '+':
            value = sum(ints)
        else:  # op == '*'
            value = prod(ints)

        grand_total += value

    print(grand_total)

if __name__ == "__main__":
    main()
