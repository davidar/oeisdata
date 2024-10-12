from math import comb
from sympy import bernoulli
def A000366(n): return (-1 if n&1 else 1)*sum(comb(n,k)*(1-(1<<n+k+1))*bernoulli(n+k+1) for k in range(n+1))>>n-2 if n>1 else 1 # _Chai Wah Wu_, Apr 14 2023
print([A000366(n) for n in range(1,31)])
