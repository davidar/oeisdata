from sympy import prime
def a(n): return (prime(n + 1) + prime(n + 2)) // 2
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jul 11 2017