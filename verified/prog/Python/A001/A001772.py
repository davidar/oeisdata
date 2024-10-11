from sympy import isprime
def aupto(lim): return [k for k in range(1, lim+1) if isprime(11*2**k - 1)]
print(aupto(2500)) # _Michael S. Branicky_, Feb 26 2021