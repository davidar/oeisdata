def a014081(n): return sum([((n>>i)&3==3) for i in range(len(bin(n)[2:]) - 1)])
def a(n): return (-1)**a014081(n) # _Indranil Ghosh_, Jun 03 2017
print([a(n) for n in range(30)])
