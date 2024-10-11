from itertools import combinations
from math import prod, factorial, gcd
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A000273(n): return int(sum(Fraction(1<<sum(p[r]*p[s]*gcd(r,s)<<1 for r,s in combinations(p.keys(),2))+sum(r*(q*r-1) for q, r in p.items()),prod(q**r*factorial(r) for q, r in p.items())) for p in partitions(n))) # _Chai Wah Wu_, Jul 05 2024
print([A000273(n) for n in range(30)])
