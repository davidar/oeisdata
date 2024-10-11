from sympy import integer_nthroot
def A018178(n): return -integer_nthroot(m:=11**n<<n, 5)[0]+integer_nthroot(m<<5, 5)[0] # _Chai Wah Wu_, Jun 20 2024
print([A018178(n) for n in range(30)])
