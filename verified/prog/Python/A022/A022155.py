from itertools import count, islice
def A022155_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:(n&(n>>1)).bit_count()&1,count(max(startvalue,0)))
A022155_list = list(islice(A022155_gen(),30)) # _Chai Wah Wu_, Feb 11 2023
print(A022155_list)
