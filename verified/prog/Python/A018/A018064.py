from sympy import integer_nthroot
def A018064(n): return -integer_nthroot(m:=7**n, 4)[0]+integer_nthroot(m<<4, 4)[0] # _Chai Wah Wu_, Jun 20 2024
print([A018064(n) for n in range(30)])
