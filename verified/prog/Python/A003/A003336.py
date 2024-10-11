def aupto(lim):
  p1 = set(i**4 for i in range(1, int(lim**.25)+2) if i**4 <= lim)
  p2 = set(a+b for a in p1 for b in p1 if a+b <= lim)
  return sorted(p2)
print(aupto(10625)) # _Michael S. Branicky_, Mar 18 2021