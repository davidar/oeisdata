from itertools import chain, count, islice
def altgen(seed, digits):
    allowed = "02468" if seed in "13579" else "13579"
    if digits == 1: yield from allowed; return
    for f in allowed: yield from (f + r for r in altgen(f, digits-1))
def agen(): yield from chain(range(10), (int(f+r) for d in count(2) for f in "123456789" for r in altgen(f, d-1)))
print(list(islice(agen(), 65))) # _Michael S. Branicky_, Jul 12 2022