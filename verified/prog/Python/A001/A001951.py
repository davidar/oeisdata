from sympy import integer_nthroot
def A001951(n): return integer_nthroot(2*n**2,2)[0] # _Chai Wah Wu_, Mar 16 2021
print([A001951(n) for n in range(30)])
