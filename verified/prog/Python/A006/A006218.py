from sympy import integer_nthroot
def A006218(n): return 2*sum(n//k for k in range(1,integer_nthroot(n,2)[0]+1))-integer_nthroot(n,2)[0]**2 # _Chai Wah Wu_, Mar 29 2021
print([A006218(n) for n in range(30)])
