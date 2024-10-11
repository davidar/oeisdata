from sympy import integer_nthroot
def A018010(n): return -integer_nthroot(m:=3**n<<(n<<1),3)[0]+integer_nthroot(m<<3,3)[0] # _Chai Wah Wu_, Jun 18 2024
print([A018010(n) for n in range(30)])
