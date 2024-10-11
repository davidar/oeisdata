from itertools import count, islice, product
def bin_pals(): # generator of binary palindromes in base 10
    yield from [0, 1]
    digits, midrange = 2, [[""], ["0", "1"]]
    for digits in count(2):
        for p in product("01", repeat=digits//2-1):
            left = "1"+"".join(p)
            for middle in midrange[digits%2]:
                yield int(left + middle + left[::-1], 2)
print(list(islice(bin_pals(), 58))) # _Michael S. Branicky_, Jan 09 2023