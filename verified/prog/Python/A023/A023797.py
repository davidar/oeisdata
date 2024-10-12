from itertools import combinations, islice
def agen(): # generator of terms
    yield 0
    for d in range(1, 17):
        yield from sorted(int("".join(c), 16) for c in combinations("FEDCBA9876543210", d) if c[0] != '0')
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Feb 05 2024