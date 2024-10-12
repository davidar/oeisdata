from sympy import integer_nthroot
def A007412(n): return n+(k:=integer_nthroot(n,3)[0])+int(n>=(k+1)**3-k) # _Chai Wah Wu_, Jun 17 2024
print([A007412(n) for n in range(1,31)])
