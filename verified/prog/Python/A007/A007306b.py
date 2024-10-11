from functools import reduce
def A007306(n): return sum(reduce(lambda x,y:(x[0],sum(x)) if int(y) else (sum(x),x[1]),bin((n<<1)-1)[-1:2:-1],(1,0))) if n else 1 # _Chai Wah Wu_, May 18 2023
print([A007306(n) for n in range(30)])
