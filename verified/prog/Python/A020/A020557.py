from itertools import accumulate, islice
def A020557_gen(): # generator of terms
    yield 1
    blist, b = (1,), 1
    while True:
        for _ in range(2):
            blist = list(accumulate(blist, initial=(b:=blist[-1])))
        yield b
A020557_list = list(islice(A020557_gen(),30)) # _Chai Wah Wu_, Jun 22 2022
print(A020557_list)
