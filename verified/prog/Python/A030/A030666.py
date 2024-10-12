from gmpy2 import isqrt
def A030666(n):
    d, nd = 10, 10*n
    while True:
        x = (isqrt(nd-1)+1)**2
        if x < nd+d:
            return int(x)
        d *= 10
        nd *= 10 # _Chai Wah Wu_, May 24 2016
print([A030666(n) for n in range(1,31)])
