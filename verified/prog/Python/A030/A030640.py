def A030640(n): return (-(n+1>>1) if n&2 else n+1>>1) if n&1 else (-n-1 if n&2 else n+1) # _Chai Wah Wu_, Aug 05 2024
print([A030640(n) for n in range(30)])
