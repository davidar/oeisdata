from math import factorial
def A000085(n): return sum(factorial(n)//(factorial(n-(k<<1))*factorial(k)*(1<<k)) for k in range((n>>1)+1)) # _Chai Wah Wu_, Aug 31 2023
print([A000085(n) for n in range(30)])
