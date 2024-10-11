from itertools import count, islice, product
def agen():
    yield from [0, 1, 8]
    for d in count(2):
        for start in "18":
            for rest in product("018", repeat=d//2-1):
                left = start + "".join(rest)
                for mid in [[""], ["0", "1", "8"]][d%2]:
                    yield int(left + mid + left[::-1])
print(list(islice(agen(), 42))) # _Michael S. Branicky_, Mar 29 2022