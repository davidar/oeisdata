def A020914(n): return (3**n).bit_length() # _Chai Wah Wu_, Oct 09 2024
print([A020914(n) for n in range(30)])
