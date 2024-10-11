from sympy import isprime
def ok(n): return n > 3 and not isprime(n) and not isprime(n-1)
print([k for k in range(122) if ok(k)]) # _Michael S. Branicky_, Dec 26 2021