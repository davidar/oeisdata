def a(n):
    s, k = str(n), 0
    while not str(9**k).startswith(s): k += 1
    return k
print([a(n) for n in range(1, 74)]) # _Michael S. Branicky_, Dec 09 2021