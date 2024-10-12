from math import prod, factorial
from sympy import factorint
def A008480(n): return factorial(sum(f:=factorint(n).values()))//prod(map(factorial,f)) # _Chai Wah Wu_, Aug 05 2023
print([A008480(n) for n in range(1,31)])
