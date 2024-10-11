from math import prod, factorial
def A005130(n): return prod(factorial(3*k+1) for k in range(n))//prod(factorial(n+k) for k in range(n)) # _Chai Wah Wu_, Feb 02 2022
print([A005130(n) for n in range(30)])
