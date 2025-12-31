#!/usr/bin/env python3
import sys
import math

def prod(iterable):
    try:
        return math.prod(iterable)
    except AttributeError:
        p = 1
        for x in iterable:
            p *= x
        return p

def main():
    # Lire toutes les lignes (conserver espaces internes, retirer '\n')
    lines = [ln.rstrip('\n') for ln in sys.stdin.readlines()]
    if not lines:
        print(0)
        return

    # Normaliser largeur
    width = max(len(ln) for ln in lines)
    lines = [ln.ljust(width, ' ') for ln in lines]
    height = len(lines)

    # Détecter colonnes vides (séparatrices entre problèmes)
    empty_col = [all(lines[r][c] == ' ' for r in range(height)) for c in range(width)]

    # Trouver intervalles contigus de colonnes non vides -> blocs (chaque bloc = un problème)
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
        # 1) trouver l'opérateur sur la dernière ligne du bloc
        bottom_snip = lines[height - 1][start:end + 1]
        op = None
        for ch in bottom_snip:
            if ch in ('+', '*'):
                op = ch
                break
        if op is None:
            # sécurité : chercher dans toutes les lignes du bloc (au cas où)
            for r in range(height - 1, -1, -1):
                for ch in lines[r][start:end + 1]:
                    if ch in ('+', '*'):
                        op = ch
                        break
                if op:
                    break
        if op is None:
            raise ValueError(f"Impossible de trouver l'opérateur pour le bloc {start}-{end}. Contenu bottom: {bottom_snip!r}")

        # 2) reconstruire les nombres en lisant chaque colonne (de droite à gauche)
        numbers = []
        for col in range(end, start - 1, -1):   # droite -> gauche
            # prendre tous les caractères de la colonne sauf la dernière ligne (opérateur)
            digits = []
            for r in range(0, height - 1):  # 0 .. height-2
                ch = lines[r][col]
                if ch != ' ':
                    digits.append(ch)
            if not digits:
                # colonne vide (aucun chiffre) -> ignorer
                continue
            num_str = ''.join(digits)   # chiffres du haut (MSD) au bas (LSD)
            # sécurité : si la colonne contient autre chose que des chiffres (ex: signes),
            # on tente d'extraire uniquement les chiffres
            filtered = ''.join(ch for ch in num_str if ch.isdigit())
            if filtered == '':
                # pas de chiffre dans cette colonne -> ignorer
                continue
            numbers.append(int(filtered))

        if not numbers:
            # bloc sans nombres valides -> ignorer
            continue

        # 3) calculer la valeur du problème
        if op == '+':
            value = sum(numbers)
        else:  # op == '*'
            value = prod(numbers)

        grand_total += value

    print(grand_total)


if __name__ == "__main__":
    main()
