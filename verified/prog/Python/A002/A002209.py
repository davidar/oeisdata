from math import factorial
from fractions import Fraction
from sympy.functions.combinatorial.numbers import stirling
def A002209(n): return (sum(Fraction(stirling(n+1,k+1,kind=1,signed=True),k+1) for k in range(n+1))/factorial(n)).denominator # _Chai Wah Wu_, Jul 09 2023
print([A002209(n) for n in range(30)])
