from gmpy2 import iroot
def A030697(n):
    d, nd = 10, 10*n**3
    while True:
        x = iroot(nd-1,3)[0]+1
        if not x % 10:
            x += 1
        x = x**3
        if x < nd+d:
            return int(x)
        d *= 10
        nd *= 10 # _Chai Wah Wu_, May 24 2016
print([A030697(n) for n in range(1,31)])
