from sympy import binomial
def F(n,c): return binomial(2*n - c, c - 1)/c
print([int(round(sum([F(n, 2*r + 1) for r in range(n//2 + 1)]))) for n in range(1, 41)]) # _Indranil Ghosh_, Apr 01 2017