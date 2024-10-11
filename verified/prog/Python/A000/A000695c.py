from itertools import count, islice
def A000695_gen(): # generator of terms
    yield (a:=0)
    for n in count(1):
        yield (a := a+((1<<((~n & n-1).bit_length()<<1)+1)+1)//3)
A000695_list = list(islice(A000695_gen(),30)) # _Chai Wah Wu_, Feb 22 2023
print(A000695_list)
