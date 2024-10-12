from sympy import integer_log
def A006899(n): return 1<<k if integer_log(m:=3**(n-1),6)[0]<(k:=integer_log(3*m,6)[0]) else 3**integer_log(1<<n,6)[0] # _Chai Wah Wu_, Oct 01 2024
print([A006899(n) for n in range(1,31)])
