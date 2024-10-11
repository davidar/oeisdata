from itertools import accumulate, count, islice
def A000754_gen(): # generator of terms
    blist = tuple()
    for i in count(1,2):
        yield (blist := tuple(accumulate(reversed(blist),initial=i)))[-1]
A000754_list = list(islice(A000754_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000754_list)
