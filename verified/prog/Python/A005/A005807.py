from __future__ import division
A005807_list, b = [], 2
for n in range(10**3):
    A005807_list.append(b)
    b = b*(4*n+2)*(5*n+9)//((n+3)*(5*n+4)) # _Chai Wah Wu_, Jan 28 2016
print(A005807_list)
