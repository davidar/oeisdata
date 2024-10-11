from math import factorial, comb
def A002464(n): return factorial(n)+sum((-1 if k&1 else 1)*factorial(n-k)*sum(comb(k-1,t-1)*comb(n-k,t)<<t for t in range(1,k+1)) for k in range(1,n+1)) # _Chai Wah Wu_, Feb 19 2024
print([A002464(n) for n in range(30)])
