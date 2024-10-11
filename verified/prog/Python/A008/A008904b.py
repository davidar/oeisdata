from functools import reduce
from sympy.ntheory.factor_ import digits
def A008904(n): return reduce(lambda x,y:x*y%10,(((6,2,4,8,6,2,4,8,2,4,8,6,6,2,4,8,4,8,6,2)[(a<<2)|(i*a&3)] if i*a else (1,1,2,6,4)[a]) for i, a in enumerate(digits(n,5)[-1:0:-1])),6) if n>1 else 1 # _Chai Wah Wu_, Dec 07 2023
print([A008904(n) for n in range(30)])
