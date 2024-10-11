def a(n):
    n = bin(n)[2:]
    x = len(n)
    return sum(int(n[i]) * 4**(x - 1 - i) for i in range(x))
[a(n) for n in range(101)] # _Indranil Ghosh_, Jun 25 2017
print([a(n) for n in range(30)])
