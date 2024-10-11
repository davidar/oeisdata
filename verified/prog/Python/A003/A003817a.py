def a(n): return 0 if n==0 else 1 + 2*a(int(n/2)) # _Indranil Ghosh_, Apr 28 2017
print([a(n) for n in range(30)])
