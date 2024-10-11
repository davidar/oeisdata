from sympy import isprime
def ok(n): s = sum(map(int, str(n))); return s and n%s==0 and isprime(n//s)
print([k for k in range(604) if ok(k)]) # _Michael S. Branicky_, Mar 28 2022