from sympy import integer_nthroot
def A017979(n): return integer_nthroot(1<<n,3)[0] # _Chai Wah Wu_, Jun 18 2024
print([A017979(n) for n in range(30)])
