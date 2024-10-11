from itertools import accumulate, count, islice
def A000736_gen(): # generator of terms
    yield 1
    blist, c = (1,), 1
    for i in count(0):
        yield (blist := tuple(accumulate(reversed(blist),initial=c)))[-1]
        c = c*(4*i+2)//(i+2)
A000736_list = list(islice(A000736_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000736_list)
