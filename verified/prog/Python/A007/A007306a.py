from sympy import binomial
def a(n):
    return 1 if n<1 else sum(binomial(n + k - 1, 2*k) % 2 for k in range(n + 1))
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Mar 22 2017