from sympy import isprime, primitive_root
from itertools import count, islice
def f(n): return 0 if not isprime(n) or (r:=primitive_root(n))==None else r
def agen(r=0): yield from ((m, r:=f(m))[0] for m in count(1) if f(m) > r)
print(list(islice(agen(), 15))) # _Michael S. Branicky_, Feb 13 2023