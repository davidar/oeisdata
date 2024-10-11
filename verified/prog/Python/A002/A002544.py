from sympy import binomial
def a(n): return binomial(2*n + 1, n)*(n + 1)**2 # _Indranil Ghosh_, Apr 18 2017
print([a(n) for n in range(30)])
