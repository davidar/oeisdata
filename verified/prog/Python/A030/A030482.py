from sympy import primerange
from itertools import groupby
def ok(n): return len([k for k, g in groupby([int(d in "13579") for d in str(n)])]) <= 2
def aupto(limit): return [p for p in primerange(2, limit+1) if ok(p**3)]
print(aupto(201673)) # _Michael S. Branicky_, Mar 27 2021