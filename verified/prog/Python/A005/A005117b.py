from itertools import count, islice
from sympy import factorint
def A005117_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:all(x == 1 for x in factorint(n).values()),count(max(startvalue,1)))
A005117_list = list(islice(A005117_gen(),20)) # _Chai Wah Wu_, May 09 2022
print(A005117_list)
