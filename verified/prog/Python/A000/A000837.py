from sympy import npartitions, mobius, divisors
def a(n): return 1 if n==0 else sum(mobius(n//d)*npartitions(d) for d in divisors(n)) # _Indranil Ghosh_, Apr 26 2017
print([a(n) for n in range(30)])
