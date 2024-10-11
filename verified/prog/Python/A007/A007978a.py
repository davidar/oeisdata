def a(n):
    k = 2
    while not n%k: k += 1
    return k
print([a(n) for n in range(1, 101)]) # _Michael S. Branicky_, Jul 09 2022