from itertools import count, islice, accumulate
def A000708_gen(): # generator of terms
    yield -1
    blist = (0,1)
    for n in count(2):
        yield -2*blist[-1]+(blist:=tuple(accumulate(reversed(blist),initial=0)))[-1]
A000708_list = list(islice(A000708_gen(),40)) # _Chai Wah Wu_, Jun 09-11 2022
print(A000708_list)
