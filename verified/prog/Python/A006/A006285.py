from itertools import count, islice
from sympy import isprime
def A006285_gen(startvalue=1): # generator of terms
    return filter(lambda n: not any(isprime(n-(1<<i)) for i in range(n.bit_length()-1,-1,-1)), count(max(startvalue+(startvalue&1^1),1),2))
A006285_list = list(islice(A006285_gen(),30)) # _Chai Wah Wu_, Nov 29 2023
print(A006285_list)
