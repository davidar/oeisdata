def A004761(n): return m+(1<<m.bit_length()-1) if (m:=n-2) else n-1 # _Chai Wah Wu_, Jul 26 2023
print([A004761(n) for n in range(1,31)])
