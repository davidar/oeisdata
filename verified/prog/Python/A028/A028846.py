from itertools import count, islice, product
def agen(): yield from (int("".join(p)) for d in count(1) for p in product("1248", repeat=d))
print(list(islice(agen(), 64))) # _Michael S. Branicky_, Aug 21 2022