def A020330(n): return (n<<n.bit_length())|n # _Chai Wah Wu_, Feb 28 2023
print([A020330(n) for n in range(1,31)])
