from itertools import accumulate, groupby, repeat
def summarize(n, _): return int("".join(bin(len(list(g)))[2:]+k for k, g in groupby(str(n))))
def aupto(terms): return list(accumulate(repeat(1, terms), summarize))
print(aupto(11)) # _Michael S. Branicky_, Sep 18 2022