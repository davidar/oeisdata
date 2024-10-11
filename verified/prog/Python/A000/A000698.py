from sympy import factorial2, cacheit
@cacheit
def a(n): return 1 if n == 0 else factorial2(2*n - 1) - sum(factorial2(2*k - 1)*a(n - k) for k in range(1, n))
[a(n) for n in range(51)]  # _Indranil Ghosh_, Jul 18 2017
print([a(n) for n in range(30)])
