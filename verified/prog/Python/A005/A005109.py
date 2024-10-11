from itertools import islice
from sympy import nextprime
def A005109_gen(): # generator of terms
    p = 2
    while True:
        q = p-1
        q >>= (~q&q-1).bit_length()
        a, b = divmod(q,3)
        while not b:
            a, b = divmod(q:=a,3)
        if q==1:
            yield p
        p = nextprime(p)
A005109_list = list(islice(A005109_gen(),30)) # _Chai Wah Wu_, Mar 17 2023
print(A005109_list)
