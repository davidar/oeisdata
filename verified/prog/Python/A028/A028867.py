from itertools import count, islice, combinations_with_replacement
from sympy import isprime
def A028867_gen(): # generator of terms
    yield from (2,3,5,7)
    a, b = {'1':1,'2':1,'3':2,'4':2,'5':2,'6':2,'7':3,'8':3,'9':4}, (1,3,7,9)
    for l in count(1):
        mlist = []
        for d in combinations_with_replacement('987654321',l):
            k = 10*int(''.join(d))
            for e in b[:a[d[-1]]]:
                if isprime(m:=k+e):
                    mlist.append(m)
        yield from sorted(mlist)
A028867_list = list(islice(A028867_gen(),30)) # _Chai Wah Wu_, Dec 25 2023
print(A028867_list)
