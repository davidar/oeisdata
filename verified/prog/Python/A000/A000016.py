from sympy import totient, divisors
def A000016(n): return sum(totient(d)<<n//d-1 for d in divisors(n>>(~n&n-1).bit_length(),generator=True))//n if n else 1 # _Chai Wah Wu_, Feb 21 2023
print([A000016(n) for n in range(30)])
