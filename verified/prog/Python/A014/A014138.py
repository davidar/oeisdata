from __future__ import division
A014138_list, b, s = [0], 1, 0
for n in range(1,10**2):
    s += b
    A014138_list.append(s)
    b = b*(4*n+2)//(n+2) # _Chai Wah Wu_, Jan 28 2016
print(A014138_list)
