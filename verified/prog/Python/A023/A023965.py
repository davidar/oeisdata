from sympy import integer_nthroot
def A023965(n): return integer_nthroot(n*10**6,6)[0] % 10 # _Chai Wah Wu_, Nov 14 2022
print([A023965(n) for n in range(1,31)])
