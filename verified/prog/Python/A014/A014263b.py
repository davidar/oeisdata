from itertools import count, islice, product
def agen(): # generator of terms
    yield 0
    for d in count(1):
        for first in "2468":
            for rest in product("02468", repeat=d-1):
                yield int(first + "".join(rest))
print(list(islice(agen(), 58))) # _Michael S. Branicky_, Jan 13 2022