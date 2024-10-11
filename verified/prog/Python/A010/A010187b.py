# second version based on linear recurrence
def a(n): return 11 if n == 0 else [4, 2, 4, 22][(n-1)%4]
print([a(n) for n in range(72)]) # _Michael S. Branicky_, Nov 04 2021