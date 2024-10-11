from gmpy2 import iroot_rem
def A018166(n):
    i,j = iroot_rem(18**n,5)
    return int(i) + int(32*j >= 10*i*(4*i*(2*i*(i + 1) + 1) + 1) + 1) # _Chai Wah Wu_, Aug 18 2016
print([A018166(n) for n in range(30)])
