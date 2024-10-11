from itertools import count, islice
from sympy import factorint
def A000415_gen(startvalue=2): # generator of terms >= startvalue
    for n in count(max(startvalue,2)):
        f = factorint(n).items()
        if any(e&1 for p,e in f if p&3<3) and not any(e&1 for p,e in f if p&3==3):
            yield n
A000415_list = list(islice(A000415_gen(),20)) # _Chai Wah Wu_, Aug 01 2023
print(A000415_list)
