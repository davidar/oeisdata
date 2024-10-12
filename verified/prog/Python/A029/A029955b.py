from gmpy2 import digits
def A029955(n):
    if n == 1: return 0
    y = 9*(x:=9**(len(digits(n>>1,9))-1))
    return int((c:=n-x)*x+int(digits(c,9)[-2::-1]or'0',9) if n<x+y else (c:=n-y)*y+int(digits(c,9)[-1::-1]or'0',9)) # _Chai Wah Wu_, Jun 14 2024
print([A029955(n) for n in range(1,31)])
