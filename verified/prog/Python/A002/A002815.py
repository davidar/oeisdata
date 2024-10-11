from sympy import primerange
def A002815(n): return n+(n+1)*len(p:=list(primerange(n+1)))-sum(p) # _Chai Wah Wu_, Jan 01 2024
print([A002815(n) for n in range(30)])
