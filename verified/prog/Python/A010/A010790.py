from math import factorial
def A010790(n): return factorial(n)**2*(n+1) # _Chai Wah Wu_, Apr 22 2024
print([A010790(n) for n in range(30)])
