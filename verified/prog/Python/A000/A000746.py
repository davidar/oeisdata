from itertools import accumulate, count, islice
def A000746_gen(): # generator of terms
    blist, c = tuple(), 1
    for i in count(2):
        yield (blist := tuple(accumulate(reversed(blist),initial=c)))[-1]
        c += i
A000746_list = list(islice(A000746_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000746_list)
