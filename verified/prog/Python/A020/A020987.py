def A020987(n): return (n&(n>>1)).bit_count()&1 # _Chai Wah Wu_, Feb 11 2023
print([A020987(n) for n in range(30)])
