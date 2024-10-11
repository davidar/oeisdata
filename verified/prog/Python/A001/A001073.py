from itertools import islice
def agen():
    an = 0
    while True: s = str(an); yield from map(int, s); an += len(s)
print(list(islice(agen(), 67))) # _Michael S. Branicky_, Jul 26 2022