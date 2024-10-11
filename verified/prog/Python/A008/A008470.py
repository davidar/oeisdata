from sympy import isprime
def ok(m): return sum(isprime(10*m+i) for i in [1, 3, 7, 9]) >= 3
print(list(filter(ok, range(700)))) # _Michael S. Branicky_, Sep 12 2021