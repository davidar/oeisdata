from itertools import count, islice
from sympy import primefactors
def A004614_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n: n&1 and all(p&2 for p in primefactors(n>>(~n & n-1).bit_length())), count(max(startvalue,1)))
A004614_list = list(islice(A004614_gen(),30)) # _Chai Wah Wu_, Aug 21 2024
print(A004614_list)
