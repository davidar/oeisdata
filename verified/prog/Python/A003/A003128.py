# Python 3.2 or higher required
from itertools import accumulate
A003128_list, blist, a, b = [], [1], 1, 1
for _ in range(30):
    blist = list(accumulate([b]+blist))
    c = blist[-1]
    A003128_list.append((c+a-3*b)//2)
    a, b = b, c # _Chai Wah Wu_, Sep 19 2014
print(A003128_list)
