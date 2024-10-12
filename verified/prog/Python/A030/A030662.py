from math import comb
def a(n): return comb(2*n, n) - 1
print([a(n) for n in range(1, 27)]) # _Michael S. Branicky_, Jul 11 2023