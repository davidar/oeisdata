from itertools import count, islice
from math import prod
def A029781_gen(): # generator of terms
    return map(lambda x:x[1], filter(lambda x:set(str(x[0])) <= set(str(x[1])) & set(str(prod(x))),((n,n**2) for n in count(0))))
A029781_list = list(islice(A029781_gen(),20)) # _Chai Wah Wu_, Apr 03 2023
print(A029781_list)
