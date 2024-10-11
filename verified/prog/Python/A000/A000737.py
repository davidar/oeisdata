from itertools import count, accumulate, islice
def A000737_gen(): # generator of terms
    blist = tuple()
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=i)))[-1]
A000737_list = list(islice(A000737_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000737_list)
