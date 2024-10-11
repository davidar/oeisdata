from math import isqrt
from sympy.abc import x
from sympy import I, resultant, chebyshevu
def A004003(n): return isqrt(resultant(chebyshevu(n<<1,x/2),chebyshevu(n<<1,I*x/2))) if n else 1 # _Chai Wah Wu_, Nov 07 2023
print([A004003(n) for n in range(30)])
