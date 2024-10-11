from itertools import count, product
def agen():
    for d in count(1):
        for first in "1234":
            for p in product("01234", repeat=d-1):
                yield int((first+"".join(p))*2, 5)
g = agen()
print([next(g) for n in range(1, 49)]) # _Michael S. Branicky_, Jun 12 2021