def A029730(n):
    if n == 1: return 0
    y = (x:=1<<(n.bit_length()-2&-4))<<4
    return (c:=n-x)*x+int(hex(c)[-2:1:-1]or'0',16) if n<x+y else (c:=n-y)*y+int(hex(c)[-1:1:-1]or'0',16) # _Chai Wah Wu_, Jun 13 2024
print([A029730(n) for n in range(1,31)])
