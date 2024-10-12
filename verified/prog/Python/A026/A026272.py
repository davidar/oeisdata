from collections import Counter
from itertools import count, islice
def agen(): # generator of terms
    aset, alst, k, mink, counts = set(), [0], 0, 1, Counter()
    for n in count(1):
        for k in range(1, len(alst)-1):
            if k == alst[n-k-1] and counts[alst[n-k-1]] == 1: an = k; break
        else: an = mink
        yield an; aset.add(an); alst.append(an); counts.update([an])
        while mink in aset: mink += 1
print(list(islice(agen(), 66))) # _Michael S. Branicky_, Jun 27 2022