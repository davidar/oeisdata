from sympy.ntheory.factor_ import core
from sympy import integer_nthroot
def A000188(n): return integer_nthroot(n//core(n),2)[0] # _Chai Wah Wu_, Jun 14 2021
print([A000188(n) for n in range(1,31)])
