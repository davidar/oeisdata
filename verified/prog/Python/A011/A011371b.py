# 3.10+
def A011371(n): return n-n.bit_count() # _Chai Wah Wu_, Jul 09 2022
print([A011371(n) for n in range(30)])
