from itertools import count, islice
def A025582_gen(): # generator of terms
    aset1, aset2, alist = set(), set(), []
    for k in count(0):
        bset2 = {k<<1}
        if (k<<1) not in aset2:
            for d in aset1:
                if (m:=d+k) in aset2:
                    break
                bset2.add(m)
            else:
                yield k
                alist.append(k)
                aset1.add(k)
                aset2 |= bset2
A025582_list = list(islice(A025582_gen(),20)) # _Chai Wah Wu_, Sep 01 2023
print(A025582_list)
