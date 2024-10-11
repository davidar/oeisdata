from itertools import islice, accumulate
def A000667_gen(): # generator of terms
    blist = tuple()
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=1)))[-1]
A000667_list = list(islice(A000667_gen(),20)) # _Chai Wah Wu_, Jun 11 2022
print(A000667_list)
