from itertools import count, islice
def A000957_gen(): # generator of terms
    yield from (0,1,0)
    a, c = 0, 1
    for n in count(1):
        yield (a:=(c:=c*((n<<2)+2)//(n+2))-a>>1)
A000957_list = list(islice(A000957_gen(),20)) # _Chai Wah Wu_, Apr 26 2023
print(A000957_list)
