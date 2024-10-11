from itertools import count, islice
def agen(s=0): # generator of terms
    yield from (k for k in count(0) if (s:=s+str(k).count('1'))==k)
print(list(islice(agen(),26))) # _Michael S. Branicky_, Oct 02 2023