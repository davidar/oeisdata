from itertools import combinations_with_replacement as mc
def a(n): return len(set(i*j*k for i, j, k in mc(range(n+1), 3)))
print([a(n) for n in range(50)]) # _Michael S. Branicky_, May 28 2021