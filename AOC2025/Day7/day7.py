#!/usr/bin/env python3
import sys
from collections import deque

def count_splits(lines):
    if not lines:
        return 0

    # Normaliser largeur (pad avec espaces)
    width = max(len(ln) for ln in lines)
    grid = [ln.rstrip('\n').ljust(width, ' ') for ln in lines]
    height = len(grid)

    # Trouver la position de S
    start = None
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break
    if start is None:
        raise ValueError("Point 'S' introuvable dans l'entrée.")

    # Utilitaires
    def is_splitter(r, c):
        return 0 <= r < height and 0 <= c < width and grid[r][c] == '^'

    def is_empty(r, c):
        # considérer '.' et ' ' comme vide (tout sauf '^' et 'S' est vide)
        if not (0 <= r < height and 0 <= c < width):
            return False
        return grid[r][c] != '^'

    # BFS/queue sur positions de départ des faisceaux:
    # un faisceau est défini par (row_start, col). Il commence à la ligne row_start,
    # et son premier mouvement inspecte la cellule row_start+1, etc.
    q = deque()
    # On met la position de départ (ligne de S, colonne de S)
    q.append((start[0], start[1]))

    # Pour éviter de retraiter la même position départ plusieurs fois
    processed_starts = set()
    processed_starts.add((start[0], start[1]))

    # Ensemble des splitters déjà activés (pour ne compter qu'une fois)
    activated_splitters = set()

    splits = 0

    while q:
        row_start, col = q.popleft()

        # le faisceau descend ; on commence à la ligne suivante
        r = row_start + 1
        while r < height:
            ch = grid[r][col]
            if ch == '^':
                # splitter rencontré en (r, col)
                if (r, col) not in activated_splitters:
                    activated_splitters.add((r, col))
                    splits += 1
                    # créer deux nouveaux faisceaux depuis la même ligne, colonnes à gauche/droite
                    for newc in (col - 1, col + 1):
                        if 0 <= newc < width:
                            start_pos = (r, newc)
                            if start_pos not in processed_starts:
                                processed_starts.add(start_pos)
                                q.append(start_pos)
                # le faisceau qui a atteint ce splitter s'arrête (on ne continue pas sous le ^)
                break
            else:
                # si caractère autre qu'espace (ex: 'S' ou '.') on continue à descendre
                # on considère tout sauf '^' comme traversable
                r += 1
        # si r >= height => le faisceau sort du bas de la grille et s'arrête naturellement

    return splits

def main():
    lines = [ln for ln in sys.stdin.readlines()]
    result = count_splits(lines)
    print(result)

if __name__ == "__main__":
    main()
