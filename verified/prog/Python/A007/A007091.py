from gmpy2 import digits
def A007091(n): return int(digits(n,5)) # _Chai Wah Wu_, Dec 26 2021
print([A007091(n) for n in range(30)])
