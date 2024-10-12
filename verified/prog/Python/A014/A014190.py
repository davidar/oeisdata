from gmpy2 import digits
def A014190(n):
    if n == 1: return 0
    y = 3*(x:=3**(len(digits(n>>1,3))-1))
    return int((c:=n-x)*x+int(digits(c,3)[-2::-1]or'0',3) if n<x+y else (c:=n-y)*y+int(digits(c,3)[-1::-1]or'0',3)) # _Chai Wah Wu_, Jun 13 2024
print([A014190(n) for n in range(1,31)])
