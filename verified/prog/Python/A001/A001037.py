from sympy import divisors, mobius
def a(n): return sum(mobius(d) * 2**(n//d) for d in divisors(n))/n if n>1 else n + 1 # _Indranil Ghosh_, Apr 26 2017
print([a(n) for n in range(30)])
