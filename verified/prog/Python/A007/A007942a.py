from itertools import count, islice
def agen(): # generator of terms
    s = "1"
    for n in count(2):
        yield int(s)
        s = str(n) + s + str(n)
print(list(islice(agen(), 14))) # _Michael S. Branicky_, Dec 09 2022