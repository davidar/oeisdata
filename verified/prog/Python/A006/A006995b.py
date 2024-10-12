def A006995(n):
    if n == 1: return 0
    a = 1<<(l:=n.bit_length()-2)
    m = a|(n&a-1)
    return (m<<l+1)+int(bin(m)[-1:1:-1]or'0',2) if a&n else (m<<l)+int(bin(m)[-2:1:-1]or'0',2) # _Chai Wah Wu_, Jun 10 2024
print([A006995(n) for n in range(1,31)])
