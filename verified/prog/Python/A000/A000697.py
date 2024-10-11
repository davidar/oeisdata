from itertools import accumulate, count, islice
def A000697_gen(): # generator of terms
    yield 1
    blist, m = (1,), 1
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=m)))[-1]
        m += 2*i+1
A000697_list = list(islice(A000697_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000697_list)
