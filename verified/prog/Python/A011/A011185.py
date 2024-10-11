from itertools import islice
def agen(): # generator of terms
    aset, sset, k = set(), set(), 0
    while True:
        k += 1
        while any(k+an in sset for an in aset): k += 1
        yield k; sset.update(k+an for an in aset); aset.add(k)
print(list(islice(agen(), 51))) # _Michael S. Branicky_, Feb 05 2023