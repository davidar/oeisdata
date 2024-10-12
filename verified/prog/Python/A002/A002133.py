from sympy import divisor_count, divisor_sigma
def A002133(n): return sum(divisor_count(j)*divisor_count(n-j) for j in range(1,(n-1>>1)+1)) + ((divisor_count(n+1>>1)**2 if n-1&1 else 0)+divisor_count(n)-divisor_sigma(n)>>1) # _Chai Wah Wu_, Sep 15 2023
print([A002133(n) for n in range(1,31)])
