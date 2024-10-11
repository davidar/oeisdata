from math import factorial, comb
def A002720(n): return sum(factorial(k)*comb(n,k)**2 for k in range(n+1)) # _Chai Wah Wu_, Aug 31 2023
print([A002720(n) for n in range(30)])
