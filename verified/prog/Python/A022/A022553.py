from sympy import mobius, binomial, divisors
def a(n):
    return 1 if n == 0 else sum(mobius(n//d)*binomial(2*d, d) for d in divisors(n))//(2*n)
print([a(n) for n in range(31)]) # _Indranil Ghosh_, Aug 05 2017