from sympy import isprime, primerange
print([2**n-1 for n in primerange(1, 1001) if isprime(2**n-1)]) # _Karl V. Keller, Jr._, Jul 16 2020