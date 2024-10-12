from math import isqrt
def A011772(n):
    m = (isqrt(8*n+1)-1)//2
    while (m*(m+1)) % (2*n):
        m += 1
    return m # _Chai Wah Wu_, May 30 2021
print([A011772(n) for n in range(1,31)])
