def A022290(n):
    a, b, s = 1,2,0
    for i in bin(n)[-1:1:-1]:
        s += int(i)*a
        a, b = b, a+b
    return s # _Chai Wah Wu_, Sep 10 2022
print([A022290(n) for n in range(30)])
