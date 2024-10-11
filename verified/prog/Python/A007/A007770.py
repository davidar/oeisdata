def ssd(n): return sum(int(d)**2 for d in str(n))
def ok(n):
  while n not in [1, 4]: n = ssd(n) # iterate until fixed point or in cycle
  return n==1
def aupto(n): return [k for k in range(1, n+1) if ok(k)]
print(aupto(338)) # _Michael S. Branicky_, Jan 07 2021