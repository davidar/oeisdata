from sympy import integer_log
from gmpy2 import digits
def A029960(n):
    if n == 1: return 0
    y = 15*(x:=15**integer_log(n>>1,15)[0])
    return int((c:=n-x)*x+int(digits(c,15)[-2::-1]or'0',15) if n<x+y else (c:=n-y)*y+int(digits(c,15)[-1::-1]or'0',15)) # _Chai Wah Wu_, Jun 14 2024
print([A029960(n) for n in range(1,31)])
