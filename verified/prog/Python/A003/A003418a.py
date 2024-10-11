from functools import reduce
from operator import mul
from sympy import sieve
def integerlog(n,b): # find largest integer k>=0 such that b^k <= n
    kmin, kmax = 0,1
    while b**kmax <= n:
        kmax *= 2
    while True:
        kmid = (kmax+kmin)//2
        if b**kmid > n:
            kmax = kmid
        else:
            kmin = kmid
        if kmax-kmin <= 1:
            break
    return kmin
def A003418(n):
    return reduce(mul,(p**integerlog(n,p) for p in sieve.primerange(1,n+1)),1) # _Chai Wah Wu_, Mar 13 2021
print([A003418(n) for n in range(30)])
