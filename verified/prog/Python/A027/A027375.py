from sympy import mobius, divisors
def a(n): return sum(mobius(d)*2**(n//d) for d in divisors(n))
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 28 2017