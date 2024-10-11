from itertools import islice
def A003312_gen(): # generator of terms
    a = 3
    while True:
        yield a
        a += a-1>>1
A003312_list = list(islice(A003312_gen(),30)) # _Chai Wah Wu_, Sep 21 2022
print(A003312_list)
