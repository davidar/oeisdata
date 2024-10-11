from sympy import nextprime
def A007918(n): return nextprime(n-1) # _Chai Wah Wu_, Apr 22 2022
print([A007918(n) for n in range(30)])
