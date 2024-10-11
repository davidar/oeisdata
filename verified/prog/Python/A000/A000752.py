from itertools import accumulate, islice
def A000752_gen(): # generator of terms
    blist, m = tuple(), 1
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=m)))[-1]
        m *= 2
A000752_list = list(islice(A000752_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000752_list)
