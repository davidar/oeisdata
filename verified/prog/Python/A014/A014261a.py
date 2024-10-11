from itertools import islice, count
def A014261(): return filter(lambda n: set(str(n)) <= {'1','3','5','7','9'}, count(1,2))
A014261_list = list(islice(A014261(),20)) # _Chai Wah Wu_, Nov 22 2021
print(A014261_list)
