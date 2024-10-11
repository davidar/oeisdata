from itertools import count, islice
from sympy import factorint
def A000404_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        c = False
        for p in (f:=factorint(n)):
            if (q:= p & 3)==3 and f[p]&1:
                break
            elif q == 1:
                c = True
        else:
            if c or f.get(2,0)&1:
                yield n
A000404_list = list(islice(A000404_gen(),30)) # _Chai Wah Wu_, Jul 01 2022
print(A000404_list)
