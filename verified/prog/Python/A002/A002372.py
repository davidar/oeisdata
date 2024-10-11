from sympy import isprime, primerange
def a(n): return sum([1 for p in primerange(3, 2*n-2) if isprime(2*n-p)])
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 23 2017