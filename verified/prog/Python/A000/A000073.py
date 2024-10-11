def a(n, adict={0:0, 1:0, 2:1}):
    if n in adict:
        return adict[n]
    adict[n]=a(n-1)+a(n-2)+a(n-3)
    return adict[n] # _David Nacin_, Mar 07 2012
from functools import cache
@cache
def A000073(n: int) -> int:
    if n <= 1: return 0
    if n == 2: return 1
    return A000073(n-1) + A000073(n-2) + A000073(n-3) # _Peter Luschny_, Nov 21 2022
print([A000073(n) for n in range(30)])
