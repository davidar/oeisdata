from sympy import divisors
def a(n):
    return 0 if n == 0 else sum(((n//d)%2)*d**3 for d in divisors(n))
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 24 2017