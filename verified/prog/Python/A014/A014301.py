from itertools import count, islice
def A014301_gen(): # generator of terms
    yield from (0,1)
    a, b, c = 0, 3, 1
    for n in count(1):
        yield ((b:=b*((n<<1)+3<<1)//(n+2))-(a:=(c:=c*((n<<2)+2)//(n+2))-a>>1))//3
A014301_list = list(islice(A014301_gen(),20)) # _Chai Wah Wu_, Apr 27 2023
print(A014301_list)
