from sympy import isprime
def a(n):
    if isprime(n): return n
    pow10 = 10
    while True:
        t, maxt = n * pow10 + 1, (n+1) * pow10
        while t < maxt:
            if isprime(t): return t
            t += 2
        pow10 *= 10
print([a(n) for n in range(1, 60)]) # _Michael S. Branicky_, Nov 02 2021