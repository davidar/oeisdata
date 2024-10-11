def A010892(n): return [1,1,0,-1,-1,0][n%6] # Alec Mihailovs, Jan 01 2007
print([A010892(n) for n in range(30)])
