from sympy import integer_log
from gmpy2 import digits
def A029958(n):
    if n == 1: return 0
    y = 13*(x:=13**integer_log(n>>1,13)[0])
    return int((c:=n-x)*x+int(digits(c,13)[-2::-1]or'0',13) if n<x+y else (c:=n-y)*y+int(digits(c,13)[-1::-1]or'0',13)) # _Chai Wah Wu_, Jun 14 2024
print([A029958(n) for n in range(1,31)])
