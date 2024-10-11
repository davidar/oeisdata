from sympy import isprime
from itertools import count, islice, product
def ud(s): return s[::-1].translate({ord('6'):ord('9'), ord('9'):ord('6')})
def agen():
    for d in count(2):
        for start in "1689":
            for rest in product("01689", repeat=d//2-1):
                left = start + "".join(rest)
                right = ud(left)
                for mid in [[""], ["0", "1", "8"]][d%2]:
                    t = int(left + mid + right)
                    if isprime(t):
                        yield t
print(list(islice(agen(), 33))) # _Michael S. Branicky_, Mar 29 2022