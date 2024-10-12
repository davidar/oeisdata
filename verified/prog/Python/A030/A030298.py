from itertools import permutations, count, chain, islice
def A030298_gen(): # generator of terms
    return chain.from_iterable(p for l in count(2) for p in permutations(range(1,l)))
A030298_list = list(islice(A030298_gen(),30)) # _Chai Wah Wu_, Mar 21 2022
print(A030298_list)
