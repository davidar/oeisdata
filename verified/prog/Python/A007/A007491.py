from sympy import nextprime
def a(n): return nextprime(n**2)
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Jan 13 2023