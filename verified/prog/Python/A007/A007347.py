from sympy.core.cache import cacheit
@cacheit
def eulerian2(n, k): return 1 if k==0 else 0 if k==n else eulerian2(n - 1, k)*(k + 1) + eulerian2(n - 1, k - 1)*(2*n - k - 1)
def a(n): return max(eulerian2(n, k) for k in range(n+1))
print([a(n) for n in range(31)]) # _Indranil Ghosh_, Dec 29 2017