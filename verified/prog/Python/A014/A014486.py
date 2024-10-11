from itertools import count, islice
from sympy.utilities.iterables import multiset_permutations
def A014486_gen(): # generator of terms
    yield 0
    for l in count(1):
        for s in multiset_permutations('0'*l+'1'*(l-1)):
            c, m = 0, (l<<1)-1
            for i in range(m):
                if s[i] == '1':
                    c += 2
                if c<i:
                    break
            else:
                yield (1<<m)+int(''.join(s),2)
A014486_list = list(islice(A014486_gen(),30)) # _Chai Wah Wu_, Nov 28 2023
print(A014486_list)
