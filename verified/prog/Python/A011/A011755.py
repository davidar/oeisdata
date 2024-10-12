from sympy import totient
def A011755(n): return sum(k*totient(k) for k in range(1,n+1)) # _Chai Wah Wu_, Feb 21 2023
print([A011755(n) for n in range(1,31)])
