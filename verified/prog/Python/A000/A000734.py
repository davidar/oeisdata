from itertools import count, accumulate, islice
def A000734_gen(): # generator of terms
    yield 1
    blist, m = (1,), 1
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=m)))[-1]
        m *= 2
A000734_list = list(islice(A000734_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000734_list)
