from sympy import prime, primerange
def aupton(terms): return [p**3 for p in primerange(1, prime(terms)+1)]
print(aupton(35)) # _Michael S. Branicky_, Aug 27 2021