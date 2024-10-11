from math import prod
from sympy import prime
def a(n): return prod(prime(i) for i in range((n-1)*n//2+1, n*(n+1)//2+1))
print([a(n) for n in range(1, 14)]) # _Michael S. Branicky_, Feb 15 2021