from itertools import accumulate, islice
def A001250_gen(): # generator of terms
    yield from (1,1)
    blist = (0,2)
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=0)))[-1]
A001250_list = list(islice(A001250_gen(),40)) # _Chai Wah Wu_, Jun 09-11 2022
print(A001250_list)
