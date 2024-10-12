from gmpy2 import digits
from sympy import integer_log
def A029954(n):
    if n == 1: return 0
    y = 7*(x:=7**integer_log(n>>1,7)[0])
    return int((c:=n-x)*x+int(digits(c,7)[-2::-1]or'0',7) if n<x+y else (c:=n-y)*y+int(digits(c,7)[-1::-1]or'0',7)) # _Chai Wah Wu_, Jun 14 2024
print([A029954(n) for n in range(1,31)])
