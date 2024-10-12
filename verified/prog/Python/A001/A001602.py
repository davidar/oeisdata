from sympy.ntheory.generate import prime
def A001602(n):
    a, b, i, p = 0, 1, 1, prime(n)
    while b % p:
        a, b, i = b, (a+b) % p, i+1
    return i # _Chai Wah Wu_, Nov 03 2015, revised Apr 04 2016.
print([A001602(n) for n in range(1,31)])
