from __future__ import division
A001700_list, b = [], 1
for n in range(10**3):
    A001700_list.append(b)
    b = b*(4*n+6)//(n+2) # _Chai Wah Wu_, Jan 26 2016
print(A001700_list)
