from itertools import chain, count, islice
def A001969_gen(): # generator of terms
    return chain((0,),chain.from_iterable((sorted(n^ n<<1 for n in range(2**l,2**(l+1))) for l in count(0))))
A001969_list = list(islice(A001969_gen(),30)) # _Chai Wah Wu_, Jun 29 2022
print(A001969_list)
