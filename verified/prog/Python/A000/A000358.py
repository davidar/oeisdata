from sympy import totient, lucas, divisors
def A000358(n): return (n&1^1)+sum(totient(n//k)*(lucas(k)-((k&1^1)<<1)) for k in divisors(n,generator=True))//n # _Chai Wah Wu_, Sep 23 2023
print([A000358(n) for n in range(1,31)])
