def sd(n): return sum(map(int, str(n)))
def a(n):
  m = 1
  while m != n*sd(m): m += 1
  return m
print([a(n) for n in range(1,62)]) # _Michael S. Branicky_, Jan 18 2021