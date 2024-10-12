from itertools import count, combinations_with_replacement
def A003634(n):
    for l in count(1):
        if 9*l*n < 10**(l-1): return 0
        c = 10**l
        for d in combinations_with_replacement(range(10),l):
            if sorted(str(a:=sum(d)*n)) == [str(e) for e in d] and a>0:
                c = min(c,a)
        if c < 10**l:
            return c # _Chai Wah Wu_, May 09 2023
print([A003634(n) for n in range(1,31)])
