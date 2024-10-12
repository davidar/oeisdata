from sympy import prime, primerange
def a(n): return sum(p*p for p in primerange(1, prime(n)+1))
print([a(n) for n in range(1, 40)]) # _Michael S. Branicky_, Apr 13 2021