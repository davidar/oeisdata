from math import prod
def A000178(n): return prod(i**(n-i+1) for i in range(2,n+1)) # _Chai Wah Wu_, Nov 26 2023
print([A000178(n) for n in range(30)])
