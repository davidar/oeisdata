from itertools import count, takewhile, combinations_with_replacement as mc
def aupto(limit):
    pows4 = list(takewhile(lambda x: x <= limit, (i**4 for i in count(1))))
    sum10 = set(sum(c) for c in mc(pows4, 10) if sum(c) <= limit)
    return sorted(sum10)
print(aupto(465)) # _Michael S. Branicky_, Oct 25 2021