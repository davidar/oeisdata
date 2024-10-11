def A003132(n): return sum(int(d)**2 for d in str(n)) # _Chai Wah Wu_, Apr 02 2021
print([A003132(n) for n in range(30)])
