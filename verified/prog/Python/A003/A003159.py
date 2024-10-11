from itertools import count, islice
def A003159_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:(n&-n).bit_length()&1,count(max(startvalue,1)))
A003159_list = list(islice(A003159_gen(),30)) # _Chai Wah Wu_, Jul 11 2022
print(A003159_list)
