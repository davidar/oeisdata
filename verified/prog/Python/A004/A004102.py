from itertools import combinations
from math import prod, gcd, factorial
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A004102(n): return int(sum(Fraction(3**(sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2))+sum((q>>1)*r+(q*r*(r-1)>>1) for q, r in p.items())),prod(q**r*factorial(r) for q, r in p.items())) for p in partitions(n))) # _Chai Wah Wu_, Jul 09 2024
print([A004102(n) for n in range(30)])
