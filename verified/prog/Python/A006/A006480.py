from math import factorial
def A006480(n): return factorial(3*n)//factorial(n)**3 # _Chai Wah Wu_, Oct 04 2022
print([A006480(n) for n in range(30)])
