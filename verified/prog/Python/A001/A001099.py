from itertools import accumulate, count, islice
def A001099_gen(): # generator of terms
    yield from accumulate((k**k for k in count(1)),func=lambda x,y:y-x)
A001099_list = list(islice(A001099_gen(),20)) # _Chai Wah Wu_, Jun 17 2022
print(A001099_list)
