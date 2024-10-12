from sympy import totient, factorial, divisors
def A002619(n): return sum(totient(m:=n//d)**2*factorial(d)*m**d for d in divisors(n,generator=True))//n**2 # _Chai Wah Wu_, Nov 07 2022
print([A002619(n) for n in range(1,31)])
