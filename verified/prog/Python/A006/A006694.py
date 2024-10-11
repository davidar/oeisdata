from sympy import totient, n_order, divisors
def A006694(n): return sum(totient(d)//n_order(2,d) for d in divisors((n+1<<1)-1,generator=True) if d>1) # _Chai Wah Wu_, Apr 09 2024
print([A006694(n) for n in range(30)])
