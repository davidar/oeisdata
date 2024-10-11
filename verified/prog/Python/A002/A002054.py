from __future__ import division
A002054_list, b = [], 1
for n in range(1,10**3):
    A002054_list.append(b)
    b = b*(2*n+2)*(2*n+3)//(n*(n+3)) # _Chai Wah Wu_, Jan 26 2016
print(A002054_list)
