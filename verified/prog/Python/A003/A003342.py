from itertools import combinations_with_replacement as mc
from sympy import integer_nthroot
def iroot4(n): return integer_nthroot(n, 4)[0]
def aupto(lim):
    pows4 = set(i**4 for i in range(1, iroot4(lim)+1) if i**4 <= lim)
    return sorted(t for t in set(sum(c) for c in mc(pows4, 8)) if t <= lim)
print(aupto(568)) # _Michael S. Branicky_, Aug 23 2021