from sympy import isprime
def A010051(n): return int(isprime(n)) # _Chai Wah Wu_, Jan 20 2022
print([A010051(n) for n in range(1,31)])
