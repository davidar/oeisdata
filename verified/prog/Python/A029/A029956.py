from gmpy2 import digits
from sympy import integer_log
def A029956(n):
    if n == 1: return 0
    y = 11*(x:=11**integer_log(n>>1,11)[0])
    return int((c:=n-x)*x+int(digits(c,11)[-2::-1]or'0',11) if n<x+y else (c:=n-y)*y+int(digits(c,11)[-1::-1]or'0',11)) # _Chai Wah Wu_, Jun 14 2024
print([A029956(n) for n in range(1,31)])
