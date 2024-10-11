from sympy import isprime
from itertools import count, takewhile
def A284971(n):
  b = bin(n+1)[3:]
  return int("".join(b.replace("0", "4").replace("1", "7")))
def aupto(limit):
  return list(filter(isprime, takewhile(lambda x: x <= limit, (A284971(n) for n in count(1)))))
print(aupto(47774747)) # _Michael S. Branicky_, Apr 07 2021