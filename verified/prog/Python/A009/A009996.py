from itertools import count, islice, combinations_with_replacement as mc
def agen(): # generator of terms
    yield 0
    for d in count(1):
        ni = (int("".join(m)) for m in mc("9876543210", d) if m[0]!="0")
        yield from sorted(ni)
print(list(islice(agen(), 70))) # _Michael S. Branicky_, Jun 24 2022