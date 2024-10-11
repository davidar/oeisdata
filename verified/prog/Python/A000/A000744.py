from itertools import accumulate, islice
def A000744_gen(): # generator of terms
    blist, a, b = tuple(), 1, 1
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=a)))[-1]
        a, b = b, a+b
A000744_list = list(islice(A000744_gen(),40)) # _Chai Wah Wu_, Jun 12 2022
print(A000744_list)
