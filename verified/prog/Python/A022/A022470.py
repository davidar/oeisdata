from itertools import accumulate, groupby, repeat
def summarize(n, _):
  return int("".join(k+str(len(list(g))) for k, g in groupby(str(n))))
def aupton(nn): return list(accumulate(repeat(2, nn), summarize))
print(aupton(13)) # _Michael S. Branicky_, Feb 21 2021