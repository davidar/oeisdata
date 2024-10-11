# requires python 3.2 or higher
from itertools import accumulate
A000111_list, blist = [1,1], [1]
for n in range(10**2):
    blist = list(reversed(list(accumulate(reversed(blist))))) + [0] if n % 2 else [0]+list(accumulate(blist))
    A000111_list.append(sum(blist)) # _Chai Wah Wu_, Jan 29 2015
print(A000111_list)
