from sympy.ntheory import digits, isprime
def a(n): return sum(sum(digits(n, b)[1:]) for b in range(2, n) if isprime(b))
print([a(n) for n in range(3, 64)]) # _Michael S. Branicky_, Sep 06 2022