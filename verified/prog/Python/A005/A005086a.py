from sympy import divisors
from sympy.ntheory.primetest import is_square
def A005086(n): return sum(1 for d in divisors(n,generator=True) if is_square(m:=5*d**2-4) or is_square(m+8)) # _Chai Wah Wu_, Mar 30 2023
print([A005086(n) for n in range(1,31)])
