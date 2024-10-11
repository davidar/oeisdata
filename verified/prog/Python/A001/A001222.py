from sympy import primeomega
def a(n): return primeomega(n)
print([a(n) for n in range(1, 112)]) # _Michael S. Branicky_, Apr 30 2022