from itertools import product
from math import prod, factorial, gcd
from fractions import Fraction
from sympy.utilities.iterables import partitions
def A001173(n): return int(sum(Fraction(1<<sum(p[r]*p[s]*gcd(r,s) for r,s in product(p.keys(),repeat=2)),prod(q**p[q]*factorial(p[q]) for q in p)) for p in partitions(n)))>>1 # _Chai Wah Wu_, Jul 02 2024
print([A001173(n) for n in range(1,31)])
