from itertools import combinations
from math import prod, gcd, factorial
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A004106(n): return int(sum(Fraction(3**(sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2) if not (r&1 and s&1))+sum(((q>>1)&-2)*r+(q*r*(r-1)>>1) for q, r in p.items() if q&1^1))<<s,prod(q**r*factorial(r) for q, r in p.items())) for s, p in partitions(n,size=True))) # _Chai Wah Wu_, Jul 10 2024
print([A004106(n) for n in range(30)])
