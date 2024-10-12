def A027868(n): return 0 if n<5 else n//5 + A027868(n//5) # _David Radcliffe_, Jun 26 2016
print([A027868(n) for n in range(30)])
