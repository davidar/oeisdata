from math import factorial
def A014288(n): return sum(factorial(k) for k in range(n+1))>>1 # _Chai Wah Wu_, Nov 01 2023
print([A014288(n) for n in range(30)])
