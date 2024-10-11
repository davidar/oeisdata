from itertools import count, islice
def A005282_gen(): # generator of terms
    aset1, aset2, alist = set(), set(), []
    for k in count(1):
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
A005282_list = list(islice(A005282_gen(),30)) # _Chai Wah Wu_, Sep 05 2023
print(A005282_list)
