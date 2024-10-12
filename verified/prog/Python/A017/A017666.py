from math import gcd
from sympy import divisor_sigma
def A017666(n): return n//gcd(divisor_sigma(n),n) # _Chai Wah Wu_, Mar 21 2023
print([A017666(n) for n in range(1,31)])
