from sympy import factorint
def valp(n, p):
    s = 0
    while n: n //= p; s += n
    return s
def K(p, e):
    if e <= p: return e*p
    t = e*(p-1)//p*p
    while valp(t, p) < e: t += p
    return t
def A002034(n):
    return 1 if n == 1 else max(K(p, e) for p, e in factorint(n).items())
print([A002034(n) for n in range(1, 85)]) # _Michael S. Branicky_, Jun 09 2022 after _Charles R Greathouse IV_