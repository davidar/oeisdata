from itertools import islice
def agen():
    yield 1; an = 1
    while True: yield an; an += sum(map(int, str(an)))
print(list(islice(agen(), 54))) # _Michael S. Branicky_, Jul 31 2022