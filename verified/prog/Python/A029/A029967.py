from gmpy2 import digits
def palQ(n,b): # check if n is a palindrome in base b
    s = digits(n,b)
    return s == s[::-1]
def palQgen10(l): # generator of palindromes in base 10 of length <= 2*l
    if l > 0:
        yield 0
        for x in range(1,l+1):
            for y in range(10**(x-1),10**x):
                s = str(y)
                yield int(s+s[-2::-1])
            for y in range(10**(x-1),10**x):
                s = str(y)
                yield int(s+s[::-1])
A029967_list = [n for n in palQgen10(5) if palQ(n,12)] # _Chai Wah Wu_, Dec 01 2014
print(A029967_list)
