from sympy import prime, composite
def A014237(n):
    return 1 if n == 1 else prime(n)-composite(n-1) # _Chai Wah Wu_, Dec 27 2018
print([A014237(n) for n in range(1,31)])
