from itertools import count, islice
def A000958_gen(): # generator of terms
    yield 1
    a, c = 0, 1
    for n in count(1):
        yield (c:=c*((n<<2)+2)//(n+2))+a>>1
        a = c-a>>1
A000958_list = list(islice(A000958_gen(),20)) # _Chai Wah Wu_, Apr 26 2023
print(A000958_list)
