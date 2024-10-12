from itertools import accumulate, islice, count
def A024255_gen(): # generator of terms
    yield from (0,1)
    blist = (0,1)
    for n in count(2):
        yield n*(blist := tuple(accumulate(reversed(tuple(accumulate(reversed(blist),initial=0))),initial=0)))[-1]
A024255_list = list(islice(A024255_gen(),40)) # _Chai Wah Wu_, Jun 09-11 2022
print(A024255_list)
