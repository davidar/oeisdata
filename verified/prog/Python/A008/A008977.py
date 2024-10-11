from math import factorial
def A008977(n): return factorial(n<<2)//factorial(n)**4 # _Chai Wah Wu_, Mar 15 2023
print([A008977(n) for n in range(30)])
