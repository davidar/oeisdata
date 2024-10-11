def aupto(limit):
  s = [i*i for i in range(1, int(limit**.5)+2) if i*i < limit]
  s2 = set(a+b for i, a in enumerate(s) for b in s[i+1:] if a+b <= limit)
  return sorted(s2)
print(aupto(197)) # _Michael S. Branicky_, May 10 2021