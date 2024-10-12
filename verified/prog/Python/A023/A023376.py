from itertools import islice
def A023376_gen(): # generator of terms
    a = 2
    while True:
        yield 1<<a
        a += a>>1
A023376_list = list(islice(A023376_gen(),20)) # _Chai Wah Wu_, Sep 21 2022
print(A023376_list)
