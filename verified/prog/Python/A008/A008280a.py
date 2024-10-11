# Python 3.2 or higher required.
from itertools import accumulate
A008280_list = blist = [1]
for n in range(10):
    blist = list(reversed(list(accumulate(reversed(blist))))) + [0] if n % 2 else [0]+list(accumulate(blist))
    A008280_list.extend(blist)
print(A008280_list) # Chai Wah Wu, Sep 20 2014