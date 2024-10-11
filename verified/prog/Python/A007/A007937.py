from math import isqrt
from sympy.utilities.iterables import multiset_permutations as mp
def sqr(n): return isqrt(n)**2 == n
def ok(n):
    if sqr(n): return False
    s = str(n)
    return any(sqr(int("".join(p))) for p in mp(s, len(s)))
print([k for k in range(600) if ok(k)]) # _Michael S. Branicky_, Oct 18 2021