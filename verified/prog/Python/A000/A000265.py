from __future__ import division
def A000265(n):
    while not n % 2:
        n //= 2
    return n # _Chai Wah Wu_, Mar 25 2018
print([A000265(n) for n in range(1,31)])
