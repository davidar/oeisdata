from itertools import count
def aupton(terms):
    adict, pow2 = dict(), 1
    for i in count(0):
        s = str(pow2)
        for j in range(len(s)):
            t = int(s[:j+1])
            if t > terms:
                break
            if t not in adict:
                adict[t] = i
        if len(adict) == terms:
            return [adict[i+1] for i in range(terms)]
        pow2 *= 2
print(aupton(67)) # _Michael S. Branicky_, Apr 08 2023