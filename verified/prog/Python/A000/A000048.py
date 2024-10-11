from sympy import divisors, mobius
def a(n): return 1 if n<1 else sum(mobius(d)*2**(n//d) for d in divisors(n) if d%2)//(2*n) # _Indranil Ghosh_, Apr 28 2017
print([a(n) for n in range(30)])
