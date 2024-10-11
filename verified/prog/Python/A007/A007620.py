from itertools import count, islice
from sympy import divisors
def A007620_gen(startvalue=1): # generator of terms >= startvalue
    for m in count(max(startvalue,1)):
        if m == 1:
            yield 1
        else:
            c = {0}
            for d in divisors(m,generator=True):
                if d < m:
                    c |= {a+d for a in c}
            if all(a in c for a in range(m+1)):
                yield m
A007620_list = list(islice(A007620_gen(),30)) # _Chai Wah Wu_, Jul 06 2023
print(A007620_list)
