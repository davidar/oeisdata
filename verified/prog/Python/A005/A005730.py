from math import prod
from sympy import isprime, primefactors
def A005730(n): return 1 if isprime(n) else prod(primefactors(n))<<(not n%6) # _Chai Wah Wu_, Mar 10 2024
print([A005730(n) for n in range(1,31)])
