from itertools import accumulate, count, islice
def A000745_gen(): # generator of terms
    blist, c = tuple(), 1
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=c)))[-1]
        c += 2*i+1
A000745_list = list(islice(A000745_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000745_list)
