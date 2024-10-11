from sympy import totient, divisors
def A000031(n): return sum(totient(d)*(1<<n//d) for d in divisors(n,generator=True))//n if n else 1 # _Chai Wah Wu_, Nov 16 2022
print([A000031(n) for n in range(30)])
