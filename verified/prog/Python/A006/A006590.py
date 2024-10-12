from math import isqrt
def A006590(n): return (lambda m: n+2*sum((n-1)//k for k in range(1, m+1))-m*m)(isqrt(n-1)) # _Chai Wah Wu_, Oct 09 2021
print([A006590(n) for n in range(1,31)])
