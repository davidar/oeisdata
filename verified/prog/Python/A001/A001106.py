def aList(): # Intended to compute the initial segment of the sequence, not isolated terms.
     x, y = 1, 1
     yield 0
     while True:
         yield x
         x, y = x + y + 7, y + 7
A001106 = aList()
print([next(A001106) for i in range(49)]) # _Peter Luschny_, Aug 04 2019