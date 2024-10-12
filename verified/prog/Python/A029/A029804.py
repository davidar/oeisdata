def palQ8(n): # check if n is a palindrome in base 8
    s = oct(n)[2:]
    return s == s[::-1]
def palQgen10(l): # unordered generator of palindromes of length <= 2*l
    if l > 0:
        yield 0
        for x in range(1,10**l):
            s = str(x)
            yield int(s+s[-2::-1])
            yield int(s+s[::-1])
A029804_list = sorted([n for n in palQgen10(6) if palQ8(n)])
# _Chai Wah Wu_, Nov 25 2014
print(A029804_list)
