def A004760(n): return m+(1<<m.bit_length()) if (m:=n-2)>0 else n-1 # _Chai Wah Wu_, Jul 26 2023
print([A004760(n) for n in range(1,31)])
