from itertools import accumulate, count, islice
from functools import reduce
def A007729_gen(): # generator of terms
    return accumulate(sum(reduce(lambda x,y:(x[0],x[0]+x[1]) if int(y) else (x[0]+x[1],x[1]),bin(n)[-1:2:-1],(1,0))) for n in count(1))
A007729_list = list(islice(A007729_gen(),30)) # _Chai Wah Wu_, May 07 2023
print(A007729_list)
