# requires python 3.2 or higher. Otherwise use def'n of accumulate in python docs.
from itertools import accumulate
A011971 = blist = [1]
for _ in range(10**2):
    b = blist[-1]
    blist = list(accumulate([b]+blist))
    A011971 += blist # _Chai Wah Wu_, Sep 02 2014, updated _Chai Wah Wu_, Sep 19 2014
print(A011971)
