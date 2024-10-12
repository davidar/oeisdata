from sympy import integer_nthroot
def A011273(n): return integer_nthroot(9*10**(19*(n-1)),19)[0] % 10 # _Chai Wah Wu_, Mar 07 2022
print([A011273(n) for n in range(1,31)])
