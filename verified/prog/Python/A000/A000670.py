from math import factorial
from sympy.functions.combinatorial.numbers import stirling
def A000670(n): return sum(factorial(k)*stirling(n,k) for k in range(n+1)) # _Chai Wah Wu_, Nov 08 2022
print([A000670(n) for n in range(30)])
