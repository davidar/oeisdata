# Python 3.2 or higher required
from itertools import accumulate
A000587, blist, b = [1,-1], [1], -1
for _ in range(30):
    blist = list(accumulate([b]+blist))
    b = -blist[-1]
    A000587.append(b) # _Chai Wah Wu_, Sep 19 2014
print(A000587)
