from sympy import divisors
def A008442(n): return 0 if n&3!=1 else sum(((a:=d&3)==1)-(a==3) for d in divisors(n,generator=True)) # _Chai Wah Wu_, May 17 2023
print([A008442(n) for n in range(1,31)])
