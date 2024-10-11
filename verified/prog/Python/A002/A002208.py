from math import factorial
from fractions import Fraction
from sympy.functions.combinatorial.numbers import stirling
def A002208(n): return (-1 if n&1 else 1)*(sum(Fraction(stirling(n+1,k+1,kind=1,signed=True),k+1) for k in range(n+1))/factorial(n)).numerator # _Chai Wah Wu_, Jul 09 2023
print([A002208(n) for n in range(30)])
