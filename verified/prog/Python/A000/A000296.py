from itertools import accumulate, islice
def A000296_gen():
    yield from (1,0)
    blist, a, b = (1,), 0, 1
    while True:
        blist = list(accumulate(blist, initial = (b:=blist[-1])))
        yield (a := b-a)
A000296_list = list(islice(A000296_gen(),20)) # _Chai Wah Wu_, Jun 22 2022
print(A000296_list)
