from sympy import divisors
def a(n): return 1 if n==0 else 24*sum(d for d in divisors(n) if d%2)
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 24 2017