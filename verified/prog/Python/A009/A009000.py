from math import isqrt
def aupto(limit):
  s = [i*i for i in range(1, limit+1)]
  s2 = sorted(a+b for i, a in enumerate(s) for b in s[i+1:])
  return [isqrt(k) for k in s2 if k in s]
print(aupto(120)) # _Michael S. Branicky_, May 10 2021