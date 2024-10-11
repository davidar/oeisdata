# Python 3.2 or higher required.
from itertools import accumulate
A008281_list = blist = [1]
for _ in range(30):
    blist = [0]+list(accumulate(reversed(blist)))
    A008281_list.extend(blist) # _Chai Wah Wu_, Sep 18 2014
print(A008281_list)
