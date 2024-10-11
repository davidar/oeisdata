def A004514(n): return (n&((1<<(m:=n.bit_length())+(m&1))-1)//3)<<1 # _Chai Wah Wu_, Jan 30 2023
print([A004514(n) for n in range(30)])
