from math import factorial
def A001813(n): return factorial(n<<1)//factorial(n) # _Chai Wah Wu_, Feb 14 2023
print([A001813(n) for n in range(30)])
