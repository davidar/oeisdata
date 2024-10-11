def aupton(terms):
  alst = [2, 7]
  for n in range(2, terms):
    sums = [alst[j]+alst[k] for j in range(n-1) for k in range(j+1, n)]
    alst.append(min([s for s in sums if sums.count(s)==1 and s > alst[-1]]))
  return alst
print(aupton(60)) # _Michael S. Branicky_, Feb 07 2021