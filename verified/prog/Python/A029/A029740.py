# generates full sequence
from itertools import permutations
afull = sorted(set(int("".join(p)) for d in range(1, 11) for p in permutations("0123456789", d) if p[0] != "0" and p[-1] in "13579"))
print(afull[:100]) # _Michael S. Branicky_, Aug 04 2022