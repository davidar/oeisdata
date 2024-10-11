from itertools import count, islice
from sympy import primefactors
def A009003_gen(): # generator of terms
    return filter(lambda n:any(map(lambda p: p % 4 == 1,primefactors(n))),count(1))
A009003_list = list(islice(A009003_gen(),20)) # _Chai Wah Wu_, Jun 22 2022
print(A009003_list)
