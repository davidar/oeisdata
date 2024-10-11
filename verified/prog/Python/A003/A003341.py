from itertools import combinations_with_replacement as mc
def aupto(limit):
    qd = [k**4 for k in range(1, int(limit**.25)+2) if k**4 + 6 <= limit]
    ss = set(sum(c) for c in mc(qd, 7))
    return sorted(s for s in ss if s <= limit)
print(aupto(630)) # _Michael S. Branicky_, Jul 22 2021