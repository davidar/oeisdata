from sympy import totient, n_order, divisors
def A023136(n): return sum(totient(d)//n_order(4,d) for d in divisors(n>>(~n & n-1).bit_length(),generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024
print([A023136(n) for n in range(1,31)])
