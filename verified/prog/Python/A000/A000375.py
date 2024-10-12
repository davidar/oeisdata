from itertools import permutations as P
def ts(d, var=1): # algorithm VARiation
  s, m = 0, d[0]
  while m != 1:
    d = (d[:m])[::-1] + d[m:]
    s, m = s+1, d[0]
  if var==2: return s*(list(d)==sorted(d))
  return s
def a(n):
  return max(ts(d) for d in P(range(1, n+1)))
print([a(n) for n in range(1, 11)]) # _Michael S. Branicky_, Dec 11 2020