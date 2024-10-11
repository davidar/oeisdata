from sympy import prime
def a(n): return sum(map(int, str(prime(n))))
print([a(n) for n in range(1, 80)]) # _Michael S. Branicky_, Feb 03 2021