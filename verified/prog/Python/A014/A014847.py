from __future__ import division
A014847_list, b = [], 1
for n in range(1,10**3):
    if not b % n:
        A014847_list.append(n)
    b = b*(4*n+2)//(n+2) # _Chai Wah Wu_, Jan 27 2016
print(A014847_list)
