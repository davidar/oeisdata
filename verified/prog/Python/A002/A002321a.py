from sympy import mobius
def M(n): return sum(mobius(k) for k in range(1,n + 1))
print([M(n) for n in range(1, 151)]) # _Indranil Ghosh_, Mar 18 2017