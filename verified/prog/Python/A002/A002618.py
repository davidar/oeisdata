from sympy import totient as phi
def a(n): return n*phi(n)
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Mar 16 2022