from math import factorial
def A008906(n): return len(str(factorial(n)).rstrip('0')) # _Chai Wah Wu_, Oct 24 2021
print([A008906(n) for n in range(30)])
