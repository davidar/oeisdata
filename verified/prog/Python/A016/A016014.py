from sympy import isprime
def a(n):
    k = 1
    while not isprime(2*n*k + 1): k += 1
    return k
print([a(n) for n in range(1, 100)]) # _Michael S. Branicky_, Mar 28 2022