def aupto(lim):
    s, pow3 = set(), 1
    while pow3 < lim:
        for j in range((lim-pow3).bit_length()):
            s.add(2**j + pow3)
        pow3 *= 3
    return sorted(set(s))
print(aupto(756)) # _Michael S. Branicky_, Jul 29 2021