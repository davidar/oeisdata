from itertools import count
from sympy import nextprime
def A005729(n):
    c, p = 1, 2
    while p < n:
        if n%p:
            for m in count(2):
                if (p**m-1)//(p-1) > n:
                    break
                for r in count(1):
                    q = (p**(m*r)-1)//(p**r-1)
                    if q > n:
                        break
                    if not n % q:
                        c *= p
                        break
                else:
                    continue
                if q <= n:
                    break
        else:
            c *= p if p&1 or n%6 else p**2
        p = nextprime(p)
    return c # _Chai Wah Wu_, Mar 10 2024
print([A005729(n) for n in range(1,31)])
