from itertools import combinations
def afull(): return [0] + sorted(int("".join(c)) for d in range(1, 10) for c in combinations("123456789", d))
print(afull()) # _Michael S. Branicky_, Sep 16 2022