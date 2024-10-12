from gmpy2 import digits
def A014192(n):
    if n == 1: return 0
    y = (x:=1<<(n.bit_length()-2&-2))<<2
    return (c:=n-x)*x+int(digits(c,4)[-2::-1]or'0',4) if n<x+y else (c:=n-y)*y+int(digits(c,4)[-1::-1]or'0',4) # _Chai Wah Wu_, Jun 14 2024
print([A014192(n) for n in range(1,31)])
