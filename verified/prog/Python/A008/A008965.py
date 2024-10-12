from sympy import totient, divisors
def A008965(n): return sum(totient(d)*(1<<n//d) for d in divisors(n, generator=True))//n-1 # _Chai Wah Wu_, Sep 23 2023
print([A008965(n) for n in range(1,31)])
