from itertools import count, islice
def A003422_gen(): # generator of terms
    yield from (0,1)
    c, f = 1, 1
    for n in count(1):
        yield (c:= c + (f:= f*n))
A003422_list = list(islice(A003422_gen(),20)) # _Chai Wah Wu_, Jun 22 2022
print(A003422_list)
