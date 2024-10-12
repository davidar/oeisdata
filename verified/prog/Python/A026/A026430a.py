from itertools import accumulate, islice
def A026430_gen(): # generator of terms
    yield from (0,1)
    blist, s = [1], 1
    while True:
        c = [3-d for d in blist]
        blist += c
        yield from (s+d for d in accumulate(c))
        s += sum(c)
A026430_list = list(islice(A026430_gen(),30)) # _Chai Wah Wu_, Feb 22 2023
print(A026430_list)
