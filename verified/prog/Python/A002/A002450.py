def A002450(n): return ((1<<(n<<1))-1)//3 # _Chai Wah Wu_, Jan 29 2023
print([A002450(n) for n in range(30)])
