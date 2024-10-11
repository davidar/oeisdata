from itertools import islice
def A005428_gen(): # generator of terms
    a, c = 1, 0
    yield 1
    while True:
        yield (a:=1+((c:=c+a)>>1))
A005428_list = list(islice(A005428_gen(),30)) # _Chai Wah Wu_, Sep 21 2022
print(A005428_list)
