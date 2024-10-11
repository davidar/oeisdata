from itertools import islice, accumulate
def A000738_gen(): # generator of terms
    blist, a, b = tuple(), 0, 1
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=a)))[-1]
        a, b = b, a+b
A000738_list = list(islice(A000738_gen(),30)) # _Chai Wah Wu_, Jun 11 2022
print(A000738_list)
