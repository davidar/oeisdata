from math import isqrt
def A010815(n):
    m = isqrt(24*n+1)
    return 0 if m**2 != 24*n+1 else ((-1)**((m-1)//6) if m % 6 == 1 else (-1)**((m+1)//6)) # _Chai Wah Wu_, Sep 08 2021
print([A010815(n) for n in range(30)])
