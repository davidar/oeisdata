from itertools import count, islice, product
def ud(s): return s[::-1].translate({ord('6'):ord('9'), ord('9'):ord('6')})
def A018846gen(): # generator of terms
    yield from [0, 1, 2, 5, 8]
    for d in count(2):
        for first in "125689":
            for rest in product("0125689", repeat=d//2-1):
                left = first + "".join(rest)
                for mid in [[""], ["0", "1", "2", "5", "8"]][d%2]:
                    yield int(left + mid + ud(left))
print(list(islice(A018846gen(), 54))) # _Michael S. Branicky_, Jul 09 2022