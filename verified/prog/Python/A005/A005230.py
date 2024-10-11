from itertools import count, islice
from math import isqrt
def A005230_gen(): # generator of terms
    blist = [1]
    for n in count(1):
        yield blist[-1]
        blist.append(sum(blist[-i] for i in range(1,(isqrt(8*n)+3)//2)))
A005230_list = list(islice(A005230_gen(),30)) # _Chai Wah Wu_, Feb 02 2022
print(A005230_list)
