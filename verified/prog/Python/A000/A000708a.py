from mpmath import polylog, j, mp
mp.dps=20
def a(n): return -1 if n==0 else int(2*abs(polylog(-n - 1, j)) - 4*abs(polylog(-n, j)))
print([a(n) for n in range(23)])  # _Indranil Ghosh_, Jul 02 2017