from math import isqrt
from sympy.ntheory.continued_fraction import continued_fraction_periodic
def A013943(n): return len(continued_fraction_periodic(0,1,n+(k:=isqrt(n))+int(n>=k*(k+1)+1))[-1]) # _Chai Wah Wu_, Jul 20 2024
print([A013943(n) for n in range(1,31)])
