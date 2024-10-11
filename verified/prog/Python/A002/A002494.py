from itertools import combinations
from math import prod, factorial, gcd
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A002494(n): return int(sum(Fraction(1<<sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2))+sum((q>>1)*r+(q*r*(r-1)>>1) for q,r in p.items()),prod(q**r*factorial(r) for q,r in p.items())) for p in partitions(n))-sum(Fraction(1<<sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2))+sum((q>>1)*r+(q*r*(r-1)>>1) for q,r in p.items()),prod(q**r*factorial(r) for q,r in p.items())) for p in partitions(n-1))) if n else 1 # _Chai Wah Wu_, Jul 03 2024
print([A002494(n) for n in range(30)])
