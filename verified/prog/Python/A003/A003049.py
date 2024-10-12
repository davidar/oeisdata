from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from math import prod, gcd, factorial
from sympy import mobius, divisors
from sympy.utilities.iterables import partitions
def A003049(n):
    @lru_cache(maxsize=None)
    def b(n): return int(sum(Fraction(1<<sum(p[r]*p[s]*gcd(r,s) for r,s in combinations(p.keys(),2))+sum(((q>>1)-1)*r+(q*r*(r-1)>>1) for q, r in p.items())+any(q&1 for q in p),prod(q**r*factorial(r) for q, r in p.items())) for p in partitions(n)))
    @lru_cache(maxsize=None)
    def c(n): return n*b(n)-sum(c(k)*b(n-k) for k in range(1,n))
    return sum(mobius(n//d)*c(d) for d in divisors(n,generator=True))//n # _Chai Wah Wu_, Jul 03 2024
print([A003049(n) for n in range(1,31)])
