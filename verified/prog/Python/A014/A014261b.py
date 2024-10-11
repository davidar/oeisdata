from itertools import count, islice, product
def agen(): yield from (int("".join(p)) for d in count(1) for p in product("13579", repeat=d))
print(list(islice(agen(), 60))) # _Michael S. Branicky_, Jan 13 2022