def A029803(n):
    if n == 1: return 0
    y = (x:=1<<(m:=n.bit_length()-2)-m%3)<<3
    return (c:=n-x)*x+int(oct(c)[-2:1:-1]or'0',8) if n<x+y else (c:=n-y)*y+int(oct(c)[-1:1:-1]or'0',8) # _Chai Wah Wu_, Jun 13 2024
print([A029803(n) for n in range(1,31)])
