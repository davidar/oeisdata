from itertools import count, islice
def A000414_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:not(n in {0, 1, 3, 5, 9, 11, 17, 29, 41} or n>>((~n&n-1).bit_length()&-2) in {2,6,14}),count(max(startvalue,0)))
A000414_list = list(islice(A000414_gen(),30)) # _Chai Wah Wu_, Jul 09 2022
print(A000414_list)
