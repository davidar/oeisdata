from gmpy2 import isqrt
def A003512(n):
    return 2*n + int(isqrt(3*n**2))  # _Chai Wah Wu_, Oct 08 2016
print([A003512(n) for n in range(1,31)])
