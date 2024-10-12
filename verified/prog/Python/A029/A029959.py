from sympy import integer_log
from gmpy2 import digits
def A029959(n):
    if n == 1: return 0
    y = 14*(x:=14**integer_log(n>>1,14)[0])
    return int((c:=n-x)*x+int(digits(c,14)[-2::-1]or'0',14) if n<x+y else (c:=n-y)*y+int(digits(c,14)[-1::-1]or'0',14)) # _Chai Wah Wu_, Jun 14 2024
print([A029959(n) for n in range(1,31)])
