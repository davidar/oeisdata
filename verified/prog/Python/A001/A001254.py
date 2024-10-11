from sympy import lucas
def a(n):  return lucas(n)**2
print([a(n) for n in range(33)]) # _Michael S. Branicky_, Apr 01 2021