from sympy import isprime
def only17(n): return int(bin(n+1)[3:].replace('1', '7').replace('0', '1'))
def auptod(digs):
  return list(filter(isprime, (only17(i) for i in range(1, 2**(digs+1)-1))))
print(auptod(8)) # _Michael S. Branicky_, Jul 11 2021