# second version based on linear recurrence
def a(n): return 11 if n == 0 else [5, 1, 1, 5, 22][(n-1)%5]
print([a(n) for n in range(75)]) # _Michael S. Branicky_, Nov 05 2021