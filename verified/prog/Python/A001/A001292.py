from itertools import count, islice
def A001292gen():
    s = []
    for i in count(1):
        s.append(str(i))
        yield from sorted(int("".join(s[j:]+s[:j])) for j in range(i))
print(list(islice(A001292gen(), 46))) # _Michael S. Branicky_, Jul 01 2022