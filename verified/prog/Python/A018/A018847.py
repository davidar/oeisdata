from itertools import count, islice
from sympy import isprime
def A018847_gen(): # generator of terms
    r, t, u = ''.maketrans('69','96'), set('0125689'), {0,1,2,5,8}
    for x in count(1):
        for y in range(10**(x-1),10**x):
            if y%10 in u:
                s = str(y)
                if set(s) <= t and isprime(m:=int(s+s[-2::-1].translate(r))):
                    yield m
        for y in range(10**(x-1),10**x):
            s = str(y)
            if set(s) <= t and isprime(m:=int(s+s[::-1].translate(r))):
                yield m
A018847_list = list(islice(A018847_gen(),20)) # _Chai Wah Wu_, Apr 09 2024
print(A018847_list)
