from sympy import divisors
def ok(n): return sum(divisors(n)) > 2*n
print(list(filter(ok, range(1, 271)))) # _Michael S. Branicky_, Aug 29 2021