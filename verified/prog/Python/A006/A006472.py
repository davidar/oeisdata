from math import factorial
def A006472(n): return n*factorial(n-1)**2 >> n-1 # _Chai Wah Wu_, Jun 22 2022
print([A006472(n) for n in range(1,31)])
