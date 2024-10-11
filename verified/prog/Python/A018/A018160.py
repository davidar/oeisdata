from gmpy2 import iroot_rem
def A018160(n):
    i, j = iroot_rem(1<<(n<<2),5)
    return int(i)+int(j<<5>=10*i*((i*((i*(i+1)<<1)+1)<<2)+1)+1) # _Chai Wah Wu_, Jun 20 2024
print([A018160(n) for n in range(30)])
