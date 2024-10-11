from sympy import integer_nthroot
def A010057(n): return int(integer_nthroot(n,3)[1]) # _Chai Wah Wu_, Apr 02 2021
print([A010057(n) for n in range(30)])
