from sympy import integer_nthroot
def A023963(n): return integer_nthroot(n*10**4,4)[0]%10 # _Chai Wah Wu_, Feb 27 2023
print([A023963(n) for n in range(1,31)])
