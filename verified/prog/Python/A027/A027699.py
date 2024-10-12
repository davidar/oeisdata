from sympy import isprime
def ok(n): return bin(n).count("1")%2 == 0 and isprime(n)
print([k for k in range(812) if ok(k)]) # _Michael S. Branicky_, Jun 27 2022