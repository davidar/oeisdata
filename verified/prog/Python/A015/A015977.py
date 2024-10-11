def ra(n): s = str(n); return int(s) + int(s[::-1])
def ispal(n): s = str(n); return s == s[::-1]
def aupto(limit):
  alst = []
  for k in range(limit+1):
    k2 = ra(k)
    if ispal(k2): continue
    if ispal(ra(k2)): alst.append(k)
  return alst
print(aupto(250)) # _Michael S. Branicky_, May 06 2021