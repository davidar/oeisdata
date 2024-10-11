from itertools import accumulate, groupby, repeat
def summarize(n, _): return int("".join(k+str(len(list(g))) for k, g in groupby(str(n))))
def aupto(terms): return list(accumulate(repeat(1, terms), summarize))
print(aupto(13)) # _Michael S. Branicky_, Sep 18 2022