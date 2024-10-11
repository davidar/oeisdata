from sympy import binomial, fibonacci
def a(n): return sum((-1)**(k - 1)*binomial(3*n, n - k)*k//n*fibonacci(k - 2) for k in range(1, n + 1))
print([a(n) for n in range(1, 21)]) # _Indranil Ghosh_, Aug 05 2017