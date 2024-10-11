def aupto(lim):
  p1 = set(i**4 for i in range(1, int(lim**.25)+2) if i**4 <= lim)
  p2 = set(a+b for a in p1 for b in p1 if a+b <= lim)
  p3 = set(apb+c for apb in p2 for c in p1 if apb+c <= lim)
  return sorted(p3)
print(aupto(2400)) # _Michael S. Branicky_, Mar 18 2021