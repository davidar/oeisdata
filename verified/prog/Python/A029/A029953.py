from gmpy2 import digits
from sympy import integer_log
def A029953(n):
    if n == 1: return 0
    y = 6*(x:=6**integer_log(n>>1,6)[0])
    return int((c:=n-x)*x+int(digits(c,6)[-2::-1]or'0',6) if n<x+y else (c:=n-y)*y+int(digits(c,6)[-1::-1]or'0',6)) # _Chai Wah Wu_, Jun 14 2024
print([A029953(n) for n in range(1,31)])
