from itertools import accumulate, count, islice
def A000660_gen(): # generator of terms
    yield 1
    blist = (1,)
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=i)))[-1]
A000660_list = list(islice(A000660_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000660_list)
