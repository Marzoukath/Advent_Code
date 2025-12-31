#!/usr/bin/env python3
"""
Part 2 - sum of IDs that are a repetition of some digit-sequence at least twice.
Input: one line containing ranges like "11-22,95-115,998-1012,..."
Output: sum of unique invalid IDs that appear inside the given ranges.
"""
from typing import List, Tuple

def parse_ranges(line: str) -> List[Tuple[int,int]]:
    parts = [p.strip() for p in line.strip().split(',') if p.strip()]
    ranges = []
    for p in parts:
        a, b = p.split('-')
        ranges.append((int(a), int(b)))
    return ranges

def sum_invalid_ids_part2(ranges: List[Tuple[int,int]]) -> int:
    if not ranges:
        return 0
    max_b = max(b for _, b in ranges)
    len_b = len(str(max_b))
    invalid_ids = set()
    # Pour chaque plage, on génère les nombres qui sont (pattern) répété k fois (k>=2)
    for a, b in ranges:
        # p = longueur du motif (1..)
        for p in range(1, len_b + 1):
            max_k = len_b // p
            if max_k < 2:
                break
            ten_p = 10 ** p
            pattern_min = 10 ** (p - 1)  # empêche les motifs commençant par 0
            pattern_max = ten_p - 1
            for k in range(2, max_k + 1):
                # R = 1 + 10^p + 10^(2p) + ... + 10^{(k-1)p} = (10^(p*k)-1)/(10^p-1)
                numerator = 10 ** (p * k) - 1
                denom = ten_p - 1
                R = numerator // denom
                # pattern * R doit être dans [a, b]
                # => pattern ∈ [ceil(a/R), floor(b/R)]
                low = (a + R - 1) // R
                high = b // R
                lo = max(pattern_min, low)
                hi = min(pattern_max, high)
                if lo <= hi:
                    for pattern in range(lo, hi + 1):
                        N = pattern * R
                        if a <= N <= b:
                            invalid_ids.add(N)
    return sum(invalid_ids)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # si on passe le fichier en argument, on lit la première ligne
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            line = f.readline().strip()
    else:
        print("Entrez la ligne de plages (ex: 11-22,95-115,998-1012,...), puis <Entrée> :")
        line = sys.stdin.readline().strip()
    ranges = parse_ranges(line)
    total = sum_invalid_ids_part2(ranges)
    print(total)
