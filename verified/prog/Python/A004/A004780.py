from itertools import count, islice
def A004780_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:n&(n<<1), count(max(startvalue,1)))
A004780_list = list(islice(A004780_gen(),30)) # _Chai Wah Wu_, Jul 13 2022
print(A004780_list)
