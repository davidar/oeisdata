from __future__ import division
A000984_list, b = [1], 1
for n in range(10**3):
    b = b*(4*n+2)//(n+1)
    A000984_list.append(b) # _Chai Wah Wu_, Mar 04 2016
print(A000984_list)
