from itertools import islice
def agen():
    yield 1
    an = s = 1
    while True:
        yield an
        an1 = an*s + an*(an+1)//2
        an, s = an1, s+an
print(list(islice(agen(), 10))) # _Michael S. Branicky_, Nov 14 2022