from itertools import islice, combinations_with_replacement
def A010354_gen(): # generator of terms
    for k in range(1,30):
        a = tuple(i**k for i in range(8))
        yield from (x[0] for x in sorted(filter(lambda x:x[0] > 0 and tuple(int(d,8) for d in sorted(oct(x[0])[2:])) == x[1], \
                          ((sum(map(lambda y:a[y],b)),b) for b in combinations_with_replacement(range(8),k)))))
A010354_list = list(islice(A010354_gen(),20)) # _Chai Wah Wu_, Apr 20 2022
print(A010354_list)
