from itertools import count, islice
def A010672_gen(): # generator of terms
    aset2, alist = set(), []
    for k in count(0):
        bset2 = set()
        for a in alist:
            if (b:=a+k) in aset2:
                break
            bset2.add(b)
        else:
            yield k
            alist.append(k)
            aset2.update(bset2)
A010672_list = list(islice(A010672_gen(),30)) # _Chai Wah Wu_, Sep 11 2023
print(A010672_list)
