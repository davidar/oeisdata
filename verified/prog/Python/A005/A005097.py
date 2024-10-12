from sympy import prime
def A005097(n): return prime(n+1)//2 # _Chai Wah Wu_, Jun 04 2022
print([A005097(n) for n in range(1,31)])
