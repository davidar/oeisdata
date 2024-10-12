from gmpy2 import isqrt
def A030688(n):
    d, nd = 10, 10*n**2
    while True:
        x = isqrt(nd-1)+1
        if not x % 10:
            x += 1
        x = x**2
        if x < nd+d:
            return int(x)
        d *= 10
        nd *= 10 # _Chai Wah Wu_, May 24 2016
print([A030688(n) for n in range(1,31)])
