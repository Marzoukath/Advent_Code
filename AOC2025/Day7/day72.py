#!/usr/bin/env python3
import sys
from functools import lru_cache

def count_timelines(lines):
    if not lines:
        return 0

    # Normaliser largeur et construire grille
    width = max(len(ln) for ln in lines)
    grid = [ln.rstrip('\n').ljust(width, ' ') for ln in lines]
    height = len(grid)

    # Trouver S
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

    @lru_cache(maxsize=None)
    def timelines_from(row_start, col):
        """
        Nombre de timelines issues d'une particule démarrant à (row_start, col).
        La particule commencera à descendre à partir de row_start+1.
        """
        # si colonne hors grille => la particule sort immédiatement (1 timeline)
        if col < 0 or col >= width:
            return 1

        r = row_start + 1
        while r < height:
            ch = grid[r][col]
            if ch == '^':
                # splitter trouvé : retourne somme des timelines issues des deux nouvelles particules
                left_col = col - 1
                right_col = col + 1
                # si left_col/right_col hors limites, considérer que la particule sort immédiatement (contribue 1)
                left_count = timelines_from(r, left_col) if 0 <= left_col < width else 1
                right_count = timelines_from(r, right_col) if 0 <= right_col < width else 1
                return left_count + right_count
            else:
                # tout autre caractère ('.', ' ', chiffres, 'S', etc.) est traversable
                r += 1
        # atteint le bas sans splitter
        return 1

    return timelines_from(start[0], start[1])


def main():
    lines = [ln for ln in sys.stdin.readlines()]
    result = count_timelines(lines)
    print(result)


if __name__ == "__main__":
    main()
