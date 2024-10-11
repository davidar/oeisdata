from sympy import isprime
def ok(n): return pow(7, n-1, n) == 1 and not isprime(n)
print(list(filter(ok, range(1, 34000)))) # _Michael S. Branicky_, Jun 25 2021