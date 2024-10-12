from itertools import combinations
from math import prod, gcd, factorial
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A001374(n): return int(sum(Fraction(1<<((sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2))<<1)+sum(q*r**2 for q, r in p.items())<<1),prod(q**r*factorial(r) for q, r in p.items())) for p in partitions(n))) # _Chai Wah Wu_, Jul 10 2024
print([A001374(n) for n in range(1,31)])
