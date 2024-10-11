# Intended to compute the initial segment of the sequence, not isolated terms.
def aList():
     x, y = 1, 1
     yield 0
     while True:
         yield x
         x, y = x + y + 4, y + 4
A000384 = aList()
print([next(A000384) for i in range(49)]) # _Peter Luschny_, Aug 04 2019