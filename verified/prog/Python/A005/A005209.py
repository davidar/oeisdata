from itertools import count, islice
def agen(): # generator of terms
    for k in count(1):
        n = k
        for i in range(k-1, 0, -1): n = 2*n-((n-1)%i)-1
        yield n
print(list(islice(agen(), 32))) # _Michael S. Branicky_, Aug 06 2022 after _Tom Duff_