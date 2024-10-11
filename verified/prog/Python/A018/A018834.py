from itertools import count, islice
def A018834_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:str(n) in str(n**2), count(max(startvalue,0)))
A018834_list = list(islice(A018834_gen(),20)) # _Chai Wah Wu_, Apr 04 2023
print(A018834_list)
