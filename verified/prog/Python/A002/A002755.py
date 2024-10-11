from sympy import divisors, isprime
from functools import cache
@cache
def T(n, m): # after Indranil Ghosh in A001055
    if isprime(n): return 1 if n <= m else 0
    s = sum(T(n//d, d) for d in divisors(n)[1:-1] if d <= m)
    return s + 1 if n <= m else s
def a(n): return (lambda x: T(x, x))(2**n * 3**6)
print([a(n) for n in range(33)]) # _Michael S. Branicky_, Nov 30 2021