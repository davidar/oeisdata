from itertools import combinations_with_replacement as combs_with_rep
def aupto(limit):
  qd = [k**4 for k in range(1, int(limit**.25)+2) if k**4 + 4 <= limit]
  ss = set(sum(c) for c in combs_with_rep(qd, 5))
  return sorted(s for s in ss if s <= limit)
print(aupto(800)) # _Michael S. Branicky_, May 20 2021