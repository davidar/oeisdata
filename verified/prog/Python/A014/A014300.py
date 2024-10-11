from itertools import count, islice
def A014300_gen(): # generator of terms
    yield from (1,2)
    a, c = 1, 1
    for n in count(1):
        yield (a:=(3*n+5)*(c:=c*((n<<2)+2)//(n+2))-a>>1)
A014300_list = list(islice(A014300_gen(),20)) # _Chai Wah Wu_, Apr 26 2023
print(A014300_list)
