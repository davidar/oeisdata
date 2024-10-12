from __future__ import division
A030056_list, b = [], 1
for n in range(6,501):
    A030056_list.append(b)
    b = b*(2*n+2)*(2*n+3)//((n-5)*(n+8)) # _Chai Wah Wu_, Jan 26 2016
print(A030056_list)
