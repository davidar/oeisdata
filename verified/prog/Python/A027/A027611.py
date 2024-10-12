from sympy import harmonic
def A027611(n): return (n*harmonic(n)).q # _Chai Wah Wu_, Sep 26 2021
print([A027611(n) for n in range(1,31)])
