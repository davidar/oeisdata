from itertools import islice, accumulate
def A000756_gen(): # generator of terms
    yield from (1,2)
    blist = (1,2)
    while True:
        yield (blist:=tuple(accumulate(reversed(blist),initial=0)))[-1]
A000756_list = list(islice(A000756_gen(),40)) # _Chai Wah Wu_, Jun 09-11 2022
print(A000756_list)
