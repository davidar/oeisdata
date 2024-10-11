def A006257(n): return bool(n&(m:=1<<n.bit_length()-1))+((n&m-1)<<1) if n else 0 # _Chai Wah Wu_, Jan 22 2023
print([A006257(n) for n in range(30)])
