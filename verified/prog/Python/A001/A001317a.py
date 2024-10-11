from sympy import binomial
def a(n): return sum([(binomial(n, i)%2)*2**i for i in range(n + 1)]) # _Indranil Ghosh_, Apr 11 2017
print([a(n) for n in range(30)])
