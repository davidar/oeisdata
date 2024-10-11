# Python 3.2 or higher required.
from itertools import accumulate
A005001_list, blist, a, b = [0,1,2], [1], 2, 1
for _ in range(30):
    blist = list(accumulate([b]+blist))
    b = blist[-1]
    a += b
    A005001_list.append(a) # _Chai Wah Wu_, Sep 19 2014
print(A005001_list)
