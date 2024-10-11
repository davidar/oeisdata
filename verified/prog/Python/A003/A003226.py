from itertools import count, islice
from sympy.ntheory.modular import crt
def A003226_gen(): # generator of terms
    a = 0
    yield from (0,1)
    for n in count(0):
        b = sorted((int(crt(m:=(1<<n,5**n),(0,1))[0]), int(crt(m,(1,0))[0])))
        if b[0] > a:
            yield from b
            a = b[1]
        elif b[1] > a:
            yield b[1]
            a = b[1]
A003226_list = list(islice(A003226_gen(),15)) # _Chai Wah Wu_, Jul 25 2022
print(A003226_list)
