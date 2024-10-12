from itertools import count, islice
def ispal(n): s = str(n); return s == s[::-1]
def agen():
    for k in count(0):
        if ispal(k*(k+7)):
            yield k
print(list(islice(agen(), 26))) # _Michael S. Branicky_, Jan 26 2022