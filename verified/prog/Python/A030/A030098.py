from math import isqrt
def ok(sq): return all(d in "02468" for d in str(sq))
def aupto(limit):
  sqs = (i*i for i in range(0, isqrt(limit)+1, 2))
  return list(filter(ok, sqs))
print(aupto(4080400)) # _Michael S. Branicky_, May 20 2021