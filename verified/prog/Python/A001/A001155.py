from itertools import accumulate, groupby, repeat
def summarize(n, _): return int("".join(str(len(list(g)))+k for k, g in groupby(str(n))))
def aupton(terms): return list(accumulate(repeat(0, terms), summarize))
print(aupton(11)) # _Michael S. Branicky_, Jun 28 2022