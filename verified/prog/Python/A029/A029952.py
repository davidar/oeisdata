from gmpy2 import digits
def A029952(n):
    if n == 1: return 0
    y = 5*(x:=5**(len(digits(n>>1,5))-1))
    return int((c:=n-x)*x+int(digits(c,5)[-2::-1]or'0',5) if n<x+y else (c:=n-y)*y+int(digits(c,5)[-1::-1]or'0',5)) # _Chai Wah Wu_, Jun 13 2024
print([A029952(n) for n in range(1,31)])
