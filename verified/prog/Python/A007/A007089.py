def A007089(n):
  n,s = divmod(n,3); t = 1
  while n: n,r = divmod(n,3); t *= 10; s += r*t
  return s # _M. F. Hasler_, Feb 15 2023
print([A007089(n) for n in range(30)])
