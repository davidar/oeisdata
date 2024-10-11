from itertools import count, takewhile
def aupto(lim):
    pows2 = list(takewhile(lambda x: x<lim, (2**i for i in count(0))))
    pows3 = list(takewhile(lambda x: x<lim, (3**i for i in count(0))))
    return sorted(c*d for c in pows2 for d in pows3 if c*d <= lim)
print(aupto(10**4)) # _Michael S. Branicky_, Jul 08 2022