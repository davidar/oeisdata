from sympy import integer_log
from gmpy2 import digits
def A029957(n):
    if n == 1: return 0
    y = 12*(x:=12**integer_log(n>>1,12)[0])
    return int((c:=n-x)*x+int(digits(c,12)[-2::-1]or'0',12) if n<x+y else (c:=n-y)*y+int(digits(c,12)[-1::-1]or'0',12)) # _Chai Wah Wu_, Jun 14 2024
print([A029957(n) for n in range(1,31)])
