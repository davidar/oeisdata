from itertools import accumulate, islice
def A000764_gen(): # generator of terms
    blist, alist = (1,2), (1,)
    yield from blist
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=(alist := list(accumulate(alist, initial=alist[-1])))[-1])))[-1]
A000764_list = list(islice(A000764_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000764_list)
