from gmpy2 import isqrt
def A018796(n):
    if n == 0:
        return 0
    else:
        d, nd = 1, n
        while True:
            x = (isqrt(nd-1)+1)**2
            if x < nd+d:
                return int(x)
            d *= 10
            nd *= 10 # _Chai Wah Wu_, May 23 2016
print([A018796(n) for n in range(30)])
