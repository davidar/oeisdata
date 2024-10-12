from itertools import count, islice, combinations_with_replacement
from sympy import isprime
def A028864_gen(): # generator of terms
    yield from (2,3,5,7)
    a, b = {'1':0,'2':1,'3':1,'4':2,'5':2,'6':2,'7':2,'8':3,'9':3}, (1,3,7,9)
    for l in count(1):
        for d in combinations_with_replacement('123456789',l):
            k = 10*int(''.join(d))
            for e in b[a[d[-1]]:]:
                if isprime(m:=k+e):
                    yield m
A028864_list = list(islice(A028864_gen(),30)) # _Chai Wah Wu_, Dec 25 2023
print(A028864_list)
