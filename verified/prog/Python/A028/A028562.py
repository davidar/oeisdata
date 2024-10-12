from itertools import count, islice
def ispal(n): s = str(n); return s == s[::-1]
def agen():
    for k in count(0):
        if ispal(k*(k+6)):
            yield k*(k+6)
print(list(islice(agen(), 19))) # _Michael S. Branicky_, Jan 25 2022