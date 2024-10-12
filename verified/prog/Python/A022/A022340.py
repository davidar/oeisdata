from itertools import count, islice
def A022340_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:not n&(n>>1),count(max(0,startvalue+(startvalue&1)),2))
A022340_list = list(islice(A022340_gen(),30)) # _Chai Wah Wu_, Sep 07 2022
print(A022340_list)
