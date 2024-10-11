# Intended to compute the initial segment of the sequence, not
# isolated terms. If in the iteration the line "x, y = x + y + 1, y + 1"
# is replaced by "x, y = x + y + k, y + k" then the figurate numbers are obtained,
# for k = 0 (natural A001477), k = 1 (triangular), k = 2 (squares), k = 3 (pentagonal), k = 4 (hexagonal), k = 5 (heptagonal), k = 6 (octagonal), etc.
def aList():
    x, y = 1, 1
    yield 0
    while True:
        yield x
        x, y = x + y + 1, y + 1
A000217 = aList()
print([next(A000217) for i in range(54)]) # _Peter Luschny_, Aug 03 2019