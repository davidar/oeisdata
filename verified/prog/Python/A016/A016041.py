from sympy import isprime
def ok(n): return isprime(n) and (b:=bin(n)[2:]) == b[::-1]
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Apr 20 2024