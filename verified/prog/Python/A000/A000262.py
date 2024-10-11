from sympy import hyper, hyperexpand
def A000262(n): return hyperexpand(hyper((-n+1, -n), [], 1)) # _Chai Wah Wu_, Jan 14 2022
print([A000262(n) for n in range(30)])
