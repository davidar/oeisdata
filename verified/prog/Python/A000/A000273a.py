from math import gcd, factorial
from sympy.utilities.iterables import partitions
def permcount(v):
    m, s, k = 1, 0, 0
    for i, t in enumerate(v):
        k = k+1 if i > 0 and t == v[i-1] else 1; m *= t*k; s += t
    return factorial(s)//m
def edges(v): return sum(sum(2*gcd(v[i], v[j]) for j in range(i)) for i in range(1, len(v))) + sum(vi-1 for vi in v)
def a(n):
    s = 0
    for p in partitions(n):
        pvec = []
        for i in sorted(p): pvec.extend([i]*p[i])
        s += permcount(pvec)*2**edges(pvec)
    return s//factorial(n)
print([a(n) for n in range(15)]) # _Michael S. Branicky_, Nov 14 2022 after _Andrew Howroyd_