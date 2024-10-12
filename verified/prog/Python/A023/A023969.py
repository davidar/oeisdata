from gmpy2 import isqrt_rem
def A023969(n):
    i, j = isqrt_rem(n)
    return int(4*(j-i) >= 1) # _Chai Wah Wu_, Aug 16 2016
print([A023969(n) for n in range(30)])
