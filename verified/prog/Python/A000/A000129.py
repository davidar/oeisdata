from itertools import islice
def A000129_gen(): # generator of terms
    a, b = 0, 1
    yield from [a,b]
    while True:
        a, b = b, a+2*b
        yield b
A000129_list = list(islice(A000129_gen(),20)) # _Chai Wah Wu_, Jan 11 2022
print(A000129_list)
