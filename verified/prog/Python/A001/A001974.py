from itertools import combinations
def aupto(lim):
  s = filter(lambda x: x <= lim, (i*i for i in range(int(lim**.5)+2)))
  s3 = set(filter(lambda x: x<=lim, (sum(c) for c in combinations(s, 3))))
  return sorted(s3)
print(aupto(113)) # _Michael S. Branicky_, May 10 2021