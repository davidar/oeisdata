from sympy import totient, n_order, divisors
def A000374(n): return sum(totient(d)//n_order(2,d) for d in divisors(n>>(~n & n-1).bit_length(),generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024
print([A000374(n) for n in range(1,31)])
