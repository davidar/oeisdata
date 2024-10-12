from math import gcd
from sympy import divisor_sigma
def A017665(n): return (m:=divisor_sigma(n))//gcd(m,n) # _Chai Wah Wu_, Mar 20 2023
print([A017665(n) for n in range(1,31)])
