# Intended to compute the initial segment of the sequence, not isolated terms.
def aList():
     x, y = 1, 1
     yield 0
     while True:
         yield x
         x, y = x + y + 5, y + 5
A000566 = aList()
print([next(A000566) for i in range(49)]) # _Peter Luschny_, Aug 04 2019