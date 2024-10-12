from sympy import isprime
def ok(n): return isprime(int(str(n)+str(n+1)))
print([k for k in range(500) if ok(k)]) # _Michael S. Branicky_, Apr 19 2023