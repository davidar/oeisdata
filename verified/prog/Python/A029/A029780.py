from itertools import count, islice
def A029780_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:set(str(n)) <= set(str(m:=n**2)) & set(str(n*m)), count(max(startvalue,0)))
A029780_list = list(islice(A029780_gen(),20)) # _Chai Wah Wu_, Apr 03 2023
print(A029780_list)
