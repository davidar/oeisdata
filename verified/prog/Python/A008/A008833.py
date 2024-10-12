from sympy.ntheory.factor_ import core
def A008833(n): return n//core(n) # _Chai Wah Wu_, Dec 30 2021
print([A008833(n) for n in range(1,31)])
