from sympy import fibonacci
def A001595(n): return (fibonacci(n+1)<<1)-1 # _Chai Wah Wu_, Sep 10 2024
print([A001595(n) for n in range(30)])
