from itertools import islice
def A016096_gen(): # generator of terms
    a = 9
    while True:
        yield a
        a += sum(int(d) for d in str(a))
A016096_list = list(islice(A016096_gen(),20)) # _Chai Wah Wu_, Mar 29 2022
print(A016096_list)
