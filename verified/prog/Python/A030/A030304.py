from itertools import count, islice
def agen():
    k, chap = 0, "0"
    for n in count(0):
        target = bin(n)[2:]
        while chap.find(target) == -1: k += 1; chap += bin(k)[2:]
        yield chap.find(target)
print(list(islice(agen(), 70))) # _Michael S. Branicky_, Oct 06 2022