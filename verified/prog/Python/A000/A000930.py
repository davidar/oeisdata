from itertools import islice
def A000930_gen(): # generator of terms
    blist = [1]*3
    while True:
        yield blist[0]
        blist = blist[1:]+[blist[0]+blist[2]]
A000930_list = list(islice(A000930_gen(),30)) # _Chai Wah Wu_, Feb 04 2022
print(A000930_list)
