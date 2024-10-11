from math import comb, factorial
def A000179(n): return 1 if n == 0 else sum((-2*n if k & 1 else 2*n)*comb(m:=2*n-k,k)*factorial(n-k)//m for k in range(n+1)) # _Chai Wah Wu_, May 27 2022
print([A000179(n) for n in range(30)])
