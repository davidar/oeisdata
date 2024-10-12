def a(n): return int(bin(n)[2:][::-1], 2) # _Indranil Ghosh_, Apr 24 2017
print([a(n) for n in range(30)])
