from itertools import permutations
def pmap(s, m): return sum(s[i-1]*10**(m-i) for i in range(1, len(s)+1))
def agen():
  m = 1
  while True:
    for s in permutations(range(1, m+1)): yield pmap(s, m)
    m += 1
def aupton(terms):
  alst, g = [], agen()
  while len(alst) < terms: alst += [next(g)]
  return alst
print(aupton(42)) # _Michael S. Branicky_, Jan 12 2021