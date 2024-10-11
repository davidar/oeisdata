from __future__ import division
A001286_list = [1]
for n in range(2,100):
    A001286_list.append(A001286_list[-1]*n*(n+1)//(n-1)) # _Chai Wah Wu_, Apr 11 2018
print(A001286_list)
