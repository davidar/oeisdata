from itertools import islice
def A003266_gen(): # generator of terms
    a,b,c = 1,1,1
    while True:
        yield c
        c *= a
        a, b = b, a+b
A003266_list = list(islice(A003266_gen(),20)) # _Chai Wah Wu_, Jan 11 2023
print(A003266_list)
