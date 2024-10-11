def aupton(terms):
  alst, aset = [None, 1], {1}
  for n in range(1, terms):
    an = alst[n] + (1 if n not in aset else 2)
    alst.append(an); aset.add(an)
  return alst[1:]
print(aupton(68)) # _Michael S. Branicky_, May 14 2021