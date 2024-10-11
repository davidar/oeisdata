from math import factorial
def A001710(n): return factorial(n)>>1 if n > 1 else 1 # _Chai Wah Wu_, Feb 14 2023
print([A001710(n) for n in range(30)])
