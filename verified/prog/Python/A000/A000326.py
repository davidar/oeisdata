# Intended to compute the initial segment of the sequence, not isolated terms.
def aList():
     x, y = 1, 1
     yield 0
     while True:
         yield x
         x, y = x + y + 3, y + 3
A000326 = aList()
print([next(A000326) for i in range(47)]) # _Peter Luschny_, Aug 04 2019