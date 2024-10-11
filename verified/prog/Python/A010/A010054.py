from sympy import integer_nthroot
def A010054(n): return int(integer_nthroot((n<<3)+1,2)[1]) # _Chai Wah Wu_, Nov 15 2022
print([A010054(n) for n in range(30)])
