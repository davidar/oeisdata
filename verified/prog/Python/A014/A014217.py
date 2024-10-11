from sympy import floor, sqrt
def A014217(n): return floor(((1+sqrt(5))/2)**n) # _Chai Wah Wu_, Dec 17 2021
print([A014217(n) for n in range(30)])
