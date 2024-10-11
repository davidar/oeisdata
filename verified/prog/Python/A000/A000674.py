from itertools import accumulate, islice
def A000674_gen(): # generator of terms
    yield 1
    blist = (1,)
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=2)))[-1]
A000674_list = list(islice(A000674_gen(),30)) # _Chai Wah Wu_, Jun 11 2022
print(A000674_list)
