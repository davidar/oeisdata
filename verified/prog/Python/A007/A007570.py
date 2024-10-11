from sympy import fibonacci
def a(n): return fibonacci(fibonacci(n))
print([a(n) for n in range(15)]) # _Michael S. Branicky_, Feb 02 2022