from itertools import count, islice
from sympy.ntheory.factor_ import primenu
def A023534_gen(startvalue=1): # generator of terms
    return filter(lambda n:(~n & n-1).bit_length() == primenu(n),count(max(startvalue,1)))
A023534_list = list(islice(A023534_gen(),30)) # _Chai Wah Wu_, Jul 05 2022
print(A023534_list)
