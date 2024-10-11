# second version based on recurrence
def a(n): return 12 if n == 0 else [4, 1, 5, 3, 3, 5, 1, 4, 24][(n-1)%9]
print([a(n) for n in range(84)]) # _Michael S. Branicky_, Dec 04 2021