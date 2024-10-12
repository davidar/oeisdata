from itertools import count
from sympy.ntheory.factor_ import digits
def A016026(n): return next(b for b in count(2) if (s := digits(n,b)[1:])[:(t:=len(s)+1>>1)]==s[:-t-1:-1]) # _Chai Wah Wu_, Jan 17 2024
print([A016026(n) for n in range(1,31)])
