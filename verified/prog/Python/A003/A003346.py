from itertools import count, takewhile, combinations_with_replacement as mc
def aupto(limit):
    qd = takewhile(lambda x: x <= limit, (k**4 for k in count(1)))
    ss = set(sum(c) for c in mc(qd, 12))
    return sorted(s for s in ss if s <= limit)
print(aupto(417)) # _Michael S. Branicky_, Dec 27 2021