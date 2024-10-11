from itertools import accumulate, count, islice
def A000718_gen(): # generator of terms
    yield 1
    blist, c = (1,), 1
    for i in count(2):
        yield (blist := tuple(accumulate(reversed(blist),initial=c)))[-1]
        c += i
A000718_list = list(islice(A000718_gen(),30)) # _Chai Wah Wu_, Jun 11 2022
print(A000718_list)
