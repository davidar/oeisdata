from itertools import islice
def A001285_gen(): # generator of terms
    yield 1
    blist = [1]
    while True:
        c = [3-d for d in blist]
        blist += c
        yield from c
A001285_list = list(islice(A001285_gen(),30)) # _Chai Wah Wu_, Nov 13 2022
print(A001285_list)
