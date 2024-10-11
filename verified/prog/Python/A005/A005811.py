def a(n): return bin(n^(n>>1))[2:].count("1") # _Indranil Ghosh_, Apr 29 2017
print([a(n) for n in range(30)])
