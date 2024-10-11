from itertools import count, islice
def agen():
    astr, preval = "121", 2
    yield from [1, 2, 1]
    while True:
        an = 3 - preval
        yield an
        astr += str(an)
        for l in range(len(astr)-1, 0, -1):
            idx = astr.rfind(astr[-l:], 0, len(astr)-1)
            if idx >= 0: preval = int(astr[idx+l]); break
print(list(islice(agen(), 105))) # _Michael S. Branicky_, Aug 03 2022