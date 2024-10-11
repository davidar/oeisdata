from sympy import prime
def a(n): return 2**prime(n)-1
print([a(n) for n in range(1, 21)]) # _Michael S. Branicky_, Mar 28 2022