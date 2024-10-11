a=lambda n: 4*n**2-3*n # _Indranil Ghosh_, Jan 01 2017
def aList(): # Intended to compute the initial segment of the sequence, not isolated terms.
     x, y = 1, 1
     yield 0
     while True:
         yield x
         x, y = x + y + 8, y + 8
A001107 = aList()
print([next(A001107) for i in range(49)]) # _Peter Luschny_, Aug 04 2019