from sympy import isprime
def ok(n): return isprime(sum(map(int, str(n))))
print(list(filter(ok, range(183)))) # _Michael S. Branicky_, Jun 18 2021