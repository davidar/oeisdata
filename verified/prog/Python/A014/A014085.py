from sympy import primepi
def a(n): return primepi((n+1)**2) - primepi(n**2)
print([a(n) for n in range(81)]) # _Michael S. Branicky_, Jul 05 2021