from sympy import binomial, subfactorial
def a(n): return sum([(-1)**(n - k)*binomial(n, k)*subfactorial(2*k) for k in range(n + 1)]) # _Indranil Ghosh_, Apr 28 2017
print([a(n) for n in range(30)])
