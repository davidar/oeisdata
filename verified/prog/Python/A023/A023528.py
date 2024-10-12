from sympy import prime
def A023528(n): return 0 if n == 1 else (~(m:=prime(n)*prime(n-1)+1)& m-1).bit_length() # _Chai Wah Wu_, Jul 07 2022
print([A023528(n) for n in range(1,31)])
