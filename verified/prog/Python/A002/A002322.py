from sympy import reduced_totient
def A002322(n): return reduced_totient(n) # _Chai Wah Wu_, Feb 24 2021
print([A002322(n) for n in range(1,31)])
