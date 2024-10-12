from sympy import totient
def A018806(n): return sum(totient(k)*(n//k)**2 for k in range(1,n+1)) # _Chai Wah Wu_, Aug 05 2024
print([A018806(n) for n in range(1,31)])
