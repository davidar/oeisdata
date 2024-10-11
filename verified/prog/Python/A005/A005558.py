from sympy import ceiling as c, binomial
def a(n):
    return binomial(n + 1, c(n/2))*binomial(n, n//2) - binomial(n + 1, c((n - 1)/2))*binomial(n, (n - 1)//2)
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Jul 02 2017