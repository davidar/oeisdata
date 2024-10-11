import math
def A006257(n):
     return 0 if n==0 else 2*(n-2**int(math.log(n,2)))+1 # _Indranil Ghosh_, Jan 11 2017
print([A006257(n) for n in range(30)])
