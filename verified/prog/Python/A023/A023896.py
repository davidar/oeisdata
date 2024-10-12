from sympy import totient
def A023896(n): return 1 if n == 1 else n*totient(n)//2 # _Chai Wah Wu_, Apr 08 2022
print([A023896(n) for n in range(1,31)])
