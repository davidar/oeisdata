from sympy import prime
def A006254(n): return prime(n+1)+1>>1 # _Chai Wah Wu_, Aug 02 2024
print([A006254(n) for n in range(1,31)])
