# requires python 3.2 or higher. Otherwise use def'n of accumulate in python docs.
from itertools import accumulate
A005493_list, blist, b = [], [1], 1
for _ in range(1001):
    blist = list(accumulate([b]+blist))
    b = blist[-1]
    A005493_list.append(blist[-2])
# _Chai Wah Wu_, Sep 02 2014, updated _Chai Wah Wu_, Sep 20 2014
print(A005493_list)
