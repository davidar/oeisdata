def agen(an):
  while True: yield an; an = int(bin(an)[2:])
g = agen(3)
print([next(g) for i in range(5)]) # _Michael S. Branicky_, Mar 11 2021