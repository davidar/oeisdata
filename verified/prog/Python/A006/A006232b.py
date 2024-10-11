from fractions import Fraction
from sympy.functions.combinatorial.numbers import stirling
def A006232(n): return sum(Fraction(stirling(n,k,kind=1,signed=True),k+1) for k in range(n+1)).numerator # _Chai Wah Wu_, Jul 09 2023
print([A006232(n) for n in range(30)])
