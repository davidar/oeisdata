from sympy import integer_nthroot
def A018025(n): return -integer_nthroot(m:=17**n,3)[0]+integer_nthroot(m<<3,3)[0] # _Chai Wah Wu_, Jun 18 2024
print([A018025(n) for n in range(30)])
