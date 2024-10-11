from itertools import islice
def agen():
    an = 1
    while True: yield an; an += an.bit_count()
print(list(islice(agen(), 61))) # _Michael S. Branicky_, Jul 31 2022