# requires python 3.2 or higher. Otherwise use def'n of accumulate in python docs.
from itertools import accumulate
A000110, blist, b = [1,1], [1], 1
for _ in range(20):
    blist = list(accumulate([b]+blist))
    b = blist[-1]
    A000110.append(b) # _Chai Wah Wu_, Sep 02 2014, updated _Chai Wah Wu_, Sep 19 2014
print(A000110)
