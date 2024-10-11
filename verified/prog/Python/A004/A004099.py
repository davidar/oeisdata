from itertools import accumulate, islice
def A004099_gen(): # generator of terms
    yield from (1,1)
    blist = (0,1)
    while True:
        blist = tuple(accumulate(reversed(blist),initial=0))
        yield sum(int(d) for d in str(blist[-1]))
A004099_list = list(islice(A004099_gen(),30)) # _Chai Wah Wu_, Apr 17 2023
print(A004099_list)
