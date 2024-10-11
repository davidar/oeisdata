from itertools import count, islice
def A014631_gen(): # generator of terms
    s, c =(1,), set()
    for i in count(0):
        for d in s:
            if d not in c:
                yield d
                c.add(d)
        s=(1,)+tuple(s[j]+s[j+1] for j in range(len(s)-1)) + ((s[-1]<<1,) if i&1 else ())
A014631_list = list(islice(A014631_gen(),30)) # _Chai Wah Wu_, Oct 17 2023
print(A014631_list)
