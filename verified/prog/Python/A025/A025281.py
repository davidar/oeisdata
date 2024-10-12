from sympy import factorial, factorint
def A025281(n): return sum(p*e for p, e in factorint(factorial(n)).items()) # _Chai Wah Wu_, Apr 09 2021
print([A025281(n) for n in range(30)])
