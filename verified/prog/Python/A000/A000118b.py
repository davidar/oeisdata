from sympy import divisor_sigma
def A000118(n): return 1 if n == 0 else 8*divisor_sigma(n) if n % 2 else 24*divisor_sigma(int(bin(n)[2:].rstrip('0'),2)) # _Chai Wah Wu_, Jun 27 2022
print([A000118(n) for n in range(30)])
