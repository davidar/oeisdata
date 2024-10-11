def A020968(n): return (3*7**(n+2)-4*8**(n + 2)+11**(n+2))//12 # _Indranil Ghosh_, Feb 28 2017
print([A020968(n) for n in range(30)])
