from gmpy2 import digits
def palQgen(l,b): # generator of palindromes in base b of length <= 2*l
    if l > 0:
        yield 0
        for x in range(1,l+1):
            for y in range(b**(x-1),b**x):
                s = digits(y,b)
                yield int(s+s[-2::-1],b)
            for y in range(b**(x-1),b**x):
                s = digits(y,b)
                yield int(s+s[::-1],b)
A029955_list = list(palQgen(4,9)) # _Chai Wah Wu_, Dec 01 2014
print(A029955_list)
