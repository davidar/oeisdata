def a(n): return sum([((n>>i)&3==3) for i in range(len(bin(n)[2:]) - 1)]) # _Indranil Ghosh_, Jun 03 2017
print([a(n) for n in range(30)])
