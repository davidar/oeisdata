from sympy import primepi, integer_nthroot
def A025528(n): return sum(primepi(integer_nthroot(n,k)[0]) for k in range(1,n.bit_length())) # _Chai Wah Wu_, Aug 15 2024
print([A025528(n) for n in range(1,31)])
